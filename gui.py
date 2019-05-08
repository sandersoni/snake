import logging
import sys
import pygcurse
import pygame
from pygame.locals import *
from game import Game
import coloredlogs

LOGGER = logging.getLogger(__name__)

WINWIDTH = 10
WINHEIGHT = 10

FPS = 40


def main():
    log_fmt = "%(asctime)s %(name)s[%(lineno)d] %(levelname)s %(message)s"
    coloredlogs.install( level = logging.DEBUG,fmt=log_fmt)
    win = pygcurse.PygcurseWindow(WINWIDTH, WINHEIGHT+4, fullscreen=False)
    pygame.display.set_caption('Window Title')
    win.autoupdate = False
    clock = pygame.time.Clock()

    game = Game(WINWIDTH,WINHEIGHT)

    while True:
        win.fill(bgcolor='blue')
        handle_events(game)
        game.draw(win)
        win.update()
        clock.tick(FPS)

def handle_events(game):
    for event in pygame.event.get():
        LOGGER.log(5, 'event: {0}'.format(event))
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            terminate()
        if event.type == KEYDOWN and (event.key == K_UP or event.key == K_w):
            game.move_up()
        if event.type == KEYDOWN and (event.key == K_DOWN or event.key == K_s):
            game.move_down()
        if event.type == KEYDOWN and (event.key == K_LEFT or event.key == K_a):
            game.move_left()
        if event.type == KEYDOWN and (event.key == K_RIGHT or event.key == K_d):
            game.move_right()
        if event.type == KEYDOWN:
            if game.check() == 10:
                terminate()


def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
