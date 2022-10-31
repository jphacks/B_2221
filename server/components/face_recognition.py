import face_recognition
import matplotlib.pyplot as plt


class FaceLocation:
    def draw_face_locations(img, face_locations):
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.set_axis_off()
        # 長方形を描画する。
        for i, (top, right, bottom, left) in enumerate(face_locations):
            w, h = right - left, bottom - top
            ax.add_patch(plt.Rectangle(
                (left, top), w, h, ec="r", lw=2, fill=None))
        plt.show()

    def get_face_locations(image_file_path):
        image = face_recognition.load_image_file(image_file_path)
        face_locations = face_recognition.face_locations(image, model="cnn")
        return face_locations
