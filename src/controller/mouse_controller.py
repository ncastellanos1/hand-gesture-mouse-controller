import time

import pyautogui

from utils import ScreenInfo, Smoother


class MouseController:
    """
    Controls mouse movement based on hand landmarks.
    """

    def __init__(self):
        self.screen_info = ScreenInfo()
        self.smoother = Smoother(smooth_factor=1.0)
        self.last_click_time = 0
        self.click_delay = 0.5
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

        x_scaled, y_scaled = self.screen_info.scale_coordinates(
            current_x + velocity_x, current_y + velocity_y, frame_shape)

        smoothed_x, smoothed_y = self.smoother.smooth(x_scaled, y_scaled)
        pyautogui.moveTo(smoothed_x, smoothed_y)
        self.last_hand_landmarks = hand_landmarks

    def click(self, direction):
        """Click"""
        current_time = time.time()
        if current_time - self.last_click_time > self.click_delay:
            pyautogui.click(button=direction)
            self.last_click_time = current_time

