import time

import numpy as np
import pyautogui
from screeninfo import get_monitors


class MouseController:
    """
    Controls mouse movement based on hand landmarks.
    """

    def __init__(self):
        monitors = get_monitors()
        self.ancho_total = sum(monitor.width for monitor in monitors)
        self.alto_max = max(monitor.height for monitor in monitors)
        self.last_click_time = 0
        self.click_delay = 0.5  # 500 ms delay between clicks
        self.smooth_factor = 0.5
        self.last_mouse_pos = (0, 0)

    def move_mouse(self, hand_landmarks, frame_shape):
        """Move mouse based on hand landmarks"""
        x, y = int(hand_landmarks.landmark[8].x * frame_shape[1]), int(hand_landmarks.landmark[8].y * frame_shape[0])
        x_scaled = np.interp(x, [0, frame_shape[1]], [0, self.ancho_total])
        y_scaled = np.interp(y, [0, frame_shape[0]], [0, self.alto_max])

        smoothed_x = self.last_mouse_pos[0] * (1 - self.smooth_factor) + x_scaled * self.smooth_factor
        smoothed_y = self.last_mouse_pos[1] * (1 - self.smooth_factor) + y_scaled * self.smooth_factor

        pyautogui.moveTo(smoothed_x, smoothed_y)
        self.last_mouse_pos = (smoothed_x, smoothed_y)

    def click(self, direction):
        """Click"""
        current_time = time.time()
        if current_time - self.last_click_time > self.click_delay:
            pyautogui.click(button=direction)
            self.last_click_time = current_time

