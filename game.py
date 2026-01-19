import cv2
import time
from hand_tracking import HandTracker
from player import Player
from enemy import Enemy
from bullet import Bullet
from utils import rect_collision

def run_game(frame_placeholder):
    WIDTH, HEIGHT = 960, 540
    cap = cv2.VideoCapture(0)

    tracker = HandTracker()
    player = Player(WIDTH, HEIGHT)

    bullets = []
    enemies = []
    score = 0
    last_shot = 0
    spawn_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (WIDTH, HEIGHT))

        tracker.find_hand(frame)
        lm = tracker.get_landmarks(frame)

        hand_x = None
        pinch = False

        if lm:
            hand_x = lm[8][1]
            pinch = tracker.pinch(lm)

        if hand_x:
            player.move_to(hand_x, WIDTH)

        if pinch and time.time() - last_shot > 0.5:
            bx, by = player.gun_position()
            bullets.append(Bullet(bx, by))
            last_shot = time.time()

        if time.time() - spawn_time > 1:
            enemies.append(Enemy(WIDTH))
            spawn_time = time.time()

        for b in bullets[:]:
            b.update()
            if not b.active:
                bullets.remove(b)

        for e in enemies[:]:
            e.update(HEIGHT)
            if not e.alive:
                enemies.remove(e)

        for b in bullets[:]:
            for e in enemies[:]:
                if rect_collision(b.rect(), e.rect()):
                    bullets.remove(b)
                    enemies.remove(e)
                    score += 10
                    break

        for e in enemies:
            e.draw(frame)

        for b in bullets:
            b.draw(frame)

        player.draw(frame)

        cv2.putText(frame, f"Score: {score}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        frame_placeholder.image(frame, channels="BGR")

    cap.release()
