import logging
import sys
from gamecomp import Game
import coloredlogs
import time

LOGGER = logging.getLogger(__name__)

WINWIDTH = 20
WINHEIGHT = 20




def main():
    log_fmt = "%(asctime)s %(name)s[%(lineno)d] %(levelname)s %(message)s"
    coloredlogs.install( level = logging.DEBUG,fmt=log_fmt)

    game = Game(WINWIDTH,WINHEIGHT)

    while True:
        if game.endstate == True:
            terminate()
        game.find_move_random()
        game.check()

def terminate():
    sys.exit()

if __name__ == '__main__':
    main()
