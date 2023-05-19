import json
from json import JSONEncoder, JSONDecoder


class Face:

    def __init__(self, x, y, w, h, is_blurred=False):
        (self.x, self.y, self.w, self.h, self.is_blurred) = (int(x), int(y), int(w), int(h), is_blurred)

    def to_json(self):
        return json.dumps(self, cls=FaceEncoder)


class FaceEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def from_json(face_json):
    face_dict = json.loads(face_json)
    face = Face(face_dict['x'], face_dict['y'], face_dict['w'], face_dict['h'], face_dict['is_blurred'])
    return face


def map_faces(faces):
    mapped = []
    for f in faces:
        mapped.append(f.to_json())
    return mapped


def unmap_faces(faces_json):
    unmapped = []
    for f in faces_json:
        unmapped.append(from_json(f))
    return unmapped
