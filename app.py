import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    prompt = f"User: {user_input}\nChatGPT:"

    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate GPT-3 engine
        prompt=prompt,
        max_tokens=50  # Limit the response to a certain length
    )

    chatbot_response = response.choices[0].text.strip()
    return {'response': chatbot_response}

if __name__ == '__main__':
    app.run(debug=True)
