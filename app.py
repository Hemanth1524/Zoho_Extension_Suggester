
import google.generativeai as genai



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



def generate_text():
    prompt = "I need to Do the sms automation inside the zoho extension is suitable for that in the zoho marketplace?"
    response = model.generate_content(prompt)
    return response.text

if __name__ == '__main__':
    print(generate_text())