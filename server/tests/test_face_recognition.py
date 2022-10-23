import unittest
from components.face_recognition import get_face_locations, draw_face_locations


class TestFaceRecognition(unittest.TestCase):
    def test_get_face_locations(self):
        face_locations = get_face_locations("assets/BarackObama.jpg")
        self.assertEqual(len(face_locations), 1)
        self.assertEqual(face_locations[0], (0, 0, 0, 0))

    def test_draw_face_locations(self):
        face_locations = get_face_locations("assets/BarackObama.jpg")
        draw_face_locations("assets/BarackObama.jpg", face_locations)


if __name__ == '__main__':
    unittest.main()
