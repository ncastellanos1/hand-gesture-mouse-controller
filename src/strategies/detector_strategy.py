from abc import ABC, abstractmethod


class DetectorStrategy(ABC):
    """Abstract class for detector strategies"""

    @abstractmethod
    def detect(self, img):
        """Detect faces in an image"""
        pass
