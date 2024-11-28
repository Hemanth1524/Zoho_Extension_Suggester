from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key="AIzaSyCcbkTa-vHbMZZ3B0CRdP1lVca2RXqt4Zs")  # Replace with your actual API key
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
}
model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
)

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'Missing prompt'}), 400

    response = model.generate_content(prompt)
    return jsonify({'text': response.text})

if __name__ == '__main__':
    app.run(debug=True)