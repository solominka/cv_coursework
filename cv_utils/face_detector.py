import cv2
from cv_utils.face import Face


class FaceDetector:

    def __init__(self):
        self.__face_cascade = cv2.CascadeClassifier('cv_utils/haarcascade_frontalface_default.xml')

    def detect_and_draw_rectangles(self, file_path):
        img = cv2.imread(file_path)
        prepped_img = prep_image(img)

        faces = self.__get_faces(prepped_img)
        img = draw_rectangles(img, faces)

        return img, faces

    def __get_faces(self, img):
        # Detect faces
        faces_raw = self.__face_cascade.detectMultiScale(img, 1.1, 4)
        faces = []
        for f in faces_raw:
            faces.append(Face(f[0], f[1], f[2], f[3]))
        return faces


def prep_image(img):
    # Convert into grayscale
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def draw_rectangles(img, faces):
    for f in faces:
        cv2.rectangle(img, (f.x, f.y), (f.x + f.w, f.y + f.h), (255, 0, 0), 2)
    return img
