# Mapeli for flappy bird, written in python
# Mapeli is a 'ghost of a game'. Give it a new life.

import pygame, time

pygame.display.init()
pygame.font.init()
pygame.mixer.init()

font = pygame.font.Font(None, 32)
sound = pygame.mixer.Sound("./164680__adam-n__flap-of-material-1.wav")

screen = pygame.display.set_mode((320, 240))
running = True
pygame.display.set_caption("flappy mapeli")
frame_id = 1

next_frame = time.time()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.KEYDOWN:
            sound.play()

    now = time.time()
    step = 1.0/60
    if next_frame + step*10 < now:
        next_frame = now
    while next_frame + step < now:
        frame_id += 1
        next_frame += step

    screen.fill((40, 40, 100))

    flap = False
    if frame_id % 20 < 10:
        flap = True
    screen.fill((128, 128, 128), (20, 50, 10, 10))
    screen.fill((255, 128, 128), (25, 55-flap*10, 5, 10))

    for x, high, low in [(100, 100, 140), (270, 50, 90)]:
        screen.fill((128, 200, 128), (x, 0, 30, high))
        screen.fill((128, 200, 128), (x, low, 30, 240-low))

    text = font.render("{}".format(frame_id), True, (255, 255, 255))
    screen.blit(text, (320/2 - text.get_width()/2, 0))

    pygame.display.flip()
