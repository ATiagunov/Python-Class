class ticket:
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


ticket = ticket()
jack = Student('Саша', 10)
tina = Student("Маша", 20)
jack.ride(ticket)
tina.ride(ticket)

