import pygame
from board import *



def startup():
    board = Board()
    board.addRandomValue()
    print(board)
    print()
    return board

def createBackground(board: Board):
    width = 720
    height = 720
    background = pygame.Surface(width, height)
    distance = width / 4

    for col in range(3):
        rect = pygame.Rect(distance - 5, 0, 10, height)
        pygame.draw.rect(background, (0,0,0), )






def render(board):
    pass



    
def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    change = False

    board = startup()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    change = board.moveUp()
                    if change:
                        board.addRandomValue()
                if event.key == pygame.K_d:
                    change = board.moveRight()
                    if change: 
                        board.addRandomValue()
                if event.key == pygame.K_s:
                    change = board.moveDown()
                    if change:
                        board.addRandomValue()
                if event.key == pygame.K_a:
                    change = board.moveLeft()
                    if change:
                        board.addRandomValue()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        if change == True:
            change = False
            print(board)
            print()


        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

        

    pygame.quit()
    return

if __name__ == "__main__":
    main()