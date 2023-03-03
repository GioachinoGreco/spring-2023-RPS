# A visually interactive Rock, paper, scissors game
# file created by Rivan Dass


# libraries
from time import sleep

from random import randint

import pygame as pg

import os

game_folder = os.path.dirname(__file__)
print(game_folder)


# Capitalize variables to highlight importance
# game settings
WIDTH = 1000
HEIGHT = 800
FPS = 30

# define colors
# tuples are immutable (cannot be changed), lists are not
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# initialize
pg.init()
pg.mixer.init()

# sets the width and height of the screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
# sets the caption of the window to the displayed text
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()
# stores the image
rock_image = pg.image.load(os.path.join(game_folder, 'rock the wock.png')).convert()
# storing the dimensions of the pixels, and allows us to change them
rock_image_rect = rock_image.get_rect()
# paper image
paper_image = pg.image.load(os.path.join(game_folder, 'roll-paper.png')).convert()
paper_image_rect = paper_image.get_rect()
# scissors image
scissors_image = pg.image.load(os.path.join(game_folder, 'scissorshand.png')).convert()
scissors_image_rect = scissors_image.get_rect()


### SEPARATE IMAGES FOR CPU ###
rock_cpu_image = pg.image.load(os.path.join(game_folder, 'rock the wock.png')).convert()
rock_cpu_image_rect = rock_image.get_rect()
paper_cpu_image = pg.image.load(os.path.join(game_folder, 'roll-paper.png')).convert()
paper_cpu_image_rect = paper_image.get_rect()
scissors_cpu_image = pg.image.load(os.path.join(game_folder, 'scissorshand.png')).convert()
scissors_cpu_image_rect = scissors_image.get_rect()

choices0 = ["rock", "paper", "scissors"]

# computer decides what to choose
def cpu_randchoice():
    # global variable that stores the computer's choice
    global cpu_choice
    cpu_choice = choices0[randint(0,2)]
    return cpu_choice

player_choice = ""

running = True

while running:
    # forces the frame rate to 30 frames per second
    clock.tick(FPS)

    for event in pg.event.get():
        # (event) is any time a thing happens, event type here is the x in the corner of the window the program stops
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            # xsubone = pg.mouse.get_pos()[0]
            # ysubone = pg.mouse.get_pos()[1]

            # gets the position of the mouse and stores it
            mouse_coords = pg.mouse.get_pos()

            # if 0<xsubone<my_image_rect.width and 0<ysubone<my_image_rect.height:
            #     print("The rock")
            # else:
            #     print(pg.mouse.get_pos())
            # if the mouse_coords are on the pixels of an image, it prints text
            if rock_image_rect.collidepoint(mouse_coords):
                player_choice = "rock"
                cpu_randchoice()
            elif paper_image_rect.collidepoint(mouse_coords):
                player_choice = "paper"
                cpu_randchoice()
            elif scissors_image_rect.collidepoint(mouse_coords):
                player_choice = "scissors"
                cpu_randchoice()
            else:
                print("not a valid choice")

    ########### INPUT ###########
    # HCI - human computer interaction...

    # set positions

    # rock image position
    rock_image_rect.x = 10
    # scissors image position
    scissors_image_rect.y = 400
    scissors_image_rect.x = 10
    # paper image position
    paper_image_rect.x = 520
    paper_image_rect.y = 250

    # cpu rock image posiiton
    rock_cpu_image_rect


    # update

    ###### draw ######

    # fills the screen with a color
    screen.fill(BLACK)
    # blit = draw a picture
    if player_choice == "":
        screen.blit(rock_image, rock_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(scissors_image, scissors_image_rect)


    if player_choice == "rock":
        screen.blit(rock_image, rock_image_rect)
    if player_choice == "scissors":
        screen.blit(scissors_image, scissors_image_rect)
    if player_choice == "paper":
        screen.blit(paper_image, paper_image_rect)



    pg.display.flip()