import cv2

def video_frame_loader(file_path: str):

    cap = cv2.VideoCapture(file_path)

    if not cap.isOpened():
        print("Error opening video file")
        exit()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Frame", frame)

        # press q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
