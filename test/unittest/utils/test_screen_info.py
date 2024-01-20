import unittest
from unittest.mock import patch, Mock

import numpy as np

from utils import ScreenInfo


class TestScreenInfo(unittest.TestCase):

    @patch('screeninfo.get_monitors')
    def setUp(self, mock_get_monitors):
        """
        Set up the ScreenInfo for testing.
        """
        mock_monitors = [Mock(width=1920, height=1080), Mock(width=1280, height=720)]
        mock_get_monitors.return_value = mock_monitors

        self.screen_info = ScreenInfo()

    def test_init(self):
        self.assertEqual(self.screen_info.total_width, 3712)
        self.assertEqual(self.screen_info.max_height, 1120)

    def test_scale_coordinates(self):
        frame_shape = (640, 480)
        x, y = 320, 240  # Center of the frame
        x_scaled, y_scaled = self.screen_info.scale_coordinates(x, y, frame_shape)

        # Expected scaled values
        expected_x_scaled = np.interp(x, [0, frame_shape[0]], [0, self.screen_info.max_height])
        expected_y_scaled = np.interp(y, [0, frame_shape[1]], [self.screen_info.total_width, 0])

        self.assertAlmostEqual(x_scaled, expected_x_scaled)
        self.assertAlmostEqual(y_scaled, expected_y_scaled)
