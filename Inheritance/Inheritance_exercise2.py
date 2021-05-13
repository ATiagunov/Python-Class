class Figure:
    color = 'white'

    def paint(self, col):
        self.color = col

    def outing(self):
        pass


class Oval(Figure):
    def __init__(self, l, w):
        self.name = 'Oval'
        self.long = l
        self.width = w

    def outing(self):
        print(f'{self.name}: length - {self.long}, width - {self.width}, color - {self.color}')


class Square(Figure):
    def __init__(self, l, w):
        self.name = 'Square'
        self.long = l
        self.width = w

    def outing(self):
        print(f'{self.name}: length - {self.long}, width - {self.width}, color - {self.color}')


f1 = Oval(10, 6)
f1.outing()
f1.paint('yellow')
f1.outing()
f2 = Square(10, 10)
f2.outing()
f2.paint('red')
f2.outing()
