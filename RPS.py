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

def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

choices0 = ["rock", "paper", "scissors"]

# computer decides what to choose
def cpu_randchoice():
    # global variable that stores the computer's choice
    choice = choices0[randint(0,2)]
    print("computer decides... " + choice)
    return choice

player_choice = ""

running = True

start_screen = True


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
                start_screen = False
                print("GAME STARTED")
                cpu_randchoice()
                cpu_choice = cpu_randchoice()
            elif paper_image_rect.collidepoint(mouse_coords):
                player_choice = "paper"
                start_screen = False
                print("GAME STARTED")
                cpu_randchoice()
                cpu_choice = cpu_randchoice()
            elif scissors_image_rect.collidepoint(mouse_coords):
                player_choice = "scissors"
                start_screen = False
                print("GAME STARTED")
                cpu_randchoice()
                cpu_choice = cpu_randchoice()
            else:
                print("not a valid choice")

    ########### INPUT ###########
    # HCI - human computer interaction...

    ###### draw ######

    # fills the screen with a color
    screen.fill(BLACK)
    
    # blit = draw picture
    screen.blit(rock_image, rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)

    # start screen before the game starts
    if start_screen:
        draw_text("click one of the options to play rock paper scissors", 22, WHITE, 700, HEIGHT/10)

        # set positions
        # rock image position
        rock_image_rect.x = 10
        rock_image_rect.y = 10
        # scissors image position
        scissors_image_rect.y = 400
        scissors_image_rect.x = 10
        # paper image position
        paper_image_rect.x = 520
        paper_image_rect.y = 400

    
    # this is what happens when the mouse is clicked
    if start_screen == False:
        # cpu images position
        rock_cpu_image_rect.x = 520
        rock_cpu_image_rect.y = 10

        paper_cpu_image_rect.x = 520
        paper_cpu_image_rect.y = 10

        scissors_cpu_image_rect.x = 520
        scissors_cpu_image_rect.y = 10
        if player_choice == "":
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, paper_image_rect)
            screen.blit(scissors_image, scissors_image_rect)
            

# checks to see who won
    if player_choice == "rock":
        if cpu_choice == "rock":
            rock_cpu_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(rock_image, rock_cpu_image_rect)
            print("you tied")
            sleep(3)
            break
            
        if cpu_choice == "paper":
            paper_cpu_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, paper_cpu_image_rect)
            print("You lost!")
            sleep(3)
            break
            
        if cpu_choice == "scissors":
            scissors_cpu_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, scissors_cpu_image_rect)
            print("you won!")
            sleep(3)
            break

    if player_choice == "paper":
        if cpu_choice == "rock":
            rock_cpu_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(rock_image, rock_cpu_image_rect)
            print("you won!")
            sleep(3)
            break
            
        if cpu_choice == "paper":
            paper_cpu_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(paper_image, paper_cpu_image_rect)
            print("You tied")
            sleep(3)
            break
            
        if cpu_choice == "scissors":
            scissors_cpu_image_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(scissors_image, scissors_cpu_image_rect)
            print("you lost!")
            sleep(3)
            break

    if player_choice == "scissors":
        if cpu_choice == "rock":
            rock_cpu_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(rock_image, rock_cpu_image_rect)
            print("you lost")
            sleep(3)
            break
            
        if cpu_choice == "paper":
            paper_cpu_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(paper_image, paper_cpu_image_rect)
            print("You Won!")
            sleep(3)
            break
            
        if cpu_choice == "scissors":
            scissors_cpu_image_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(scissors_image, scissors_cpu_image_rect)
            print("you lost!")
            sleep(3)
            break

    



    pg.display.flip()
