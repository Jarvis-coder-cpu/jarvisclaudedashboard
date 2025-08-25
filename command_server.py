from flask import Flask, request, jsonify
from gpt_agent import ask_jarvis, get_jarvis_status
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.get_json()
    print("[JARVIS SERVER] Received:", data)
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'reply': 'No prompt received.'}), 400
    reply = ask_jarvis(prompt)
    return jsonify({'reply': reply})

@app.route('/status', methods=['GET'])
def get_status():
    """Real status endpoint to replace fake frontend data"""
    status_data = get_jarvis_status()
    print("[JARVIS SERVER] Status requested:", status_data)
    return jsonify(status_data)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'server': 'Jarvis Local Agent',
        'version': '1.0.0-local'
    })

if __name__ == '__main__':
    print("[JARVIS] Local Agent Server Starting...")
    print("[JARVIS] Endpoints available:")
    print("   POST /command - Jarvis command processing")
    print("   GET  /status  - Real system status")
    print("   GET  /health  - Health check")
    print("[JARVIS] Server running on http://localhost:5001")
    print("[JARVIS] Ready for LLM integration from external systems")
    app.run(host='localhost', port=5001, debug=True)
