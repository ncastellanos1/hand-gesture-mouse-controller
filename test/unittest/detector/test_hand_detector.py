import unittest
from unittest.mock import patch, MagicMock

import cv2

from detector import HandDetector

# Constants for landmark indices
INDEX_FINGERTIP = 8
MIDDLE_FINGER_BASE = 6
MIDDLE_FINGER_LOWER_JOINT = 9


class MockLandmark:
    """
    Mock class for a landmark.
    """

    def __init__(self, y):
        self.y = y


def create_mock_landmarks(landmark_states):
    """
    Create a mock list of landmarks.
    :param landmark_states: A dictionary with key as landmark index and value as y-coordinate.
    """
    landmarks = [MockLandmark(y=3) for _ in range(21)]  # Default state
    for index, y in landmark_states.items():
        landmarks[index] = MockLandmark(y=y)
    return landmarks


class TestHandDetector(unittest.TestCase):

    def setUp(self):
        """
        Set up the HandDetector for testing.
        """
        self.detector = HandDetector()

    @patch('cv2.cvtColor')
    def test_process_frame(self, mock_cvt_color):
        frame = MagicMock()
        mock_cvt_color.return_value = frame

        self.detector.hands.process = MagicMock(return_value='mocked_result')

        result = self.detector.process_frame(frame)

        mock_cvt_color.assert_called_once_with(frame, cv2.COLOR_BGR2RGB)
        self.detector.hands.process.assert_called_once_with(frame)
        self.assertEqual(result, 'mocked_result')

    def test_index_finger_raised(self):
        landmarks = create_mock_landmarks({INDEX_FINGERTIP: 1})
        self.assertTrue(self.detector.is_index_finger_raised(landmarks))

    def test_index_finger_not_raised(self):
        landmarks = create_mock_landmarks({})
        self.assertFalse(self.detector.is_index_finger_raised(landmarks))

    def test_hand_closed(self):
        landmarks = create_mock_landmarks({
            INDEX_FINGERTIP: 100,
            MIDDLE_FINGER_BASE: 101,
            MIDDLE_FINGER_LOWER_JOINT: 102,
        })
        self.assertFalse(self.detector.is_hand_closed(landmarks))

    def test_hand_open(self):
        landmarks = create_mock_landmarks({})
        self.assertFalse(self.detector.is_hand_closed(landmarks))
