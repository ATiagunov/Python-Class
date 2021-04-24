class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f'My name is {self.name}')

    def learn(self):
        raise NotImplementedError

class Programmer(Person):
    def __init__(self, name, programming_language):
        super().__init__(name)
        self.programming_language = programming_language
        self.known_pl = [self.programming_language]

    def learn(self, programming_language = None):
        if programming_language is not None:
            self.known_pl.append(programming_language)

class Singer(Person):

    def __init__(self, name):
        super().__init__(name)
        self.known_songs = []

    def learn(self, song=None):
        if song is not None:
            self.known_songs.append(song)

    def introduce(self):
        if len(self.known_songs) == 0:
            known_songs = 'no songs'
        else:
            known_songs = ' '.join(self.known_songs)
        print(f'My name is {self.name} and I can sing {known_songs}')

alex = Programmer('Alex', 'Python')
alex.introduce()
alex.learn('C++')
print(alex.known_pl)

jane = Singer('Jane')
jane.introduce()
jane.learn('Tiny Dancer')
print(jane.introduce())
