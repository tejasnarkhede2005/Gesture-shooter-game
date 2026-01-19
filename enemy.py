import random
import cv2

class Enemy:
    def __init__(self, width):
        self.w = 40
        self.h = 40
        self.x = random.randint(0, width - self.w)
        self.y = -self.h
        self.speed = random.randint(4, 7)
        self.color = (0, 0, 255)
        self.alive = True

    def update(self, height):
        self.y += self.speed
        if self.y > height:
            self.alive = False

    def draw(self, frame):
        cv2.rectangle(frame, (self.x, self.y),
                      (self.x + self.w, self.y + self.h),
                      self.color, -1)

    def rect(self):
        return (self.x, self.y, self.w, self.h)
