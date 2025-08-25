from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from history_manager import save_chat, list_chats, load_chat, delete_chat, clear_all_chats
import os
import uuid
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    chats = list_chats()
    return render_template("index.html", chats=chats)

@app.route("/get", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message", "").strip()
        chat_id = request.json.get("chat_id")
        
        if not user_input:
            return jsonify({"response": "Please type a message.", "chat_id": chat_id})
        
        if not chat_id:  # if new chat, generate ID
            chat_id = str(uuid.uuid4())
        
        bot_response = get_response(user_input)
        save_chat(chat_id, user_input, bot_response)
        
        return jsonify({"response": bot_response, "chat_id": chat_id})
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({"response": "Sorry, I encountered an error processing your request.", "chat_id": chat_id or ""})

@app.route("/chat/<chat_id>")
def load_old_chat(chat_id):
    try:
        history = load_chat(chat_id)
        return jsonify(history)
    except Exception as e:
        print(f"Error loading chat {chat_id}: {e}")
        return jsonify([])

@app.route("/chats")
def get_chats():
    try:
        chats = list_chats()
        return jsonify(chats)
    except Exception as e:
        print(f"Error getting chats: {e}")
        return jsonify([])


@app.route("/chat/<chat_id>", methods=["DELETE"])
def delete_chat_route(chat_id):
    try:
        success = delete_chat(chat_id)
        return jsonify({"success": success})
    except Exception as e:
        print(f"Error deleting chat {chat_id}: {e}")
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/clear_chats", methods=["POST"])
def clear_chats():
    try:
        success = clear_all_chats()
        return jsonify({"success": success})
    except Exception as e:
        print(f"Error clearing chats: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/health")
def health_check():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    # Create necessary directories
    if not os.path.exists("history"):
        os.makedirs("history")
    
    print("Starting AI-Lite Chatbot Server...")
    print("Open http://localhost:5000 in your browser")

    app.run(debug=True, host='0.0.0.0', port=5000)
