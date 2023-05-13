import cv2


class ClickHandler:

    def __init__(self, original_file_path, current_image_path, faces):
        self.faces = faces
        self.original_file_path = original_file_path  # for unblur
        self.current_image_path = current_image_path

        cv2.imwrite(current_image_path, cv2.imread(original_file_path))
        self.current_file_path = current_image_path

    def save_img_with_blurred_face_on_click(self, x, y):
        (x_face, y_face, w, h) = self.__get_face_by_click(x, y)

        if x_face != -1:
            blurred_img = self.__get_blurred_face(x_face, y_face, w, h)
            cv2.imwrite(self.current_file_path, blurred_img)

        return self.current_file_path

    def __get_face_by_click(self, x_click, y_click):
        for (x, y, w, h) in self.faces:
            if x <= x_click <= x + w and y <= y_click <= y + h:
                return x, y, w, h
        return -1, -1, -1, -1

    def __get_blurred_face(self, x, y, w, h):
        img = cv2.imread(self.current_file_path)
        blurred = img.copy()
        blurred_part = cv2.blur(img[y:y + h, x:x + w], ksize=(100, 100), )
        blurred[y:y + h, x:x + w] = blurred_part
        return blurred
