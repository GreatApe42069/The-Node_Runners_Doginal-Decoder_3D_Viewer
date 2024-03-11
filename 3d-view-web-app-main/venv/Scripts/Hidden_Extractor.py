# Hidden_Extractor.py

from stegano import lsb
from PIL import Image

def extract_hidden_message(filename):
    try:
        # Load the steganographed image
        steg_image = lsb.reveal(Image.open(filename))

        # Check if the hidden message contains '|||'
        if '|||' in steg_image:
            # Split the hidden message (transaction ID and phrase) using '|||'
            hidden_values = steg_image.split('|||')

            # Extract the hidden transaction ID and phrase
            hidden_transaction_id = hidden_values[0]
            hidden_phrase = hidden_values[1]

            # Return the extracted transaction ID and phrase
            return {
                'decoded_message': {
                    'transaction_id': hidden_transaction_id,
                    'hidden_phrase': hidden_phrase
                }
            }
        else:
            return {'error': 'No hidden message found in the image.'}
    except Exception as e:
        return {'error': str(e)}
