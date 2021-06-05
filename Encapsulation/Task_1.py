class Phone:
    def __init__(self):
        self.username = "Alex"
        self._number = 89001234567
        self.__how_many_times_turned_on = 0   # private variable

    def call(self):                  # public method
        print( "Ring-ring!" )

    def change_num(self, new):        # protected method
        self._number = new

    def __turn_on(self):             # private method
        self.__how_many_times_turned_on += 1
        print( "Times was turned on: ", self.__how_many_times_turned_on )

my_phone = Phone()

my_phone.call()
my_phone.change_num(123)
print("new number is", my_phone._number)
print( "The username is ", my_phone.username )

