class Person:
    def __init__(self):
        self.__name = 'Alex'
        self.__labs_to_do = 3

    def set_labs(self, num):
        if num >= 0:
            self.__labs_to_do = num
        else:
            print("Не может быть!")

    def get_labs(self):
        return self.__labs_to_do

    def get_name(self):
        return self.__name

    def display_info(self):
        print("Имя:", self.get_name(), "\tСколько осталось лабораторных:", self.get_labs())


a = Person()
a.display_info()
a.set_labs(2)
a.display_info()