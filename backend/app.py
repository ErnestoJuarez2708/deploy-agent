
import os
from flask import Flask, render_template, request, jsonify
from gemini_client import GeminiClient

# Inicializar Flask
app = Flask(__name__, template_folder='../templates')

# ⚡ Instancia global del agente de viajes (mantiene historial)
client = GeminiClient()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    payload = request.get_json(silent=True) or {}
    user_message = payload.get('message', '').strip()
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        # Usar la misma instancia del agente
        response_text = client.generate_response(user_message)
        return jsonify({'response': response_text})
    except Exception as e:
        return jsonify({'error': f'Error generating response: {str(e)}'}), 500

if __name__ == '__main__':
    # Escuchar en 0.0.0.0 para acceso externo (EC2)
    app.run(host='0.0.0.0', port=5000, debug=True)
