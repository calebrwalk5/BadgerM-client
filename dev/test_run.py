import pygame
import os
from pygame.locals import *

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

screen_width=1366
screen_height=768
screen=pygame.display.set_mode((screen_width, screen_height))

def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

font = "mensch.ttf"


clock = pygame.time.Clock()
FPS=60

# Main Menu
def main_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        os.system('echo test')
                        os.system('start ../')
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill(black)
        title=text_format("BadgerM", font, 90, white)
        info=text_format("Use arrow keys to select", font, 20, white)
        if selected=="start":
            text_start=text_format("START", font, 75, yellow)
        else:
            text_start = text_format("START", font, 75, white)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, yellow)
        else:
            text_quit = text_format("QUIT", font, 75, white)

        title_rect=title.get_rect()
        info_rect=info.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(info, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("BadgerM Launcher")

main_menu()
pygame.quit()
quit()
