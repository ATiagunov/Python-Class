#Создайте класс, содержащий, как минимум, два метода: публичный (public)
# и приватный (private), при этом приватный метод вызывается в открытом методе.

class BankAccount:
    name = 'Bill'
    account_id = 12345
    __balance = 20000
    __password = 'ABC'

    def change_balance(self, pswrd, new_balance_value):
        if self.__password == pswrd:
            self.__balance = new_balance_value
            print("Balance changed! New balance is", new_balance_value)
        else:
            print("Incorrect password!")
    def __print_balance(self):
        print(self.__balance)

    def balance_info(self):
        print(f'{self.name} has {self.__print_balance()}')


acc = BankAccount()
acc.balance_info()
acc.change_balance('АБВ', 10000)
acc.change_balance('ABC', 10000)
acc.balance_info()
