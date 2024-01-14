class ImageProcessor:
    """Image processor"""

    def __init__(self, face_detector, eye_detector):
        self.face_detector = face_detector
        self.eye_detector = eye_detector

    def process(self, img):
        """Process an image"""
        face = self.face_detector.detect(img)
        eyes = self.eye_detector.detect(face)
        return face, eyes
