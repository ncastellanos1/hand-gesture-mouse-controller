class Smoother:
    """
    Class to smooth the position of the mouse
    """

    def __init__(self, smooth_factor):
        self.smooth_factor = smooth_factor
        self.last_position = (0, 0)

    def smooth(self, current_x, current_y):
        """
        Smooth the position of the mouse
        """
        smoothed_x = self.last_position[1] * (1 - self.smooth_factor) + current_y * self.smooth_factor
        smoothed_y = self.last_position[0] * (1 - self.smooth_factor) + current_x * self.smooth_factor
        self.last_position = (smoothed_x, smoothed_y)
        return smoothed_x, smoothed_y
