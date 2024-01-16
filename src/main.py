import cv2

from controller import MouseController, MultiMonitorController
from detector import HandDetector, HeadOrientationDetector


def main():
    """
    Main function.
    """
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 260)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
    hand_detector = HandDetector()
    head_orientation_detector = HeadOrientationDetector()

    mouse_controller = MouseController()
    multi_monitor_controller = MultiMonitorController()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        current_head_orientation = head_orientation_detector.get_head_orientation(frame)

        if current_head_orientation != head_orientation_detector.last_head_orientation:
            target_monitor = multi_monitor_controller.determine_target_monitor(current_head_orientation)
            multi_monitor_controller.move_mouse_to_monitor(target_monitor)

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
