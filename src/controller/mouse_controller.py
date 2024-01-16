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
        self.last_hand_landmarks = None

    def move_mouse(self, hand_landmarks, frame_shape):
        """Move mouse based on hand landmarks, inverting horizontal movement and incorporating hand speed."""
        current_x, current_y = int(hand_landmarks.landmark[8].y * frame_shape[0]), int(hand_landmarks.landmark[8].x * frame_shape[1])

        if self.last_hand_landmarks:
            last_x, last_y = int(self.last_hand_landmarks.landmark[8].y * frame_shape[0]), int(self.last_hand_landmarks.landmark[8].x * frame_shape[1])
            velocity_x = current_x - last_x
            velocity_y = current_y - last_y
        else:
            velocity_x, velocity_y = 0, 0

        x_scaled = np.interp(current_x + velocity_x, [0, frame_shape[0]], [0, self.alto_max])
        y_scaled = np.interp(current_y + velocity_y, [0, frame_shape[1]], [self.ancho_total, 0])

        smoothed_x = self.last_mouse_pos[1] * (1 - self.smooth_factor) + y_scaled * self.smooth_factor
        smoothed_y = self.last_mouse_pos[0] * (1 - self.smooth_factor) + x_scaled * self.smooth_factor

        pyautogui.moveTo(smoothed_x, smoothed_y)
        self.last_mouse_pos = (smoothed_y, smoothed_x)
        self.last_hand_landmarks = hand_landmarks

    def click(self, direction):
        """Click"""
        current_time = time.time()
        if current_time - self.last_click_time > self.click_delay:
            pyautogui.click(button=direction)
            self.last_click_time = current_time

