class Point:
    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y

    def getX(self):
        return self.xCoord

    def getY(self):
        return self.yCoord

    def midPoint(self, otherPoint):
        """calculate the coordinates of the new midpoint."""
        newX = (otherPoint.getX() - self.xCoord) // 2 + self.xCoord
        newY = (otherPoint.getY() - self.yCoord) // 2 + self.yCoord
        return Point(newX, newY)
