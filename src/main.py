import cv2

from src.detector.eye_detector import EyeDetector
from src.detector.face_detector import FaceDetector
from utils.cascade_loader import load_cascade

# Initialize classifiers
face_cascade = load_cascade('resources/xml/haarcascade_frontalface_default.xml')
eye_cascade = load_cascade('resources/xml/haarcascade_eye.xml')

# Detector parameters
detector_params = cv2.SimpleBlobDetector.Params()
detector_params.filterByArea = True
detector_params.maxArea = 1500
detector = cv2.SimpleBlobDetector.create(detector_params)


def cut_eyebrows(img):
    """Cut the eyebrows from an image (assumes that the image contains an eye)"""
    height, width = img.shape[:2]
    eyebrow_h = int(height / 4)
    return img[eyebrow_h:height, 0:width]


def blob_process(img, threshold, detector2):
    """Process an image using the blob detector"""
    _, img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    img = cv2.erode(img, None, iterations=2)
    img = cv2.dilate(img, None, iterations=4)
    img = cv2.medianBlur(img, 5)
    key_points = detector2.detect(img)
    return key_points


def main():
    """Main function"""
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('image')
    cv2.createTrackbar('threshold', 'image', 0, 255, lambda x: x)
    face_detector = FaceDetector(face_cascade)
    eye_detector = EyeDetector(eye_cascade)
    while True:
        _, frame = cap.read()
        face_frame = face_detector.detect(frame)
        if face_frame is not None:
            eyes = eye_detector.detect(face_frame)
            for eye in eyes:
                if eye is not None:
                    threshold = cv2.getTrackbarPos('threshold', 'image')
                    eye = cut_eyebrows(eye)
                    key_points = blob_process(eye, threshold, detector)
                    eye = cv2.drawKeypoints(eye, key_points, eye, (0, 0, 255),
                                            cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    """"""
    main()
