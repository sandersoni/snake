import logging
import os
import sys
from gamecomp import Game
import coloredlogs
import time
import matplotlib.pyplot as plt
import numpy as np

LOGGER = logging.getLogger(__name__)

WINWIDTH = 20
WINHEIGHT = 20




def main():
    log_fmt = "%(asctime)s %(name)s[%(lineno)d] %(levelname)s %(message)s"
    coloredlogs.install( level = logging.WARNING,fmt=log_fmt)



    if os.path.exists("length.txt"):
        os.remove("length.txt")

    lendata = []

    for i in range(9999):
        game = Game(WINWIDTH,WINHEIGHT)

        running = True

        while running == True:
            if game.endstate == True:
                # outfile = open("length.txt","a")
                # outfile.write(str(len(game.snake))+" \n")
                # outfile.close()
                lendata.append(len(game.snake))
                running = False
                # terminate()
            game.find_move_basic()
            game.check()

    # print(lendata)
    plt.hist(lendata,bins = 20)
    plt.savefig('length.png')
    plt.show()


def terminate():
    sys.exit()

if __name__ == '__main__':
    main()
