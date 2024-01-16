import pyautogui
from screeninfo import get_monitors

from detector import HeadOrientationDetector


class MultiMonitorController:
    """
    Controls mouse movement based on head orientation.
    """

    PRIMARY_MONITOR = 0
    SECONDARY_MONITOR = 1

    def __init__(self):
        self.monitors = get_monitors()

    def determine_target_monitor(self, head_orientation):
        """
        Determine to which monitor the user is likely looking based on head orientation.
        """
        if head_orientation == HeadOrientationDetector.ORIENTATION_RIGHT and len(self.monitors) > 1:
            return self.SECONDARY_MONITOR
        else:
            return self.PRIMARY_MONITOR

    def move_mouse_to_monitor(self, monitor_index):
        """
        Move the mouse to the target monitor.
        """
        if monitor_index < len(self.monitors):
            target_monitor = self.monitors[monitor_index]
            center_x = target_monitor.x + target_monitor.width // 2
            center_y = target_monitor.y + target_monitor.height // 2
            pyautogui.moveTo(center_x, center_y)
