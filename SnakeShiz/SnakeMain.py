import pygame
import time
import random 
# Board dimensions in cells
BOARD_WIDTH = 50
BOARD_HEIGHT = 35
CELL_SIZE = 10

pygame.init()
screen = pygame.display.set_mode(size = (BOARD_WIDTH*CELL_SIZE, BOARD_HEIGHT*CELL_SIZE))

def generate_random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

class SnakeSegment:
    def __init__(self, x, y, color = generate_random_rgb()):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x*CELL_SIZE, self.y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Snake:
    def __init__(self, hx, hy, direction):
        self.hx = hx
        self.hy = hy
        self.direction = direction
        self.chain = [SnakeSegment(hx, hy, )]

    def update(self):
        for event in events: # Update direction snake is heading in
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.direction = (1, 0)
                if event.key == pygame.K_UP:
                    self.direction = (0, -1)
                if event.key == pygame.K_LEFT:
                    self.direction = (-1, 0)
                if event.key == pygame.K_DOWN:
                    self.direction = (0, 1)

 

    def draw(self):
        for part in self.chain:
            part.draw()


segment = SnakeSegment(x = 10, y = 10)
segment.draw()

pygame.display.update()
time.sleep(3)


