import os
import cv2

from flask import Flask, render_template, request, session, redirect, send_file

from utils import is_allowed_file
from cv_utils.click_handler import ClickHandler
from cv_utils.face_detector import FaceDetector

app = Flask(__name__, template_folder='templates', static_folder='static')
UPLOAD_FOLDER = os.path.join('static', 'uploads')
OUTPUT_FOLDER = os.path.join('static', 'output')

app.secret_key = 'not_a_secret'
os.path.dirname("../templates")
face_detector = FaceDetector()


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/', methods=["POST"])
def upload_file():
    if request.method == 'POST':
        _img = request.files['file-uploaded']
        filename = _img.filename
        is_allowed_file(filename)
        _img.save(os.path.join(UPLOAD_FOLDER, filename))
        session['uploaded_img_file_path'] = os.path.join(UPLOAD_FOLDER, filename)
        session['output_img_file_path'] = os.path.join(OUTPUT_FOLDER, filename)
        session['rectangles_drawn'] = False
        return render_template('index.html', success=True)


@app.route('/show_file')
def show_file():
    uploaded_image_path = session.get('uploaded_img_file_path', None)
    output_image_path = session.get("output_img_file_path", None)

    if not session.get('rectangles_drawn', None):
        output_image, faces = face_detector.detect_and_draw_rectangles(uploaded_image_path)
        cv2.imwrite(output_image_path, output_image)
        session['rectangles_drawn'] = True

    return render_template('show_file.html', user_image=output_image_path)


@app.route('/blur_face/<x>/<y>')
def blur_face(x, y):
    uploaded_image_path = session.get('uploaded_img_file_path', None)
    output_image_path = session.get("output_img_file_path", None)

    _, faces = face_detector.detect_and_draw_rectangles(uploaded_image_path)

    handler = ClickHandler(uploaded_image_path, output_image_path, faces)
    handler.save_img_with_blurred_face_on_click(int(x), int(y))

    return redirect('/show_file')


@app.route('/download_file')
def download():
    path = session.get("output_img_file_path", None)
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, port=8080)  # for local run
