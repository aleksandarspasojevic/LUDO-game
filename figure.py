from field import path
from field import Field


def toCoord(place):
    return (place.posx * place.w + 6, place.posy * place.w - 15)


class Figure:
    def __init__(self, name, playerImage, inHomeCoords, startIndex, endFields):
        self.name = name
        self.playerImage = playerImage
        self.startIndex = startIndex
        self.currIndex = startIndex
        self.currPos = path[startIndex]
        self.inHome = True
        self.inHomeCoords = inHomeCoords
        self.playerRect = self.playerImage.get_rect()
        self.setRect()
        self.endFields = endFields
        self.crossed = 0
        self.ovr = 0

    def jump(self, num):
        if not self.inHome:
            if self.crossed + num < path.__len__() - 1:
                self.crossed += num
                self.currIndex = (self.currIndex + num) % path.__len__()
                self.currPos = path[self.currIndex]
            else:
                if (self.crossed + num) % (path.__len__() - 1) <= 6:
                    self.ovr = (self.crossed + num) % (path.__len__() - 1)
                    self.crossed += num

                if self.ovr < 6:
                    self.currPos = self.endFields[self.ovr]

        if num == 6:
            self.inHome = False
        self.setRect()

    def show(self, screen):
        if self.inHome:
            screen.blit(self.playerImage, self.inHomeCoords)
        else:
            screen.blit(self.playerImage, toCoord(self.currPos))

    def setRect(self):
        if self.inHome:
            x, y = self.inHomeCoords
            self.playerRect.topleft = [x, y]
        else:
            x1, y1 = toCoord(self.currPos)
            self.playerRect.topleft = [x1, y1]

    def reachedFinalPos(self):
        return self.ovr == 5
