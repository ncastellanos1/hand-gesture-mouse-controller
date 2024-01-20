import numpy as np
from screeninfo import get_monitors


class ScreenInfo:
    """
    Class to get information about the screen
    """

    def __init__(self):
        monitors = get_monitors()
        self.total_width = sum(monitor.width for monitor in monitors)
        self.max_height = max(monitor.height for monitor in monitors)

    def scale_coordinates(self, x, y, frame_shape):
        """
        Scale coordinates from the frame to the screen.
        """
        x_scaled = np.interp(x, [0, frame_shape[0]], [0, self.max_height])
        y_scaled = np.interp(y, [0, frame_shape[1]], [self.total_width, 0])
        return x_scaled, y_scaled
