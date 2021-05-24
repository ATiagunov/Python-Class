class Person:
    __name = 'Alex'
    __labs_to_do = 3

    def set_labs(self, num):
        if num >= 0:
            self.__labs_to_do = num
        else:
            print("Не может быть!")

    def __get_labs(self):
        return self.__labs_to_do

    def __get_name(self):
        return self.__name

    def display_info(self):
        print("Имя:", self.__get_name(), "\tСколько осталось лабораторных:", self.__get_labs())


a = Person()
a.display_info()
a.set_labs(2)
a.display_info()