import unittest

from utils import VelocityCalculator


class TestVelocityCalculator(unittest.TestCase):

    def test_velocity_with_no_last_position(self):
        current = (10, 20)
        last = None
        velocity = VelocityCalculator.calculate_velocity(current, last)
        self.assertEqual(velocity, (0, 0))

    def test_velocity_with_last_position(self):
        current = (15, 25)
        last = (10, 20)
        velocity = VelocityCalculator.calculate_velocity(current, last)
        expected_velocity = (current[0] - last[0], current[1] - last[1])
        self.assertEqual(velocity, expected_velocity)