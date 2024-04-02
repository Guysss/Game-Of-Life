import pygame
from copy import deepcopy
from math import floor
from random import randrange
from time import sleep

TABLE_SIZE = 60 #cell
CELL_SIZE = 15 #px

PERIODICITY = 100 #Periodicity of update in msec

POPULATION_THRESHOLD = 3
STABILITY_THRESHOLD = 2

#X/Y  0  1  2  3
#0 [ [0, 0, 0, 0],  
#1   [0, 0, 0, 0],  
#2   [0, 0, 0, 0],  
#3   [0, 0, 0, 0] ] 

cell = [[0 for y in range(TABLE_SIZE)] for x in range(TABLE_SIZE)]

class Window():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

    def __init__(self):
        self.size = CELL_SIZE*TABLE_SIZE
        self.screen = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption('Game Of Life')
        self.clear()

    def clear(self):
        self.screen.fill((255, 255, 255))

    def draw_grid(self):
        for x in range(0, self.size, CELL_SIZE):
            for y in range(0, self.size, CELL_SIZE):
               rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
               pygame.draw.rect(self.screen, self.BLACK, rect, 1)

    def draw_cell(self, x, y):
        color = self.BLUE if cell[x][y] == 1 else self.WHITE

        size = CELL_SIZE-1
        rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, size, size)
        pygame.draw.rect(self.screen, color, rect, 0)


def update_cell(x, y):
    counter = 0 #Num of alive cell

    #Check all near cells
    if(x != 0 and y != 0):
        if(cell[x-1][y-1] == 1): counter += 1

    if(x != 0):
        if(cell[x-1][y] == 1): counter += 1
    
    if(y != 0):
        if(cell[x][y-1] == 1): counter += 1

    if(y != TABLE_SIZE-1 and x != 0):
        if(cell[x-1][y+1] == 1): counter += 1
    if(y != TABLE_SIZE-1):
        if(cell[x][y+1] == 1): counter += 1

    if(x != TABLE_SIZE-1 and y != 0):
        if(cell[x+1][y-1] == 1): counter += 1
    if(x != TABLE_SIZE-1):
        if(cell[x+1][y] == 1): counter += 1

    if(x != TABLE_SIZE-1 and y != TABLE_SIZE-1): 
        if(cell[x+1][y+1] == 1): counter += 1

    if(counter == POPULATION_THRESHOLD): return 1 #The cell lives
    elif(counter == STABILITY_THRESHOLD): return cell[x][y] # The cell stay
    else: return 0 #The cell dies

def get_clicked_cell():
    x_mouse, y_mouse = pygame.mouse.get_pos()

    #Rounded down to get the index
    x = floor(x_mouse/CELL_SIZE)
    y = floor(y_mouse/CELL_SIZE)

    return (x, y)



if __name__ == '__main__':
    DELTATIME = 1/60 #Fps

    running = playing = True
    timer = 0

    pygame.init()

    window = Window()

    #Set random cells alive at the beginning of the game
    for i in range(200):
        x = randrange(0, TABLE_SIZE-1)
        y = randrange(0, TABLE_SIZE-1)
        cell[x][y] = 1

    while running:
        #Clear
        window.clear()
        window.draw_grid()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #Play and stop the game
                    playing = not playing

            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = get_clicked_cell()

                if pygame.mouse.get_pressed()[0]: # Left click
                    #Create cell
                    cell[x][y] = 1
                elif pygame.mouse.get_pressed()[2]: # Right click
                    #Delete cell
                    cell[x][y] = 0

                window.draw_cell(x, y)

        #Update only if the game is playing
        if(timer >= PERIODICITY and playing):
            temp_cell = deepcopy(cell)

            for x in range(TABLE_SIZE):
                for y in range(TABLE_SIZE):
                    temp_cell[x][y] = update_cell(x, y)
        
            cell = deepcopy(temp_cell)
            del temp_cell

            timer = 0

        #Draw cells
        for x in range(TABLE_SIZE):
            for y in range(TABLE_SIZE):
                window.draw_cell(x, y)

        pygame.display.update()

        #Timer
        sleep(DELTATIME)
        timer += DELTATIME*1000

    pygame.quit()