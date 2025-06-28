from const import FILE_PATH, POSITIONS_PATH
from video_load.loader import video_frame_loader
from point_extraction.pose_detection import keypoints_detection
from point_extraction.coordinates_saving import save_ankle_positions
from point_extraction.gait_analysis import analyze_gait

# video_frame_loader(FILE_PATH)
# keypoints_detection(FILE_PATH)
save_ankle_positions(FILE_PATH, POSITIONS_PATH)
analyze_gait(POSITIONS_PATH)

