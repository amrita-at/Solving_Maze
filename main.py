import pygame

from constants import *
from userInput import createGrid, getStartEnd
from algorithm import Grid

grid, dims = createGrid()
start, end = getStartEnd(dims)
gridObj = Grid(grid, start, end, dims)
final_path = gridObj.getEnd()


HEIGHT = (dims[0]) * BLOCK_HEIGHT
WIDTH = (dims[1]) * BLOCK_WIDTH


black_box = pygame.Surface((100, 70))
black_box.fill(BLACK)

yellow_box = pygame.Surface((100, 70))
yellow_box.fill(YELLOW)

green_box = pygame.Surface((100, 70))
green_box.fill(GREEN)

orange_box = pygame.Surface((100, 70))
orange_box.fill(ORANGE)

blue_box = pygame.Surface((100, 70))
blue_box.fill(BLUE)

white_box = pygame.Surface((110, 80))
white_box.fill(WHITE)

pygame.font.init()
myfont = pygame.font.SysFont("Arial", 20)


def draw_grid():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            xcoord = x * 100
            ycoord = y * 70

            x_coord = xcoord + 2
            y_coord = ycoord + 2

            screen.blit(white_box, (xcoord, ycoord))

            if grid[y][x] == 1:
                screen.blit(black_box, (x_coord, y_coord))

            if grid[y][x] == 0:
                screen.blit(yellow_box, (x_coord, y_coord))

            if (y, x) == start:
                screen.blit(orange_box, (x_coord, y_coord))

            if (y, x) == end:
                screen.blit(green_box, (x_coord, y_coord))

            if (y, x) in final_path:
                text = myfont.render("R: %d C: %d" % (y, x), 0, (0, 0, 0))
                screen.blit(text, (x_coord + 15, y_coord + 25))

    while True:
        # gets a single event from the event queue
        pygame.display.update()
        event = pygame.event.wait()

        # if the 'close' button of the window is pressed
        if event.type == pygame.QUIT:
            # stops the application
            break

        # finalizes Pygame
    pygame.quit()


if __name__ == '__main__':
    draw_grid()
