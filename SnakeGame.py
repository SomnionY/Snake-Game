# Snake Game!

# Imports
import pygame
import sys          #Exit function
import random
import time

# Colors
red = pygame.Color(255, 0, 0)  # game over
green = pygame.Color(0, 255, 0) # snake
black = pygame.Color(0, 0, 0)   # score
white =pygame.Color(255, 255, 255)  # score
brown = pygame.Color(165, 42, 42)   #food

# Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# food
food_pos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
food_spawn = True

# Direction
direction = 'RIGHT'
changet = direction


# FPS controller
fps_controller = pygame.time.Clock()

# Chec for initializing eroors
check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...". format(check_errors))
    sys.exit(-1)
else:
    print("(+) Pygame succesfully initialized!")

# Set display
set_display = pygame.display.set_mode((720, 460))

# Game name
pygame.display.set_caption("Snake Game")

score = 0

# Game over function
def GameOver():
    MyFont = pygame.font.SysFont('monaco', 72)
    GOSurface = MyFont.render('Game over!', True, red)
    GOSRect = GOSurface.get_rect()
    GOSRect.midtop = (360, 15)
    set_display.blit(GOSurface, GOSRect)
    pygame.display.flip()
    ShowScore(0)
    time.sleep(1)
    pygame.quit()   # For pygame window
    sys.exit()  # For console

# Score function
def ShowScore(c = 1):
    SFont = pygame.font.SysFont('monaco', 24)
    SSurface = SFont.render('Score : {0}'. format(score), True, black)
    SRect = SSurface.get_rect()
    if c == 1:
        SRect.midtop = (80, 10)
    else:
        SRect.midtop = (360, 120)
    set_display.blit(SSurface, SRect)


# Main logic of the Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changet = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changet = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changet = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changet = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Validation of direction
    if changet == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changet == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changet == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changet == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Update snake position [x,y]
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10


    # Snake body mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    #Food Spawn
    if food_spawn == False:
        food_pos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    food_spawn = True

    #Background
    set_display.fill(white)

    #Draw snake
    for pos in snake_body:
        pygame.draw.rect(set_display, green, pygame.Rect(pos[0], pos[1], 10, 10))

    #Draw food
    pygame.draw.rect(set_display, brown, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    #Screen borders
    if snake_pos[0] > 710 or snake_pos[0] < 0:
        GameOver()
    if snake_pos[1] > 450 or snake_pos[1] < 0:
        GameOver()


    for block in snake_body[1:]:
        if block[0] == snake_pos[0] and block[1] == snake_pos[1]:
            GameOver()


    ShowScore()
    pygame.display.flip()
    fps_controller.tick(16)
