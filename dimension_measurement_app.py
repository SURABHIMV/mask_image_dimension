# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 12:12:28 2023

@author: h"p
"""
import numpy as np
import os
from flask import Flask,request,render_template,send_file
import dim_module
from werkzeug.utils import secure_filename
import io
import base64
import cv2
app = Flask(__name__)



@app.route('/')
def index():
    # Main page
    return render_template('index.html')



@app.route('/mask', methods=['POST'])
def mask_image():
    # Get the uploaded image file
    image = request.files['image']
    filename = secure_filename(image.filename)
    
    # Process the image (perform the masking operation)
    binary = dim_module.imag(filename)
    
    # Save the binary image
    destination_dir = 'C:/Users/hp/Pictures/dimension_measurement/images/dim_measure _images'
    os.makedirs(destination_dir, exist_ok=True)  # Create directory if it doesn't exist
    destination = os.path.join(destination_dir, filename + '.png')
    cv2.imwrite(destination, binary)
    
    # Convert the binary image data to Base64 string
    _, img_encoded = cv2.imencode('.png', binary) # Read and encode the input image as base64
    preprocessed_data = base64.b64encode(img_encoded).decode('utf-8')
    
    # Convert the input image to Base64 string
    input_data = base64.b64encode(image.read()).decode('utf-8')
    
    # Return the input and masked image to the user
    return render_template('index.html', input_data=input_data,preprocessed_data=preprocessed_data)




if __name__ == '__main__':
    app.run(debug=True)
    

        