import re
import random
import datetime
import requests
import os
import socket
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Check internet connectivity
def check_internet():
    try:
        socket.create_connection(("api.openweathermap.org", 80), timeout=5)
        return True
    except OSError:
        return False

# Enhanced weather function with better error handling and city extraction
def get_weather(city=None):
    # Check if API key is configured
    if not API_KEY or API_KEY == "your_api_key_here":
        return "Weather service is not configured. Please check the API key setup."
    
    # Check if city is provided
    if not city:
        return "Please specify a city. For example: 'weather in London'"
    
    # Check internet connectivity
    if not check_internet():
        return "No internet connection. Cannot fetch weather data."
    
    # Build request URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            desc = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]
            
            return (f"The weather in {city.title()} is {desc} with a temperature of {temp}°C "
                   f"(feels like {feels_like}°C). Humidity is {humidity}% and wind speed is {wind_speed} m/s.")
        
        elif response.status_code == 401:
            return "Invalid API key. Please check your OpenWeatherMap API configuration."
        
        elif response.status_code == 404:
            return f"Sorry, I couldn't find weather information for {city}."
        
        elif response.status_code == 429:
            return "Weather service is temporarily unavailable due to too many requests. Please try again later."
        
        else:
            return f"Sorry, I couldn't fetch the weather. (Error: {response.status_code})"
            
    except requests.exceptions.Timeout:
        return "Weather service request timed out. Please try again later."
    
    except requests.exceptions.RequestException as e:
        return f"Sorry, I'm having trouble connecting to the weather service. Error: {str(e)}"
    
    except KeyError:
        return "Received unexpected response from weather service."

# More comprehensive response function
def get_response(user_input):
    user_input = user_input.lower().strip()

    # Exit intent
    if re.search(r"\b(bye|exit|quit|goodbye|see you)\b", user_input):
        return random.choice([
            "Goodbye! Have a great day!",
            "See you later! 👋",
            "Bye! It was nice chatting with you!",
            "Talk to you soon! 👋"
        ])

    # Greetings
    if re.search(r"\b(hi|hello|hey|hola|greetings|howdy)\b", user_input):
        return random.choice([
            "Hi there! How can I help you today?",
            "Hello! What can I do for you?",
            "Hey! How can I assist you?",
            "Hi! I'm here to help. What do you need?"
        ])

    # Time
    if re.search(r"\b(time|what.time|current.time)\b", user_input):
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}"

    # Date
    if re.search(r"\b(date|today|what.date|current.date)\b", user_input):
        now = datetime.datetime.now()
        return f"Today is {now.strftime('%A, %B %d, %Y')}"

    # Weather with city extraction
    weather_match = re.search(r"\bweather\b.*\bin\b\s+([a-zA-Z\s]+)?|\bweather\b\s+in\s+([a-zA-Z\s]+)|([a-zA-Z\s]+)\s+\bweather\b", user_input)
    if weather_match:
        city = weather_match.group(1) or weather_match.group(2) or weather_match.group(3)
        if city:
            return get_weather(city.strip())
        else:
            return "Which city would you like the weather for?"

    # How are you
    if re.search(r"\b(how.are.you|how.do.you.do|how's.it.going)\b", user_input):
        return random.choice([
            "I'm doing great, thanks for asking! How can I help you?",
            "I'm functioning perfectly! What can I do for you today?",
            "All systems operational! How can I assist you?",
            "I'm good! Ready to help you with anything you need."
        ])

    # Thanks
    if re.search(r"\b(thanks|thank.you|appreciate.it|cheers)\b", user_input):
        return random.choice([
            "You're welcome! 😊",
            "Happy to help!",
            "Anytime! Let me know if you need anything else.",
            "Glad I could assist you!"
        ])

    # FAQ examples
    if re.search(r"\b(your.name|who.are.you|what's.your.name)\b", user_input):
        return "I'm AI-Lite, your helpful chatbot assistant! 🤖"

    if re.search(r"\b(who.made.you|who.created.you|who.built.you)\b", user_input):
        return "I was created by Raj Pawar 🚀"

    if re.search(r"\b(what.can.you.do|your.abilities|help.me)\b", user_input):
        return ("I can help you with various tasks like: \n"
                "- Telling you the current time and date \n"
                "- Providing weather information for any city \n"
                "- Answering questions about myself \n"
                "- Having a friendly conversation \n\n"
                "Just ask me anything!")

    # Jokes
    if re.search(r"\b(tell.a.joke|make.me.laugh|joke)\b", user_input):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
            "How does a penguin build its house? Igloos it together!",
            "Why don't eggs tell jokes? They'd crack each other up!"
        ]
        return random.choice(jokes)

    # Fallback with more varied responses
    fallback_responses = [
        "I'm not sure I understand. Could you rephrase that?",
        "That's an interesting question. I'm still learning though!",
        "I don't have an answer for that yet. Try asking me something else!",
        "I'm not programmed to handle that query. Maybe ask me about time, weather, or just say hello!",
        "I'm afraid I can't help with that. Is there something else I can assist you with?"
    ]
    return random.choice(fallback_responses)

# For testing the chatbot directly
if __name__ == "__main__":
    print("AI-Lite Chatbot (Console Mode)")
    print("Type 'exit' to quit\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Bot: Goodbye!")
            break
        
        response = get_response(user_input)

        print(f"Bot: {response}\n")
