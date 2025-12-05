from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from inference import run_inference

app = Flask(__name__)
CORS(app)

# Create upload directory if it doesn't exist
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    # Run YOLOv8 inference
    result = run_inference(file_path)
    
    # Return the path to the modified image
    return jsonify({
        'message': 'Inference completed',
        'image_url': f'http://localhost:5000/outputs/{os.path.basename(result["output_image"])}'
    })

# Route to serve the inference image
@app.route('/outputs/<filename>')
def send_inference_image(filename):
    return send_file(os.path.join('runs', 'detect', 'exp', filename), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
