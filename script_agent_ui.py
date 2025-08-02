import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Groq API
openai.api_base = "https://api.groq.com/openai/v1"
openai.api_key = os.getenv("GROQ_API_KEY")

# Check if API key is available
if not openai.api_key:
    st.error("❌ GROQ_API_KEY not found in environment variables. Please check your .env file.")
    st.stop()

st.set_page_config(page_title="🎬 DesiScript – Scriptwriting Agent", layout="centered")
st.title("🎬 DesiScript – Your Indian Scriptwriting Assistant")
st.markdown("Craft powerful scenes for short films or feature-length stories.\n")

# --- Form for input ---
with st.form("script_form"):
    script_type = st.selectbox("🎭 Script Type", ["Short Film", "Feature Film", "Web Series"])
    genre = st.selectbox("🎞 Genre", ["Drama", "Comedy", "Thriller", "Romance", "Mythology"])
    setting = st.selectbox("🌏 Setting", ["Modern Indian City", "Indian Village", "Hill Town", "Historical Period"])
    tone = st.selectbox("🎯 Tone", ["Emotional", "Dark", "Wholesome", "Satirical"])
    characters = st.text_area("🧑‍🤝‍🧑 Character Names & Traits (one per line)", height=100, placeholder="e.g.\nRaj – introverted coder\nNeha – bold news anchor")
    idea = st.text_area("💡 Your Central Idea / Imagination", height=100, placeholder="A girl discovers a secret letter in an old diary in Delhi.")
    word_limit = st.slider("📝 Approx Word Count", 200, 3000, 800)
    submitted = st.form_submit_button("🎬 Generate Script")

# --- Generate Prompt ---
def craft_prompt(script_type, genre, setting, tone, characters, idea, word_limit):
    return f"""
You are an award-winning Indian screenwriter. Based on the following inputs, write a {script_type.lower()} screenplay in a {tone.lower()} tone.

**Genre:** {genre}  
**Setting:** {setting}  
**Characters:**  
{characters}

**Idea:**  
{idea}

Write the script in proper screenplay format with scene headings, character names, and realistic dialogues. Limit the response to approximately {word_limit} words. Start from the opening scene. Avoid over-explaining.
"""

# --- Call LLM ---
if submitted:
    if not idea.strip():
        st.warning("Please share your idea or imagination first.")
    else:
        with st.spinner("✍️ Writing the script..."):
            prompt = craft_prompt(script_type, genre, setting, tone, characters, idea, word_limit)
            try:
                response = openai.ChatCompletion.create(
                    model="gemma2-9b-it",
                    messages=[
                        {"role": "system", "content": "You are a professional Indian scriptwriter with expertise in creating engaging screenplays for various genres and formats."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=min(word_limit * 2, 4000)  # Adjust max_tokens based on word limit
                )
                script = response['choices'][0]['message']['content']
                st.success("✅ Script Generated Successfully!")
                st.markdown("### 🧾 Script Output")
                st.text_area("Screenplay", value=script, height=500, key="script_output")
                
                # Add download button
                st.download_button(
                    label="📥 Download Script",
                    data=script,
                    file_name=f"script_{script_type.lower().replace(' ', '_')}_{genre.lower()}.txt",
                    mime="text/plain"
                )
            except openai.error.AuthenticationError:
                st.error("❌ Authentication failed. Please check your GROQ_API_KEY.")
            except openai.error.RateLimitError:
                st.error("❌ Rate limit exceeded. Please try again later.")
            except openai.error.APIError as e:
                st.error(f"❌ API Error: {e}")
            except Exception as e:
                st.error(f"❌ Unexpected error: {e}")
                st.info("💡 Please check your internet connection and try again.")
