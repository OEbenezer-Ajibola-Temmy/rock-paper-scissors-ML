from utils import *

from flask import Flask, request, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)




@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Get JSON data from the request
        # Get the base64-encoded image data
        base64_image_data = data.get('images')

        if not base64_image_data:
            return jsonify({'error': 'No image data provided.'})

        # Process the image using OpenCV
        result = process_image(base64_image_data)

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})




if __name__ == '__main__':
    app.run(debug=False)
