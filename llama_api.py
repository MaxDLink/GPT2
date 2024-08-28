from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Initialize the OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Root URL route
@app.route('/')
def home():
    return "OpenAI API is running. Use /query to interact with the model."

@app.route('/query', methods=['POST'])
def query_openai():
    data = request.json
    queries = data.get('queries', [])

    responses = []
    for query in queries:
        # Call the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # or other models like "gpt-3.5-turbo"
            prompt=query,
            max_tokens=150
        )

        # Collect the response text
        result = response['choices'][0]['text'].strip()
        responses.append(result)

    return jsonify({'results': responses})

if __name__ == '__main__':
    app.run(port=5000)