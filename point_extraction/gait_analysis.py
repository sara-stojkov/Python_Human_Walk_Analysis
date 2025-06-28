import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def analyze_gait(positions_path:str):
    # load saved positions
    df = pd.read_csv(positions_path)

    # get just x-coordinate over time
    x_pos = df['x']

    # plot raw
    plt.figure()
    plt.plot(x_pos)
    plt.title("Left ankle X over time")
    plt.show()

    # find peaks - these are roughly the farthest left or right positions
    peaks, _ = find_peaks(-x_pos, distance=10)  # negative to find valleys
    print(f"Detected {len(peaks)} steps")

    # plot with peaks
    plt.figure()
    plt.plot(x_pos, label="ankle x")
    plt.plot(peaks, x_pos[peaks], "rx", label="detected steps")
    plt.title("Gait cycle analysis")
    plt.legend()
    plt.show()

    # estimate average step period
    if len(peaks) > 1:
        avg_step_frames = pd.Series(peaks).diff().mean()
        print(f"Average step period: {avg_step_frames:.2f} frames")
