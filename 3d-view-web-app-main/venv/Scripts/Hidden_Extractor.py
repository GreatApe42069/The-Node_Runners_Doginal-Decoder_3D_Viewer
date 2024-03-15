from stegano import lsb
from PIL import Image
import sys

try:
    # Check if an image file was dragged and dropped onto the script
    if len(sys.argv) > 1:
        # The first argument is the image file path, so the second argument is the script name
        steg_image_path = sys.argv[1]

        # Load the steganographed image
        steg_image = lsb.reveal(Image.open(steg_image_path))

        # Check if the hidden message contains '|||'
        if '|||' in steg_image:
            # Split the hidden message (transaction ID and phrase) using '|||'
            hidden_values = steg_image.split('|||')

            # Extract the hidden transaction ID and phrase
            hidden_transaction_id = hidden_values[0]
            hidden_phrase = hidden_values[1]

            # Print the extracted transaction ID and phrase
            print("Extracted Transaction ID:", hidden_transaction_id)
            print("Extracted Hidden Phrase:", hidden_phrase)
        else:
            print("No hidden message found in the image.")
    else:
        print("Please drag and drop an image file onto the script.")

except Exception as e:
    print(f"Error: {e}")
