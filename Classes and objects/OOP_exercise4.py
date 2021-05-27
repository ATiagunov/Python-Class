class Ticket:
    cost = 19
    station = "Центр"


class Student:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def ride(self, ticket):
        if self.money < ticket.cost:
            print(f"{self.name} идет пешком")
        else:
            print(f"{self.name} едет на станцию {ticket.station}")


s = Student('Саша', 10)
m = Student("Маша", 20)
s.ride(Ticket)
m.ride(Ticket)

