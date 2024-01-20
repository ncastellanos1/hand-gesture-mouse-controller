from unittest.mock import Mock, patch

from controller import MouseController
import unittest


class MockLandmark:
    """
    Mock class for a landmark.
    """
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z


class TestMouseControllerIntegration(unittest.TestCase):

    def setUp(self):
        """Set up the MouseController class for the tests."""
        self.mouse_controller = MouseController()
        self.frame_shape = (640, 480)  # Example frame shape

        # Create mock landmarks
        mock_landmarks = [MockLandmark(0.5, 0.5) for _ in range(21)]  # Assuming 21 landmarks
        self.hand_landmarks = Mock()
        self.hand_landmarks.landmark = mock_landmarks

    @patch('pyautogui.moveTo')
    def test_move_mouse(self, mock_moveTo):
        # Example hand landmarks
        self.hand_landmarks.landmark[8].y = 0.5
        self.hand_landmarks.landmark[8].x = 0.5

        self.mouse_controller.move_mouse(self.hand_landmarks, self.frame_shape)

        # Assert pyautogui.moveTo is called with expected coordinates
        # The actual values will depend on the implementation details of your methods
        mock_moveTo.assert_called_with(1856.0, 560.0)

    @patch('pyautogui.click')
    def test_click(self, mock_click):
        # Simulate a click
        self.mouse_controller.click("left")

        # Assert pyautogui.click is called
        mock_click.assert_called_with(button="left")
