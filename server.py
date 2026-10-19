from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

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
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'mensaje': 'Servidor Flask con IA funcionando',
        'endpoint': '/ask',
        'metodo': 'POST',
        'ejemplo': {'prompt': 'Tu pregunta aquí'}
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
