import mediapipe as mp
import cv2


class HandDetector:
    """
    Detects hands using MediaPipe and computes the landmarks.
    """

    LEFT = 'left'
    RIGHT = 'right'

    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()

    def process_frame(self, frame):
        """Process a frame and return the hand landmarks"""
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(frame_rgb)

    @staticmethod
    def is_index_finger_raised(landmarks):
        """
        Determines if only the index finger is raised.

        Args:
            landmarks (list): A list of landmarks detected on the hand.

        Returns:
            bool: True if only the index finger is raised, False otherwise.
        """
        fingertip_ids = [4, 8, 12, 16, 20]
        raised_fingers = 0
        for i, tip_id in enumerate(fingertip_ids):
            # Compare the Y position of the fingertip to the middle finger's base
            if landmarks[tip_id].y < landmarks[9].y:
                raised_fingers += 1

        # Only the index finger is considered raised if it's the only finger raised
        return raised_fingers == 1 and landmarks[8].y < landmarks[6].y

    @staticmethod
    def is_hand_closed(landmarks):
        """
        Determines if the hand is closed.

        Args:
            landmarks (list): A list of landmarks detected on the hand.

        Returns:
            bool: True if the majority of the fingers (3 or more) are bent, indicating a closed hand.
        """
        fingertip_ids = [8, 12, 16, 20]  # Reference points for the fingertips (index, middle, ring, little finger)
        base_ids = [5, 9, 13, 17]  # Reference points for the base of the fingers

        bent_fingers = 0
        for fingertip_id, base_id in zip(fingertip_ids, base_ids):
            # Compare the Y position (height) of the fingertip with the base of the finger
            if landmarks[fingertip_id].y > landmarks[base_id].y:
                bent_fingers += 1

        # Consider the hand as closed if the majority of the fingers (here, 3 or more) are bent
        return bent_fingers >= 4
