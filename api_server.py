from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import tensorflow as tf
from utils import normalize_url, heuristic_score, tokenize_and_pad

app = Flask(__name__)
CORS(app)

# Global variables for models and tokenizer
model1 = None
model2 = None
tokenizer = None

def load_resources():
    global model1, model2, tokenizer
    try:
        model1 = tf.keras.models.load_model("model1_url.h5")
        model2 = tf.keras.models.load_model("model2_bilstm.h5")
        with open("tokenizer.pkl", "rb") as f:
            tokenizer = pickle.load(f)
        print("✅ Models and tokenizer loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load models/tokenizer: {e}")
        model1 = model2 = tokenizer = None

# Load resources at startup
load_resources()

@app.route('/predict', methods=['POST'])
def predict():
    if model1 is None or model2 is None or tokenizer is None:
        return jsonify({'error': 'Models not loaded'}), 500

    data = request.get_json()
    url_text = data.get('url', '').strip()
    if not url_text:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        domain, normalized_text, _ = normalize_url(url_text)
        pad = tokenize_and_pad(tokenizer, normalized_text, maxlen=100)
        p1 = float(model1.predict(pad).ravel()[0])
        p2 = float(model2.predict(pad).ravel()[0])
        model_conf = (p1 + p2) / 2
        heur = heuristic_score(domain, url_text)
        final_conf = 0.75 * model_conf + 0.25 * heur
        final_conf = min(max(final_conf, 0.0), 0.99)

        status = 'Phishing' if final_conf >= 0.5 else 'Safe'
        confidence = int(final_conf * 100)

        return jsonify({'status': status, 'confidence': confidence})
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
