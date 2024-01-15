import cv2

from controller import MouseController
from detector import HandDetector


def main():
    """
    Main function.
    """
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 260)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
    hand_detector = HandDetector()
    mouse_controller = MouseController()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        results = hand_detector.process_frame(frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if hand_detector.is_index_finger_raised(hand_landmarks.landmark):
                    mouse_controller.move_mouse(hand_landmarks, frame.shape)
                if hand_detector.is_right_click(hand_landmarks.landmark):
                    mouse_controller.click(hand_detector.RIGHT)
                if hand_detector.is_hand_closed(hand_landmarks.landmark):
                    mouse_controller.click(hand_detector.LEFT)

        cv2.imshow('MediaPipe Hands', frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
