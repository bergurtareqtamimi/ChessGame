from board.tile import Tile
from pieces.none_piece import NonePiece


class Board:

    game_tiles = {}

    def __init__(self):
        pass

    def create_board(self):
        for tile in range(64):
            self.game_tiles[tile] = Tile(tile, NonePiece())

    def print_board(self):
        count = 0
        for squere in range(64):
            print("|",end=self.game_tiles[squere].piece_on_tile.toString())

            count += 1

            if count == 8:
                print("|",end="\n")
                count = 0