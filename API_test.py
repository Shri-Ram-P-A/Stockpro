from flask import Flask, request, jsonify
import redis
from langchain_groq import ChatGroq

# Initialize Redis connection
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Initialize Flask app
app = Flask(__name__)

# Initialize Langchain with Groq LLM
llm = ChatGroq(
    temperature=0,
    groq_api_key='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',
    model_name="llama-3.1-70b-versatile"
)


def get_message_history(user_id):
    key = f"user:{user_id}:messages"
    return redis_client.lrange(key, 0, -1)


@app.route('/personal-ai-assistant/<user_id>', methods=['GET'])
def personal_ai_assistant(user_id):
    try:
        history = get_message_history(user_id)
        return jsonify({"history": history})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/personal-ai-assistant-chat', methods=['POST'])
def personal_ai_assistant_chat():
    try:
        input_data = request.json
        question = input_data.get("Question")

        if not question:
            return jsonify({'error': 'No question provided'}), 400

        ans = llm.invoke(
        f"""
        I am shri bot. I will answer your {question}
        """
        )

        return jsonify({'answer': ans.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
