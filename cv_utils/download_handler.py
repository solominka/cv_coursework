import cv2


def save_file_to_download(original_file_path, download_file_path, faces):
    img = cv2.imread(original_file_path)
    result = img.copy()
    for f in faces:
        if f.is_blurred:
            blurred_part = cv2.blur(img[f.y:f.y + f.h, f.x:f.x + f.w], ksize=(100, 100))
            result[f.y:f.y + f.h, f.x:f.x + f.w] = blurred_part
    cv2.imwrite(download_file_path, result)
