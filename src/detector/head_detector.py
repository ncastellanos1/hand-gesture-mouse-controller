import cv2
import mediapipe as mp


class HeadOrientationDetector:
    """
    Detects the head orientation using MediaPipe and computes the landmarks.
    """

    ORIENTATION_UNKNOWN = "unknown"
    ORIENTATION_FRONT = "front"
    ORIENTATION_LEFT = "left"
    ORIENTATION_RIGHT = "right"

    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh()
        self.last_head_orientation = None

    def get_head_orientation(self, frame):
        """
        Returns the head orientation based on the frame and updates the last head orientation.
        """
        current_orientation = self._calculate_head_orientation(frame)
        if current_orientation != self.last_head_orientation:
            self.last_head_orientation = current_orientation
        return current_orientation

    def _calculate_head_orientation(self, frame):
        """
        Returns the head orientation based on the frame.
        """
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(frame_rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Use direct indices for landmarks
                nose_tip = face_landmarks.landmark[4]  # Index for nose tip
                left_eye_outer = face_landmarks.landmark[130]  # Index for left eye outer corner
                right_eye_outer = face_landmarks.landmark[359]  # Index for right eye outer corner

                # Simple example to determine orientation
                if nose_tip.x < left_eye_outer.x:
                    return self.ORIENTATION_LEFT
                elif nose_tip.x > right_eye_outer.x:
                    return self.ORIENTATION_RIGHT
                else:
                    return self.ORIENTATION_FRONT

        return self.ORIENTATION_UNKNOWN
