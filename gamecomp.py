import random
import logging
import numpy as np

LOGGER = logging.getLogger(__name__)

class Game:
    def __init__(self, width, height, snake_head_pos=None):
        self.width = width
        self.height = height
        if snake_head_pos is None:
            snake_head_pos = (width // 2, height // 2)
        self.snake = [snake_head_pos,(snake_head_pos[0],snake_head_pos[1]+1),(snake_head_pos[0],snake_head_pos[1]+2)]

        self.apples = set()

        self.whole_space = set((i, j) for i in range(self.width) for j in range(self.height))

        self.make_apple()
        self.make_apple()

        self.food = 0

        self.endstate = False



    def empty_space(self):
        return self.whole_space - self.apples - set(self.snake)

    def make_apple(self):
        #self.apples.add((random.randint(0, self.width-1), random.randint(0, self.height-1)))
    #make_apple()
        self.apples.add(random.choice(tuple(self.empty_space())))

    def move_up(self):
        if self.food == 0:
            self.snake = [(self.snake[0][0], self.snake[0][1] - 1)] + self.snake[:-1]
        if self.food > 0:
            self.snake = [(self.snake[0][0], self.snake[0][1] - 1)] + self.snake
            self.food -= self.food




    def move_down(self):
        if self.food == 0:
            self.snake = [(self.snake[0][0], self.snake[0][1] + 1)] + self.snake[:-1]
        if self.food > 0:
            self.snake = [(self.snake[0][0], self.snake[0][1] + 1)] + self.snake
            self.food -= self.food



    def move_left(self):
        if self.food == 0:
            self.snake = [(self.snake[0][0] - 1, self.snake[0][1])] + self.snake[:-1]
        if self.food > 0:
            self.snake = [(self.snake[0][0] - 1, self.snake[0][1])] + self.snake
            self.food -= self.food



    def move_right(self):
        if self.food == 0:
            self.snake = [(self.snake[0][0] + 1, self.snake[0][1])] + self.snake[:-1]
        if self.food > 0:
            self.snake = [(self.snake[0][0] + 1, self.snake[0][1])] + self.snake
            self.food -= self.food

    def find_move_random(self):
        self.possible = []
        # self.move_left()
        if (self.snake[0][0], self.snake[0][1] - 1) not in self.snake and 0 <= self.snake[0][1] - 1:
            self.possible.append("u")
        if (self.snake[0][0], self.snake[0][1] + 1) not in self.snake and self.height > self.snake[0][1] + 1:
            self.possible.append("d")
        if (self.snake[0][0] - 1, self.snake[0][1]) not in self.snake and 0 <= self.snake[0][0] -1:
            self.possible.append("l")
        if (self.snake[0][0] + 1, self.snake[0][1]) not in self.snake and self.width > self.snake[0][0] + 1:
            self.possible.append("r")

        if self.possible == []:
            LOGGER.debug('no possible moves!')
            self.endstate = True
            return 0


        direction = random.choice(self.possible)

        if direction == "u":
            self.move_up()
        elif direction == "d":
            self.move_down()
        elif direction == "l":
            self.move_left()
        elif direction == "r":
            self.move_right()

        # print((self.snake[0][0] - 1, self.snake[0][1]))
        # print(self.snake)
        # print(self.possible)

    


    def is_collision(self):
        if self.snake[0] in self.snake[1:]:
            return True
        if 0 > self.snake[0][0]:
            return True
        if 0 > self.snake[0][1]:
            return True
        if self.width <= self.snake[0][0]:
            return True
        if self.height <= self.snake[0][1]:
            return True

    def is_apple(self):
        if self.snake[0] in self.apples:
            return True

    def eat_apple(self):
        self.apples.remove(self.snake[0])
        self.food = self.food + 1

    def check(self):
        if self.is_collision() == True:
            LOGGER.debug('collision!')
            self.endstate = True
        if self.is_apple() == True:
            LOGGER.info('on apple!')
            self.eat_apple()
            self.make_apple()
            #LOGGER.info('{0}'.format(self.empty_space()))



    def draw(self, win):
        win.write('O', fgcolor='orange', x=self.snake[0][0], y=self.snake[0][1])
        if len(self.snake) > 1:
            for segment in self.snake[1:-1]:
                win.write('#', fgcolor='red', x=segment[0], y=segment[1])
        win.write('#', fgcolor='yellow', x=self.snake[-1][0], y = self.snake[-1][1])
        if len(self.apples) != []:
            for apple in self.apples:
                win.write('@', fgcolor='green', x=apple[0], y=apple[1])

        win.colors = ('black','black')
        win.fill('x',region=(0,self.height,self.width,4))
        win.colors = ('white','black')
        win.write('snake length is {0}'.format(len(self.snake)), x=self.width//2 - 9, y=self.height)
