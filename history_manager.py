import os
import json
from datetime import datetime

HISTORY_DIR = "history"


if not os.path.exists(HISTORY_DIR):
    os.makedirs(HISTORY_DIR)

def save_chat(chat_id, user_input, bot_response):
    """Save a chat message to history"""
    filepath = os.path.join(HISTORY_DIR, f"{chat_id}.json")
    timestamp = datetime.now().isoformat()

    try:
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                history = json.load(f)
        else:
            history = []

        history.append({
            "timestamp": timestamp,
            "user": user_input, 
            "bot": bot_response
        })

        with open(filepath, "w") as f:
            json.dump(history, f, indent=4)
            
        return True
    except Exception as e:
        print(f"Error saving chat: {e}")
        return False

def list_chats():
    """Get list of all chat sessions"""
    chats = []
    try:
        for f in os.listdir(HISTORY_DIR):
            if f.endswith(".json"):
                filepath = os.path.join(HISTORY_DIR, f)
                with open(filepath, "r") as file:
                    data = json.load(file)
                    if data:
                        # Get the last message timestamp
                        last_message = data[-1]
                        chats.append({
                            "id": f.split(".")[0],
                            "last_message": last_message["timestamp"],
                            "message_count": len(data)
                        })
        
       
        chats.sort(key=lambda x: x["last_message"], reverse=True)
        return [chat["id"] for chat in chats]
    except Exception as e:
        print(f"Error listing chats: {e}")
        return []

def load_chat(chat_id):
    """Load a specific chat session"""
    filepath = os.path.join(HISTORY_DIR, f"{chat_id}.json")
    try:
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                return json.load(f)
        return []
    except Exception as e:
        print(f"Error loading chat {chat_id}: {e}")
        return []

def delete_chat(chat_id):
    """Delete a specific chat session"""
    filepath = os.path.join(HISTORY_DIR, f"{chat_id}.json")
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            return True
        return False
    except Exception as e:
        print(f"Error deleting chat {chat_id}: {e}")
        return False

def clear_all_chats():
    """Clear all chat history"""
    try:
        for filename in os.listdir(HISTORY_DIR):
            if filename.endswith(".json"):
                filepath = os.path.join(HISTORY_DIR, filename)
                os.remove(filepath)
        return True
    except Exception as e:
        print(f"Error clearing chats: {e}")
        return False

def get_chat_info(chat_id):
    """Get information about a specific chat"""
    filepath = os.path.join(HISTORY_DIR, f"{chat_id}.json")
    try:
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                data = json.load(f)
                return {
                    "message_count": len(data),
                    "first_message": data[0]["timestamp"] if data else None,
                    "last_message": data[-1]["timestamp"] if data else None
                }
        return None
    except Exception as e:
        print(f"Error getting chat info {chat_id}: {e}")

        return None
