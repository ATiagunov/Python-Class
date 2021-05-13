class Director:
    def __init__(self, n):
        self.position = 'Director'
        self.name = n

    def info(self):
        print(self.position, self.name)


class Executive:
    def __init__(self, n):
        self.position = 'Executive'
        self.name = n

    def info(self, Director):
        print(f'{self.position} {self.name} is supervised by {Director.position} {Director.name}')


class Manager:
    def __init__(self, n):
        self.position = 'Manager'
        self.name = n
    def info(self, Executive):
        print(f'{self.position} {self.name} is supervised by {Executive.position} {Executive.name}')


class Employer:
    def __init__(self, n):
        self.position = 'Employer'
        self.name = n
    def info(self, Manager):
        print(f'{self.position} {self.name} is supervised by {Manager.position} {Manager.name}')


director1 = Director("Elon")
director1.info()
ceo1 = Executive('Robert')
ceo1.info(director1)
ceo2 = Executive('Marie')
ceo2.info(director1)
manager1 = Manager('Jacob')
manager1.info(ceo1)
manager2 = Manager('Alicia')
manager2.info(ceo2)
employer1 = Employer('J')
employer1.info(manager1)
employer2 = Employer('Christina')
employer2.info(manager1)
employer3 = Employer('Franklin')
employer3.info(manager2)
employer4 = Employer('Elizabeth')
employer4.info(manager2)
