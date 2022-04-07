
class Field:
    def __init__(self, posx, posy, w=600//15):
        self.posx=posx
        self.posy=posy
        self.w=w

    def setPosX(self, posx):
        self.posx=posx

    def setPosY(self, posy):
        self.posy=posy


path = [Field(6,13), Field(6,12), Field(6,11), Field(6,10), Field(6,9),
                Field(5,8), Field(4,8), Field(3,8), Field(2,8), Field(1,8), Field(0,8),
                Field(0,8), Field(0,7), Field(0,6),
                Field(1,6), Field(2, 6), Field(3,6), Field(4,6), Field(5,6),
                Field(6, 5), Field(6, 4), Field(6, 3),Field(6, 2), Field(6, 1), Field(6, 0),
                Field(7, 0), Field(8, 0),
                Field(8, 1), Field(8, 2), Field(8, 3), Field(8, 4), Field(8, 5),
                Field(9, 6), Field(10, 6), Field(11, 6), Field(12, 6), Field(13, 6), Field(14, 6),
                Field(14, 7), Field(14, 8),
                Field(13, 8), Field(12, 8), Field(11, 8), Field(10, 8), Field(9, 8),
                Field(8, 9), Field(8, 10), Field(8, 11), Field(8, 12), Field(8, 13), Field(8, 14),
                Field(7, 14), Field(6, 14)]
