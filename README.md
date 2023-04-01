# Image Array Generator

This program generates an image array based on the provided parameters using Flask, a popular web framework for Python. You can use this API to generate image arrays of a specified width, height, color, and format.

## Requirements

To run this program, you need to have the following installed on your machine:

Python 3.x
Flask
NumPy
Pillow


## Installation

To install the required libraries, run the following command in your terminal:

```bash
pip install flask numpy pillow
```

## Usage

To use this program, run the `app.py` file in your terminal:

```bash
python app.py
```

This will start the Flask development server on your local machine. You can access the API using the following URL:

```bash
http://localhost:5000/generate_image?width=100&height=100&color=red&format=jpeg
```

This URL will generate a red image array of 100x100 pixels in JPEG format. You can customize the parameters to generate image arrays of different sizes, colors, and formats.

## API Endpoints
This program has the following API endpoint:

`/generate_image`
This endpoint generates an image array based on the provided parameters. It accepts GET requests with the following parameters:

`width:`: the width of the image array in pixels (integer)

`height`: the height of the image array in pixels (integer)

`color:` the color of the image (string, one of 'red', 'green', 'blue')

`format`: the format of the image (string, one of 'jpeg', 'png', 'gif')

If any of the provided parameters are invalid, the API returns an appropriate error message with a 400 Bad Request status code.

## License
This program is licensed under the MIT License. You are free to use, modify, and distribute this program for personal or commercial purposes. See the LICENSE file for more information.
