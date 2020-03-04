from pieces.piece import Piece

class NonePiece(Piece):
    def __init__(self):
        pass

    def toString(self):
        return "-" 