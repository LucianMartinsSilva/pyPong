import pygame
import random
import sys


def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        ball_restart()

    if ball.right >= screen_width:
        opponent_score += 1
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    if opponent.centery < ball.top:
        opponent.centery += opponent_speed
    if opponent.centery > ball.bottom:
        opponent.centery -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

ball_speed_x = 7.7 * random.choice((1, -1))
ball_speed_y = 7.7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7.15
player_move = 4.5

# Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)


while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += player_move
            if event.key == pygame.K_UP:
                player_speed -= player_move

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= player_move
            if event.key == pygame.K_UP:
                player_speed += player_move

    ball_animation()
    player_animation()
    opponent_ai()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    player_text = game_font.render(f"{player_score}", True, light_grey)
    screen.blit(player_text, (660, 470))

    opponent_text = game_font.render(f"{opponent_score}", True, light_grey)
    screen.blit(opponent_text, (600, 470))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
