import pygame
import grid
from pygame.locals import *
import button
import player

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic-tac-toe')
# define font
font = pygame.font.SysFont(None, 40)
# load button images
x_img = pygame.image.load('Tic-tac-toe/imgs/X.png')
o_img = pygame.image.load('Tic-tac-toe/imgs/O.png')
img_3 = font.render('3x3', True, (0, 0, 0))
img_4 = font.render('4x4', True, (0, 0, 0))
img_5 = font.render('5x5', True, (0, 0, 0))
# create button instances
x_button = button.Button(75, 300, x_img, 1)
o_button = button.Button(325, 300, o_img, 1)
button_3 = button.Button(230, 83, img_3, 1)
button_4 = button.Button(230, 250, img_4, 1)
button_5 = button.Button(230, 415, img_5, 1)
# define variables
bg = (255, 255, 200)
line_width = 5
clicked = True
pos = []
markers = []
# create objects
player = player.Player()
table = grid.Grid(x_img, o_img, player.get_is_x())

# game loop
player_is_choosing = True
player_is_choosing_grid = True
run = True
while run:

    # menu fold choosing 'X' or 'O'
    if player_is_choosing:
        screen.fill(bg)

        pygame.draw.line(screen, (0, 0, 0), (screen_width / 2, 0), (screen_width / 2, screen_height), line_width)
        # pygame.draw.line(screen, (0, 0, 0), (0, screen_height/2), (screen_width, screen_height/2), line_width)

        if x_button.draw(screen):
            player_is_choosing = False
            isX = True
            player.set_is_x(True)

            print("works")
        elif o_button.draw(screen):
            player_is_choosing = False
            isX = False
            player.set_is_x(isX)

            print("works")
    # menu with grid size
    elif player_is_choosing_grid:
        screen.fill(bg)

        if button_3.draw(screen):
            #table = grid.Grid(3, x_img, o_img, player.get_is_x())
            table.set_size(3)
            player_is_choosing_grid = False
        elif button_4.draw(screen):
            #table = grid.Grid(4, x_img, o_img, player.get_is_x())
            table.set_size(4)
            player_is_choosing_grid = False
        elif button_5.draw(screen):
            #table = grid.Grid(5, x_img, o_img, player.get_is_x())
            table.set_size(5)
            player_is_choosing_grid = False
    # tic tac toe game
    else:
        table.draw_grid(screen, screen_width, screen_height, (50, 50, 50), bg, font)
        #table.draw_markers(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                run = False
                print('q')
            if event.key == K_SPACE:
                player_is_choosing = True
                player_is_choosing_grid = True
                table.set_tie(False)
                table.set_game_over(False)
                print('space')

    pygame.display.update()

pygame.quit()
