from pygame import *
import pygame
from random import *
import sys
pygame.init()
finish = True
font.init()
run= True
win_w = 600
win_h = 500
window = display.set_mode((win_w, win_h))
background = (200, 255, 150)
window.fill(background)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def control_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_h - 155:
            self.rect.y += self.speed
               
    def control_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_h - 155:
            self.rect.y += self.speed

fps = 60

text_font = font.Font(None, 60)

game_winner = ""

set_point = 0

set_points_list = [5, 10, 15, 20, 25, 30]
l_playerpoint = 0
r_playerpoint = 0

point_l = text_font.render(str(l_playerpoint), 1, (255, 0, 0))
point_r = text_font.render(str(r_playerpoint), 1, (0, 0, 255))

clock = time.Clock()
winner1 = text_font.render("Player 1 wins", 1, (0, 0, 0))
winner2 = text_font.render("Player 2 wins", 1, (0,0, 0))
ball_x_speed = 5
ball_y_speed = 5

space_checker = False
#create things
player1 = Player("racket.png", 20, win_h/2 - 75, 5, 50, 150)
player2 = Player("racket.png", win_w - 75, win_h/2 - 75, 5, 50, 150)
ball = GameSprite("tenis_ball.png", win_w/2 - 25, win_h/2 - 50, 5, 50, 50)

random_direction = [-1.01, 1.01]

restart = False

point_chosen = False

countdown_time = 3000
countdown_start = 0
countdown_end = 3



count_screen = text_font.render("Play in :", 1, (255, 0, 0))

#pause handler
pause_screen = text_font.render("Press e to continue", 1, (0, 0, 0))
while run == True:   
    for e in event.get():
        if e.type == QUIT:
            run = False
            pygame.quit()

    key_pressed = key.get_pressed()
    if key_pressed[K_SPACE] and restart == False and point_chosen == True:
        finish = True
        window.blit(pause_screen, (win_w/2 - 180, 210))
        # space_checker = True

    elif key_pressed[K_e] and restart == False and point_chosen == True:
        finish = False
        # space_checker = False

    if key_pressed[K_1] or key_pressed[K_2] or key_pressed[K_3] and point_chosen == False:
        if key_pressed[K_1] and point_chosen == False:
            set_point = set_points_list[0]
        if key_pressed[K_2] and point_chosen == False:
            set_point = set_points_list[1]
        if key_pressed[K_3] and point_chosen == False:
            set_point = set_points_list[2]
        if key_pressed[K_4] and point_chosen == False:
            set_point = set_points_list[3]
        if key_pressed[K_5] and point_chosen == False:
            set_point = set_points_list[4]
        if key_pressed[K_6] and point_chosen == False:
            set_point = set_points_list[5]
        

        current_time = time.get_ticks()
        # if current_time - countdown_start <countdown_time:
        #     countdown_number = (3 - ((current_time - countdown_start) // 2 ))
        #     window.blit()

        finish = False
        point_chosen = True


    if finish != True:
        print(current_time)
        window.fill(background)
        player1.control_l()
        player2.control_r()

        ball.rect.x += ball_x_speed
        ball.rect.y += ball_y_speed

        
        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            ball_x_speed*=-1.01
            ball_y_speed*= random_direction[randint(0, 1)]

        if ball.rect.y < 5 or ball.rect.y > win_h - 55:
            ball_y_speed*=-1.01

            ball_x_speed*= 1.01

        if ball.rect.x < 0:
            l_playerpoint += 1
            ball_x_speed = 5
            ball_y_speed = 5

            ball.rect.x = win_w/2 - 25
            ball.rect.y = win_w/2 - 50

            ball_x_speed*=-1
            
            #player 2 wins
        if ball.rect.x > win_w:
            r_playerpoint += 1
            ball_x_speed = 5
            ball_y_speed = 5
            ball.rect.x = win_w/2 - 25
            ball.rect.y = win_w/2 - 50
            ball_x_speed*=-1

        if l_playerpoint == set_point:
            game_winner = "Player 1"
            finish = True
            restart = True
        elif r_playerpoint == set_point:
            game_winner = "Player 2"
            finish = True
            restart = True
        
        if l_playerpoint - set_point == -1 and r_playerpoint - set_point == -1:
            set_point += 1
        point_l = text_font.render(str(l_playerpoint), 1, (255, 0, 0))
        point_r = text_font.render(str(r_playerpoint), 1, (0, 0, 255))
        window.blit(point_r, (win_w/2 - 50, 5))
        window.blit(point_l, (win_w/2 + 40, 5))
        player1.reset()
        player2.reset()
        ball.reset()

    if game_winner != "":
        if game_winner == "Player 1":
            window.blit(winner1, (win_w/2 - 120, win_h/2 - 40))
        elif game_winner == "Player 2":
            window.blit(winner2, (win_w/2 - 120, win_h/2 - 40))
        finish = True
        keys = key.get_pressed()
        if keys[K_r]:
            finish = False
            restart = False
            l_playerpoint = 0
            r_playerpoint = 0
            game_winner = ""


    display.update()
    clock.tick(fps) #times by 2 when you are not sharing ur screen