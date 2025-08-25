# AI-Lite Chatbot 🤖

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![OpenWeatherMap](https://img.shields.io/badge/API-OpenWeatherMap-orange.svg)](https://openweathermap.org/api)

A intelligent chatbot built with Python and Flask that can answer questions, provide weather information, tell time, and engage in conversation.

![Chatbot Demo](https://img.shields.io/badge/Demo-Live_Preview-brightgreen?style=for-the-badge)

</div>

## ✨ Features

- 🌟 **Natural Conversations**: Regex-based intent recognition for human-like interactions
- 🕐 **Time & Date**: Real-time current time and date information
- 🌤️ **Weather Data**: Live weather information for any city worldwide using OpenWeatherMap API
- 💾 **Chat History**: Persistent conversation history with JSON storage
- 🎨 **Beautiful UI**: Modern web interface built with Tailwind CSS
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- 🎯 **Contextual Responses**: Intelligent fallback handling for unknown queries
- 🔄 **Session Management**: Multiple chat sessions with history tracking

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- OpenWeatherMap API key (free)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-lite-chatbot.git
   cd ai-lite-chatbot

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
4. **Set up environment variables**
   
   Create a .env file in the root directory
   
   Add your OpenWeatherMap API key:
   ```bash
     OPENWEATHER_API_KEY=your_api_key_here
   ```
   Get a free API key from OpenWeatherMap
   
6. **Run the application**
   ```bash
   python app.py
   
7. **Open your browser and navigate to http://localhost:5000**


## 💬 How to Use

- Ask Questions Like:
- Greetings: "Hello", "Hi", "How are you?"

- Time: "What time is it?", "Current time please"

- Date: "What's the date today?", "What day is it?"

- Weather: "What's the weather?", "Weather in London", "How's the weather in Paris?"

- About: "Who made you?", "What can you do?", "What's your name?"

- Fun: "Tell me a joke", "Make me laugh"

- Exit: "Goodbye", "Bye", "Exit"

## Web Interface Features:

💬 Start new conversations with the "New Chat" button

📚 View and load previous chat history

🎨 Clean, modern UI with dark/light mode support

⚡ Real-time messaging with typing indicators

📱 Fully responsive design

## 🏗️ Project Structure

ai-lite-chatbot/
├── app.py                 # Main Flask application
├── chatbot.py            # Chatbot logic and response handling
├── history_manager.py    # Chat history management
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not tracked)
├── .gitignore           # Git ignore rules
├── README.md            # Project documentation
└── templates/
    └── index.html       # Main web interface template
   
   

