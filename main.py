from flask import Flask, render_template, request, send_file
import os
from werkzeug.utils import secure_filename
from detect import detect_object

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

# Create folders if not exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    image = request.files['image']
    filename = secure_filename(image.filename)
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)

    labels, output_image = detect_object(image_path)

    return send_file(output_image, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
