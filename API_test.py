from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)


@app.route('/personal-ai-assistant', methods=['GET'])
def personal_ai_assistant(user_id):
    try:
        return jsonify({"history": "hii"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/personal-ai-assistant-chat', methods=['POST'])
def personal_ai_assistant_chat():
    try:
        input_data = request.json
        question = input_data.get("Question")
        return jsonify({'answer': question})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
