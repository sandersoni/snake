import random
import logging
import numpy as np

LOGGER = logging.getLogger(__name__)

class Node():
    """A node for a* pathfinding"""
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self,other):
        return self.position == other.position

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
        # self.make_apple()

        self.food = 0

        self.endstate = False

    def empty_space(self):
        return self.whole_space - self.apples - set(self.snake)

    def make_apple(self):
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

    def nearest_apple(self):
        apple_distances = []
        apples_list = list(self.apples)
        for apple in apples_list:
            apple_distances.append((apple[0] - self.snake[0][0])**2 + (apple[1] - self.snake[0][1])**2)
        # print(apple_distances)
        closest_index = apple_distances.index(min(apple_distances))
        # print(apples_list[closest_index])
        return apples_list[closest_index]

    def straight_distance_sq(self,start,end):
        return (start[0] - end[0])**2 + (start[1] - end[1])**2

    def nearest_apple_distance(self,start):
        return self.straight_distance_sq(start,self.nearest_apple())

    def find_move_basic(self):
        self.possible = []
        # self.move_left()
        if (self.snake[0][0], self.snake[0][1] - 1) not in self.snake and 0 <= self.snake[0][1] - 1:
            self.possible.append(("u",self.nearest_apple_distance((self.snake[0][0],self.snake[0][1] - 1))))
        if (self.snake[0][0], self.snake[0][1] + 1) not in self.snake and self.height > self.snake[0][1] + 1:
            self.possible.append(("d",self.nearest_apple_distance((self.snake[0][0],self.snake[0][1] + 1))))
        if (self.snake[0][0] - 1, self.snake[0][1]) not in self.snake and 0 <= self.snake[0][0] -1:
            self.possible.append(("l",self.nearest_apple_distance((self.snake[0][0] - 1,self.snake[0][1]))))
        if (self.snake[0][0] + 1, self.snake[0][1]) not in self.snake and self.width > self.snake[0][0] + 1:
            self.possible.append(("r",self.nearest_apple_distance((self.snake[0][0] + 1,self.snake[0][1]))))

        if self.possible == []:
            LOGGER.debug('no possible moves!')
            self.endstate = True
            return 0
        # print(self.possible)
        # print(min(self.possible, key = lambda item:item[1]))

        direction = min(self.possible, key = lambda item:item[1])[0]

        if direction == "u":
            self.move_up()
        elif direction == "d":
            self.move_down()
        elif direction == "l":
            self.move_left()
        elif direction == "r":
            self.move_right()

    def move_to(self,target):
        if target[0] = self.snake[0][0] + 1 and 

    def maze(self):
        self.maze_array = np.zeros((self.width,self.height))
        for segment in self.snake:
            self.maze_array[segment[0]][segment[1]] = 1
        return self.maze_array

    def find_move_a_star(self):
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

        start_node = Node(None,self.snake[0])
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None,self.nearest_apple())
        end_node.g = end_node.g = end_node.f = 0

        open_list = []
        closed_list = []

        open_list.append(start_node)

        # print(self.nearest_apple())
        # print("start")

        # counter = 0

        while len(open_list) > 0:

            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            open_list.pop(current_index)
            closed_list.append(current_node)
            # print("current and end nodes:")
            # print(current_node)
            # print(current_node.position)
            # print(end_node)
            # print(end_node.position)
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent

                return path[::-1]


            children = []
            for new_position in [(0,-1),(0,1),(-1,0),(1,0)]:

                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                #Makes sure node within the grid
                if node_position[0] > self.width - 1 or node_position[0] < 0 or node_position[1] > self.height or node_position[1] < 0:
                    continue
                if self.maze()[node_position[0]][node_position[1]] != 0.0:
                    continue

                new_node = Node(current_node, node_position)

                children.append(new_node)

            for child in children:

                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0])**2) +  ((child.position[1] - end_node.position[1])**2)
                child.f = child.g + child.h

                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                open_list.append(child)
            # for node in open_list:
            #     print(node.position)
            #     print(node.f)
            # print("end")
            # if counter == 4:
            #     break
            # counter = counter + 1


        # print(open_list)




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
