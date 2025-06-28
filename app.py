from flask_cors import CORS
from flask import Flask, jsonify, request
from generate_patients import generate_breast_cancer_patients

app = Flask(__name__)
CORS(app)

@app.route('/generate_patients', methods=['GET'])
def generate_patients():
    count = int(request.args.get('count', 100))
    raw_text, patients = generate_breast_cancer_patients(count)
    if patients and isinstance(patients, list):
        return jsonify(patients)
    else:
        return jsonify({"error": "Failed to generate patients data"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)