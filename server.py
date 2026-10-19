import logging
import os

from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Configurar la API de Google Generative AI
genai.configure(api_key="TU_API_KEY_AQUI")

# Crear el modelo
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/ask', methods=['POST'])
def ask():
    try:
        # Obtener el prompt del request
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'error': 'No se proporcionó un prompt'}), 400
        
        # Generar respuesta con IA
        response = model.generate_content(prompt)
        
        # Retornar la respuesta
        return jsonify({
            'response': response.text,
            'prompt': prompt
        })
    
    except Exception:
        # El detalle de la excepción va al log del servidor, no a la
        # respuesta: podría incluir la clave de API o detalles internos.
        logging.exception('Error al llamar al modelo')
        return jsonify({'error': 'No se pudo generar una respuesta. Intenta de nuevo.'}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'mensaje': 'Servidor Flask con IA funcionando',
        'endpoint': '/ask',
        'metodo': 'POST',
        'ejemplo': {'prompt': 'Tu pregunta aquí'}
    })

if __name__ == '__main__':
    # Por defecto: solo localhost y sin el depurador interactivo. El
    # depurador de Werkzeug (debug=True) permite ejecutar código arbitrario
    # desde el navegador si el servidor queda accesible en la red -- nunca
    # lo actives junto con host="0.0.0.0".
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    app.run(debug=debug, host=host, port=5000)
