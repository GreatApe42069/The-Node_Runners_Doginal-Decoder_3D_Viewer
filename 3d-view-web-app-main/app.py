from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from stegano import lsb
from PIL import Image

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('3d-view-web_app_index.html')

@app.route('/decode', methods=['POST'])
def decode():
    try:
        # Assuming the image file is sent as a POST request
        image_file = request.files['image']

        # Load the steganographed image
        steg_image = lsb.reveal(Image.open(image_file))

        # Check if the hidden message contains '|||'
        if '|||' in steg_image:
            # Split the hidden message using '|||'
            hidden_values = steg_image.split('|||')

            # Extract the hidden transaction ID and phrase
            hidden_transaction_id = hidden_values[0]
            hidden_phrase = hidden_values[1]

            # Return the extracted transaction ID and phrase as JSON
            return jsonify({
                'transaction_id': hidden_transaction_id,
                'hidden_phrase': hidden_phrase
            })

        else:
            return jsonify({'error': 'No hidden message found in the image.'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
