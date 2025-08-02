# 🎬 DesiScript - Indian Scriptwriting Agent

A powerful Streamlit-based AI scriptwriting assistant designed specifically for Indian cinema and storytelling. Generate engaging screenplays for short films, feature films, and web series using the Groq API with the Gemma2-9B-IT model.

## ✨ Features

- **🎭 Multiple Script Types**: Short Film, Feature Film, Web Series
- **🎞 Diverse Genres**: Drama, Comedy, Thriller, Romance, Mythology
- **🌏 Indian Settings**: Modern cities, villages, hill towns, historical periods
- **🎯 Various Tones**: Emotional, Dark, Wholesome, Satirical
- **📝 Customizable Length**: Adjustable word count (200-3000 words)
- **📥 Download Scripts**: Export generated scripts as text files
- **🎨 Beautiful UI**: Modern, responsive interface with custom theming

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/desiscript-agent.git
   cd desiscript-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run script_agent_ui.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 🔧 Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key (required)

### Customization

The app uses a custom theme defined in `.streamlit/config.toml`. You can modify colors, fonts, and other settings there.

## 📖 Usage

1. **Select Script Type**: Choose between Short Film, Feature Film, or Web Series
2. **Pick Genre**: Select from Drama, Comedy, Thriller, Romance, or Mythology
3. **Choose Setting**: Modern Indian City, Indian Village, Hill Town, or Historical Period
4. **Set Tone**: Emotional, Dark, Wholesome, or Satirical
5. **Add Characters**: Describe your characters (one per line)
6. **Share Your Idea**: Provide the central concept or imagination
7. **Adjust Length**: Use the slider to set approximate word count
8. **Generate**: Click "Generate Script" and wait for your screenplay!

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Gemma2-9B-IT via Groq API
- **Language**: Python 3.8+
- **Styling**: Custom Streamlit theme

## 📁 Project Structure

```
desiscript-agent/
├── script_agent_ui.py      # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (not in repo)
├── .gitignore            # Git ignore rules
├── README.md             # Project documentation
└── .streamlit/
    └── config.toml       # Streamlit configuration
```

## 🔒 Security

- API keys are stored in environment variables (`.env` file)
- The `.env` file is excluded from version control
- No sensitive data is hardcoded in the application

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Groq for providing fast AI inference
- Streamlit for the amazing web framework
- The Indian film industry for inspiration

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Made with ❤️ for Indian storytelling** 