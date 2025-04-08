import pygame
from board import *

def startup():
    board = Board()
    board.setValue(0, 0, 2)
    board.setValue(1, 0, 2)
    
    board.setValue(1, 0, 4)
    board.setValue(1, 1, 2)
    board.setValue(1, 2, 4)
    board.setValue(1, 3, 4)

    board.setValue(2, 0, 4)
    board.setValue(2, 2, 4)

    board.setValue(3, 3, 4)


    
    print(board)
    print()
    board.moveDown()

    print(board)
    print()
    board.moveLeft()
    print(board)
    return board


def render(items):
    pass
    
def main():
    # pygame setup
    # pygame.init()
    # screen = pygame.display.set_mode((1280, 720))
    # clock = pygame.time.Clock()
    running = True
    board = startup()


    '''
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE


        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
    '''
        

    # pygame.quit()
    return

if __name__ == "__main__":
    main()