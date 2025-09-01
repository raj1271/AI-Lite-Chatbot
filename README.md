 
# ðŸ¤– AI-Lite Chatbot  

An intelligent, lightweight chatbot built with **Python (Flask)** that can answer questions, provide weather updates, show time/date, crack jokes, and maintain chat history â€“ all inside a modern **responsive UI** powered by TailwindCSS.  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg) 
![Flask](https://img.shields.io/badge/Flask-2.3-green.svg) 
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-blueviolet.svg) 
![License](https://img.shields.io/badge/License-MIT-green.svg)  

---

## âœ¨ Features  
- ðŸ’¬ **Natural Conversations** â€“ Regex-based intent recognition (greetings, time, date, weather, jokes).  
- ðŸŒ¤ï¸ **Live Weather Updates** â€“ Integrated with OpenWeatherMap API.  
- ðŸ•‘ **Time & Date Support** â€“ Get the current time and date instantly.  
- ðŸ“š **Persistent Chat History** â€“ Chats saved in JSON (with option to reload, delete, or clear).  
- ðŸŽ¨ **Modern UI** â€“ Built with TailwindCSS, includes dark/light mode and typing indicators.  
- ðŸ“± **Responsive Design** â€“ Works smoothly on desktop and mobile.  
- âš¡ **Error Handling** â€“ Handles API errors, invalid inputs, and connectivity issues gracefully.  

---

## ðŸ—ï¸ Project Structure  

```
AI-Lite-Chatbot/
â”‚â”€â”€ app.py              # Flask server (routes, API endpoints)
â”‚â”€â”€ chatbot.py          # Chatbot logic & weather API integration
â”‚â”€â”€ history_manager.py  # JSON-based chat history management
â”‚â”€â”€ templates/
â”‚   â””â”€â”€ index.html      # Frontend UI (Tailwind + JS)
â”‚â”€â”€ history/            # Saved chat sessions (auto-created)
â”‚â”€â”€ requirements.txt    # Dependencies
```

---

## ðŸš€ Getting Started  

### Prerequisites  
- Python 3.8+  
- pip (Python package manager)  
- OpenWeatherMap API key (free)  

### Installation  
```bash
# Clone the repo
git clone https://github.com/raj1271/AI-Lite-Chatbot.git
cd AI-Lite-Chatbot

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Setup Environment Variables  
Create a `.env` file in the root folder and add your OpenWeatherMap API key:  
```bash
OPENWEATHER_API_KEY=your_api_key_here
```

### Run the Application  
```bash
python app.py
```
Then open: ðŸ‘‰ [http://localhost:5000](http://localhost:5000)  

---

## ðŸ“¸ Screenshots  

### ðŸ’» Chat UI (Dark Mode)  
![Chatbot UI Dark](https://via.placeholder.com/800x400.png?text=Chatbot+Dark+Mode+Screenshot)

### ðŸŒž Chat UI (Light Mode)  
![Chatbot UI Light](https://via.placeholder.com/800x400.png?text=Chatbot+Light+Mode+Screenshot)

---

## ðŸ› ï¸ Tech Stack  
- **Backend**: Python, Flask  
- **Frontend**: HTML, TailwindCSS, JavaScript  
- **Database/Storage**: JSON-based chat history  
- **API**: OpenWeatherMap  

---

## ðŸ™Œ Author  
ðŸ‘¨â€ðŸ’» Developed by **[Raj Pawar](https://github.com/raj1271)** ðŸš€  

---

## â­ Future Improvements  
- Add **FastAPI version** for better performance.  
- Integrate **SQLAlchemy / DB support** instead of JSON.  
- Deploy on **Heroku / Render / AWS**.  
- Add more intents (news, calculator, reminders).  