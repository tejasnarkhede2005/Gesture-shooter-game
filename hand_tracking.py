import cv2
import mediapipe as mp
import math

class HandTracker:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.draw = mp.solutions.drawing_utils
        self.result = None

    def find_hand(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(rgb)

    def get_landmarks(self, frame, draw=True):
        if self.result.multi_hand_landmarks:
            hand = self.result.multi_hand_landmarks[0]
            h, w, _ = frame.shape
            lm = []

            for i, point in enumerate(hand.landmark):
                lm.append((i, int(point.x * w), int(point.y * h)))

            if draw:
                self.draw.draw_landmarks(
                    frame, hand, mp.solutions.hands.HAND_CONNECTIONS
                )
            return lm
        return []

    def pinch(self, lm, threshold=35):
        if not lm:
            return False
        x1, y1 = lm[4][1], lm[4][2]   # thumb tip
        x2, y2 = lm[8][1], lm[8][2]   # index tip
        return math.hypot(x2-x1, y2-y1) < threshold
