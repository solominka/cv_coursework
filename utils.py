from http.client import UnimplementedFileMode


def is_allowed_file(filename):
    file_extension = filename.split(".")[-1]
    if file_extension not in ("jpg", "jpeg", "png"):
        raise UnimplementedFileMode()
