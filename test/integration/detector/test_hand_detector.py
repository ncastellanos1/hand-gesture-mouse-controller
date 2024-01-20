import unittest
import cv2

from detector import HandDetector


class TestHandDetectorIntegration(unittest.TestCase):
    """Integration tests for the HandDetector class."""

    @classmethod
    def setUpClass(cls):
        """
        Set up the HandDetector class for the tests.
        """
        cls.hand_detector = HandDetector()

    def process_image(self, image_path):
        """Helper method to process an image through the HandDetector."""
        frame = cv2.imread(image_path)
        self.assertIsNotNone(frame, f"Test image {image_path} not found")
        return self.hand_detector.process_frame(frame)

    def test_process_frame_with_index_finger_raised(self):
        """Test processing a frame with the index finger raised."""
        results = self.process_image("./../../resources/hand_index_finger_raised.png")
        self.assertIsNotNone(results, "No results returned from process_frame")
        self.assertTrue(self.hand_detector.is_index_finger_raised(results.multi_hand_landmarks[0].landmark))

    def test_process_frame_with_hand_closed(self):
        """Test processing a frame with a closed hand."""
        results = self.process_image("./../../resources/hand_closed.png")
        self.assertIsNotNone(results, "No results returned from process_frame")
        self.assertTrue(self.hand_detector.is_hand_closed(results.multi_hand_landmarks[0].landmark))
