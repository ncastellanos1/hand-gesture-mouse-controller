from strategies import DetectorStrategy


class FaceDetector(DetectorStrategy):
    """Concrete strategy for detecting faces"""

    def __init__(self, cascade):
        self.cascade = cascade

    def detect(self, img):
        """Detect faces in an image"""
        cords = self.cascade.detectMultiScale(img, 1.3, 5)
        if len(cords) == 0:
            return None
        biggest = max(cords, key=lambda rect: rect[3])
        x, y, w, h = biggest
        return img[y:y + h, x:x + w]
