import unittest

from utils import Smoother


class TestSmoother(unittest.TestCase):

    def test_initialization(self):
        smooth_factor = 0.5
        smoother = Smoother(smooth_factor)
        self.assertEqual(smoother.smooth_factor, smooth_factor)
        self.assertEqual(smoother.last_position, (0, 0))

    def test_smooth(self):
        smooth_factor = 0.5
        smoother = Smoother(smooth_factor)
        current_x, current_y = 10, 20

        # First call to smooth
        smoothed_x, smoothed_y = smoother.smooth(current_x, current_y)
        expected_smoothed_x = 0 * (1 - smooth_factor) + current_y * smooth_factor  # Last Y (0) and current Y (20)
        expected_smoothed_y = 0 * (1 - smooth_factor) + current_x * smooth_factor  # Last X (0) and current X (10)
        self.assertAlmostEqual(smoothed_x, expected_smoothed_x)
        self.assertAlmostEqual(smoothed_y, expected_smoothed_y)

        # Prepare for second call
        last_smoothed_x, last_smoothed_y = smoothed_x, smoothed_y

        # Second call to smooth with different values
        current_x, current_y = 30, 40
        smoothed_x, smoothed_y = smoother.smooth(current_x, current_y)
        expected_smoothed_x = last_smoothed_y * (
                    1 - smooth_factor) + current_y * smooth_factor  # Last smoothed Y and current Y
        expected_smoothed_y = last_smoothed_x * (
                    1 - smooth_factor) + current_x * smooth_factor  # Last smoothed X and current X
        self.assertAlmostEqual(smoothed_x, expected_smoothed_x)
        self.assertAlmostEqual(smoothed_y, expected_smoothed_y)


