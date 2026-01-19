import cv2

class Player:
    def __init__(self, width, height):
        self.w = 120
        self.h = 20
        self.x = (width - self.w) // 2
        self.y = height - 60

    def move_to(self, center_x, width):
        self.x = int(center_x - self.w // 2)
        self.x = max(0, min(width - self.w, self.x))

    def draw(self, frame):
        cv2.rectangle(frame, (self.x, self.y),
                      (self.x + self.w, self.y + self.h),
                      (200, 200, 200), -1)

    def gun_position(self):
        return self.x + self.w // 2, self.y
