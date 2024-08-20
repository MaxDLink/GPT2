from flask import Flask, request, jsonify

app = Flask(__name__)

# Root URL route
@app.route('/')
def home():
    return "Llama LLM API is running. Use /query to interact with the model."

@app.route('/query', methods=['POST'])
def query_llama():
    data = request.json
    queries = data.get('queries', [])

    responses = []
    for query in queries:
        # Run Llama command
        command = f'./llama.cpp/build/bin/llama-cli -m ./models/3B/Open_Llama_3B-3.4B-F16.gguf -p "{query}"'
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        
        # Collect the output
        response = result.stdout.decode('utf-8').strip()
        responses.append(response)

    return jsonify({'results': responses})

if __name__ == '__main__':
    app.run(port=5000)
