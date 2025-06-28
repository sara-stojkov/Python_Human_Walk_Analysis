import cv2
import mediapipe as mp
import pandas as pd

def save_ankle_positions(video_file:str, positions_save_file:str):

    # initialize mediapipe
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    cap = cv2.VideoCapture(video_file)

    # to store data
    ankle_data = []

    frame_idx = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)

        if results.pose_landmarks:
            left_ankle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
            # store normalized coordinates
            ankle_data.append({
                "frame": frame_idx,
                "x": left_ankle.x,
                "y": left_ankle.y
            })

        frame_idx += 1

        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    # save as CSV
    df = pd.DataFrame(ankle_data)
    df.to_csv(positions_save_file, index=False)
    print("saved", positions_save_file)
