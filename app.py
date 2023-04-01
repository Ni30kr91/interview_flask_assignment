from flask import Flask, request, Response
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

@app.route('/generate_image', methods=['GET'])
def generate_image():
    # Get parameters from the request
    width = request.args.get('width')
    height = request.args.get('height')
    color = request.args.get('color')
    img_format = request.args.get('format')

    # Check if parameters are valid
    if not width or not height or not color or not img_format:
        return Response("Missing parameters", status=400)

    if not width.isdigit() or not height.isdigit():
        return Response("Invalid width or height", status=400)

    if color not in ['red', 'green', 'blue']:
        return Response("Invalid color", status=400)

    if img_format not in ['jpeg', 'png', 'gif']:
        return Response("Invalid format", status=400)

    # Generate the image array
    img = np.zeros((int(height), int(width), 3), dtype=np.uint8)
    if color == 'red':
        img[:, :, 0] = 255
    elif color == 'green':
        img[:, :, 1] = 255
    elif color == 'blue':
        img[:, :, 2] = 255

    # Convert the image array to the specified format
    img = Image.fromarray(img)
    img_buffer = io.BytesIO()
    img.save(img_buffer, format=img_format)
    img_bytes = img_buffer.getvalue()

    # Return the image as a response
    return Response(img_bytes, mimetype='image/'+img_format)


if __name__ == "__main__":
    app.run(debug=True)