class Tile:

    piece_on_tile = None
    tile_coordinate = None

    def __init__(self,coordinate, piece):
        self.piece_on_tile = piece
        self.tile_coordinate = coordinate