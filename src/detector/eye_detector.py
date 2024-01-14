import numpy as np

from strategies import DetectorStrategy


class EyeDetector(DetectorStrategy):
    """Concrete strategy for detecting eyes"""

    def __init__(self, cascade):
        self.cascade = cascade

    def detect(self, img):
        """Detect eyes in an image"""
        eyes = self.cascade.detectMultiScale(img, 1.3, 5)
        if len(eyes) == 0:
            return None, None
        width = np.size(img, 1)
        left_eye = None
        right_eye = None
        for (x, y, w, h) in eyes:
            if y > img.shape[0] / 2:
                continue
            eye_center = x + w / 2
            if eye_center < width * 0.5:
                left_eye = img[y:y + h, x:x + w]
            else:
                right_eye = img[y:y + h, x:x + w]
        return left_eye, right_eye
