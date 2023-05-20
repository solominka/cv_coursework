import cv2

from cv_utils.face import Face


class ClickHandler:

    def __init__(self, original_file_path, current_image_path, faces):
        self.faces = faces
        self.original_file_path = original_file_path  # for unblur

        cv2.imwrite(current_image_path, cv2.imread(current_image_path))
        self.current_file_path = current_image_path

    def save_img_with_blurred_face_on_click(self, x, y):
        f = self.__get_face_by_click(x, y)

        if f.x != -1:
            blurred_img = self.__get_unblurred_face(f) if f.is_blurred else self.__get_blurred_face(f)
            cv2.imwrite(self.current_file_path, blurred_img)

        return self.current_file_path

    def __get_face_by_click(self, x_click, y_click):
        for f in self.faces:
            if f.x <= x_click <= f.x + f.w and f.y <= y_click <= f.y + f.h:
                return f
        return Face(-1, -1, -1, -1)

    def __get_blurred_face(self, f):
        img = cv2.imread(self.current_file_path)
        blurred = img.copy()
        blurred_part = cv2.blur(img[f.y:f.y + f.h, f.x:f.x + f.w], ksize=(100, 100), )
        blurred[f.y:f.y + f.h, f.x:f.x + f.w] = blurred_part
        f.is_blurred = True
        return blurred

    def __get_unblurred_face(self, f):
        original_img = cv2.imread(self.original_file_path)
        current_img = cv2.imread(self.current_file_path)

        unblurred = current_img.copy()
        unblurred[f.y:f.y + f.h, f.x:f.x + f.w] = original_img[f.y:f.y + f.h, f.x:f.x + f.w]
        f.is_blurred = False
        return unblurred
