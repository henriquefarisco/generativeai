import google.generativeai as genai
import os
import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

GOOGLE_API_KEY = 'SUA API AQUI DO GEMINI'

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash') #ESCOLHA A VERSÃO DA SUA IA

def add_line_numbers(code):
    lines = code.split('\n')
    numbered_lines = [f'<span class="line-number" data-line-number="{i+1}"></span>{line}' for i, line in enumerate(lines)]
    return '\n'.join(numbered_lines)

def format_response(text):
    # CÓDIGOS PARA MUDAR O ESTILO DA FONTE COM BASE NA RESPOSTA DO CHAT
    text = re.sub(r'```(.*?)```', lambda m: f'<pre><code>{add_line_numbers(m.group(1))}</code></pre>', text, flags=re.DOTALL)
    text = re.sub(r'`([^`]*)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = text.replace('\n', '<br>')
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')
    response = model.generate_content(user_input)
    formatted_response = format_response(response.text)
    return jsonify({'response': formatted_response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True) #COLOQUE SEU IP NO LUGAR DE 0.0.0.0
