import unittest
from unittest.mock import patch, MagicMock

from controller import MouseController


class TestMouseController(unittest.TestCase):

    def setUp(self):
        """
        Set up test
        """
        self.mouse_controller = MouseController()
        self.hand_landmarks = MagicMock()
        self.frame_shape = (1920, 1080)

    @patch('pyautogui.moveTo')
    def test_move_mouse(self, mock_moveTo):
        self.mouse_controller.move_mouse(self.hand_landmarks, self.frame_shape)
        mock_moveTo.assert_called_once()

    @patch('pyautogui.click')
    @patch('time.time')
    def test_click(self, mock_time, mock_click):
        mock_time.return_value = 1000
        self.mouse_controller.last_click_time = 995
        self.mouse_controller.click(direction='left')
        mock_click.assert_called_once_with(button='left')

