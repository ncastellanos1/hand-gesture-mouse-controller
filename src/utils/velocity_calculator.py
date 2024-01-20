
class VelocityCalculator:
    """
    Class to calculate the velocity of a point
    """

    @staticmethod
    def calculate_velocity(current, last):
        """Calculate the velocity of a point"""
        if last:
            return current[0] - last[0], current[1] - last[1]
        return 0, 0

