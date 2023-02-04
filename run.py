import os
from flask import Flask
from flask import render_template, redirect, url_for 
from flask import request

app = Flask(__name__)


"""This path operation returns a redirect for the path operation 'upload'
There is the landing page"""

@app.route('/')
def index():
    return redirect(url_for('upload'))


"""This path operation returns a GET method of the main template
'form_image.html' (These is a block that extends index.html)

If the method isn't GET, but instead it's POST, we save the image that send in './media' whith the name 'Imagen prueba'
and return a dict {"size" : size}
"""
@app.route('/upload', methods=["GET","POST"])
def upload():
    """Upload

    Returns:
        INT: size = returnImageSize(image_name)
    """
    if request.method == 'POST':
        #These are the image methods
        image = request.files['image']
        image_name = "Imagen prueba"
        images_dir = "./media"
        file_path = os.path.join(images_dir, image_name)
        image.save(file_path)
        #Size calls returnImageSize function
        size = returnImageSize(image_name)
        return {"size" : size}
    if request.method == 'GET':
        return render_template("form_image.html")


def returnImageSize(image_name):
    """_summary_

    Args:
        image_name (_str_): the name of the image saved on './media' folder 

    Returns:
        INT : size = (image size) 
    """
    size = os.stat(f'./media/{image_name}').st_size
    return size

if __name__ == ('__main__'):
    app.run()