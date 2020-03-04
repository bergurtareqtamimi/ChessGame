import pygame
from board.chess_board import Board

# insert pygame for usage
pygame.init()

gameDisplay = pygame.display.set_mode((800,800))
pygame.display.set_caption("Chess with python")
clock = pygame.time.Clock()



chessBoard = Board()
chessBoard.create_board()
chessBoard.print_board()


quitGame = False


while not quitGame:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

    pygame.display.update()
    clock.tick(60)