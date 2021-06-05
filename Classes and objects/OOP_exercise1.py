class Human:
    def __init__(self, name, stat):
        self.name = name
        self.stat = stat

    def stat_info(self):
        print(self.name, 'is', self.stat)


class State:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f'born in {self.name}')

    def bust(self, obj):
        obj.stat = "busted"


human_1 = Human('Ivan', 'free')
state_1 = State('Putin_land')
human_1.stat_info()
state_1.info()
state_1.bust(human_1)
human_1.stat_info()
