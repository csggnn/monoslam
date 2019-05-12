from mobilecapture import MobileCapture
import cv2


def init():
    p_cap = MobileCapture()
    im = p_cap.read()
    cv2.imshow('sample image', im)
    return p_cap


def run(p_cap):
    while True:
        cv2.imshow('sample image', p_cap.read())
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    cap = init()
    run(cap)
