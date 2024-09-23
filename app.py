from flask import Flask, request, jsonify, send_from_directory
import openai
import os
import json

app = Flask(__name__)

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a folder to store chat files
CHAT_FOLDER = os.path.join(os.getcwd(), 'chats')

# Ensure the folder exists
if not os.path.exists(CHAT_FOLDER):
    os.makedirs(CHAT_FOLDER)

@app.route('/')
def index():
    # Serve the index.html file from the static folder
    return send_from_directory('static', 'index.html')

@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'reply': 'No message provided'}), 400

    try:
        # Interact with GPT-3.5 Turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Leo, an AI assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({'reply': reply}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/save-chat', methods=['POST'])
def save_chat():
    data = request.get_json()
    chat_id = data.get('chatId')
    chat_data = data.get('chatData')

    if chat_id and chat_data:
        file_path = os.path.join(CHAT_FOLDER, f'{chat_id}.json')

        try:
            # Save chat data to a file
            with open(file_path, 'w') as chat_file:
                json.dump(chat_data, chat_file, indent=2)
            return jsonify({"message": "Chat saved successfully!"}), 200
        except Exception as e:
            return jsonify({"message": f"Error saving chat: {str(e)}"}), 500
    else:
        return jsonify({"message": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
