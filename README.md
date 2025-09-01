------------------------------------------------------------
AI-Lite Chatbot  
------------------------------------------------------------

An intelligent, lightweight chatbot built with Python (Flask) that can answer questions, provide weather updates, show time/date, crack jokes, and maintain chat history â€“ all inside a modern responsive UI powered by TailwindCSS.  

------------------------------------------------------------
 Features
------------------------------------------------------------
- Natural Conversations â€“ Regex-based intent recognition (greetings, time, date, weather, jokes).
- Live Weather Updates â€“ Integrated with OpenWeatherMap API.
- Time & Date Support â€“ Get the current time and date instantly.
- Persistent Chat History â€“ Chats saved in JSON (with option to reload, delete, or clear).
- Modern UI â€“ Built with TailwindCSS, includes dark/light mode and typing indicators.
- Responsive Design â€“ Works smoothly on desktop and mobile.
- Error Handling â€“ Handles API errors, invalid inputs, and connectivity issues gracefully.  

------------------------------------------------------------
 Project Structure
------------------------------------------------------------
AI-Lite-Chatbot/
â”‚â”€â”€ app.py              # Flask server (routes, API endpoints)
â”‚â”€â”€ chatbot.py          # Chatbot logic & weather API integration
â”‚â”€â”€ history_manager.py  # JSON-based chat history management
â”‚â”€â”€ templates/
â”‚   â””â”€â”€ index.html      # Frontend UI (Tailwind + JS)
â”‚â”€â”€ history/            # Saved chat sessions (auto-created)
â”‚â”€â”€ requirements.txt    # Dependencies  

------------------------------------------------------------
 Getting Started
------------------------------------------------------------
Prerequisites:
- Python 3.8+
- pip (Python package manager)
- OpenWeatherMap API key (free)

Installation:
1. Clone the repo
   git clone https://github.com/raj1271/AI-Lite-Chatbot.git
   cd AI-Lite-Chatbot

2. Create virtual environment
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

Setup Environment Variables:
Create a .env file in the root folder and add your OpenWeatherMap API key:
   OPENWEATHER_API_KEY=your_api_key_here

Run the Application:
   python app.py
Then open: http://localhost:5000  

------------------------------------------------------------
 Tech Stack
------------------------------------------------------------
- Backend: Python, Flask
- Frontend: HTML, TailwindCSS, JavaScript
- Database/Storage: JSON-based chat history
- API: OpenWeatherMap  

------------------------------------------------------------
 Author
------------------------------------------------------------
Developed by Raj Pawar (https://github.com/raj1271) ðŸš€  

------------------------------------------------------------
 Future Improvements
------------------------------------------------------------
- Add FastAPI version for better performance.
- Integrate SQLAlchemy / DB support instead of JSON.
- Deploy on Heroku / Render / AWS.
- Add more intents (news, calculator, reminders).  