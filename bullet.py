import cv2

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 6
        self.speed = 14
        self.active = True

    def update(self):
        self.y -= self.speed
        if self.y < 0:
            self.active = False

    def draw(self, frame):
        cv2.circle(frame, (self.x, self.y), self.r, (0, 255, 255), -1)

    def rect(self):
        return (self.x - self.r, self.y - self.r, self.r*2, self.r*2)
