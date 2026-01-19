import cv2
import numpy as np
import random

WIDTH, HEIGHT = 960, 540

def run_demo(frame_placeholder, slider_x):
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    frame[:] = (20, 20, 40)

    # player
    px = int(slider_x * WIDTH)
    cv2.rectangle(frame, (px-60, HEIGHT-60), (px+60, HEIGHT-40), (200,200,200), -1)

    # fake enemy
    ex = random.randint(50, WIDTH-50)
    ey = random.randint(50, HEIGHT-200)
    cv2.rectangle(frame, (ex, ey), (ex+40, ey+40), (0,0,255), -1)

    frame_placeholder.image(frame, channels="BGR")
