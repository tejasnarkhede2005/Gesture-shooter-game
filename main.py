import cv2
import time
from hand_tracking import HandTracker
from player import Player
from enemy import Enemy
from bullet import Bullet
from utils import rect_collision

WIDTH, HEIGHT = 1280, 720

cap = cv2.VideoCapture(0)
cap.set(3, WIDTH)
cap.set(4, HEIGHT)

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
    tracker.find_hand(frame)
    lm = tracker.get_landmarks(frame)

    hand_x = None
    pinch = False

    if lm:
        hand_x = lm[8][1]
        pinch = tracker.pinch(lm)

    if hand_x:
        player.move_to(hand_x, WIDTH)

    # shoot
    if pinch and time.time() - last_shot > 0.4:
        bx, by = player.gun_position()
        bullets.append(Bullet(bx, by))
        last_shot = time.time()

    # spawn enemies
    if time.time() - spawn_time > 1:
        enemies.append(Enemy(WIDTH))
        spawn_time = time.time()

    # update bullets
    for b in bullets[:]:
        b.update()
        b.draw(frame)
        if not b.active:
            bullets.remove(b)

    # update enemies
    for e in enemies[:]:
        e.update(HEIGHT)
        e.draw(frame)
        if not e.alive:
            enemies.remove(e)

    # collisions
    for b in bullets[:]:
        for e in enemies[:]:
            if rect_collision(b.rect(), e.rect()):
                bullets.remove(b)
                enemies.remove(e)
                score += 10
                break

    player.draw(frame)

    cv2.putText(frame, f"Score: {score}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("Gesture Shooter Game", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
