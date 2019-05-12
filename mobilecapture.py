import numpy as np
import cv2
import urllib.request

IP_webcam_add = "192.168.150.188"


class MobileCapture:
    def __init__(self, add=IP_webcam_add):
        self.ipweb_add = "http://" + add + ":8080/shot.jpg"
        self.fig_name = ""

    def read(self):
        fr = urllib.request.urlopen(self.ipweb_add)
        fr_np = np.array(bytearray(fr.read()), dtype=np.uint8)
        return cv2.imdecode(fr_np, -1)

    def show_loop(self, figure_name="MobileCapture loop"):
        self.fig_name = figure_name
        while True:
            im = self.read()
            cv2.imshow(self.fig_name, im)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def __del__(self):
        cv2.destroyWindow(self.fig_name)


if __name__ == "__main__":
    cap = MobileCapture()
    cap.show_loop()
