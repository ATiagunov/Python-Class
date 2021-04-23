class Social:
    def __init__(self, name, age, income):
        self.name = name
        self.age = age
        self.income = income

    def info(self):
        print(f'name: {self.name}; age: {self.age}; income: {self.income}')

poor = Social('Jimmy', 21, '32048$')
lower_middle = Social('Sue', 26, '53413$')
middle = Social('David', 32, '106827$')
upper_middle = Social('Stacey', 36, '373894$')
rich = Social('Paul', 45, '999999$')
