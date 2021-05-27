class Table:
    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long, self.width, round(self.height, 1))


class Kitchen(Table):
    def howplaces(self, n):
        if n < 2:
            print("It is not kitchen table")
        else:
            self.places = n

    def outplases(self):
        print(self.places)


class Carpenter(Table):
    def lengthen(self, m):
        self.long += m

    def raise_height(self, c):
        self.height += c


t = Carpenter(1,3,0.7)
t.outing()
t.lengthen(0.5)
t.raise_height(0.2)
t.outing()
