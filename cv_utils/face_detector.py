import cv2


class FaceDetector:

    def __init__(self):
        self.__face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def detect_and_draw_rectangles(self, file_path):
        img = cv2.imread(file_path)
        prepped_ing = prep_image(img)

        faces = self.__get_faces_coordinates(prepped_ing)
        img = draw_rectangles(img, faces)

        return img, faces

    def __get_faces_coordinates(self, img):
        # Detect faces
        faces = self.__face_cascade.detectMultiScale(img, 1.1, 4)
        return faces


def prep_image(img):
    # Convert into grayscale
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def draw_rectangles(img, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img
