class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self.amount = amount
        try:
            if self.amount < 0:
                raise ValueError('Ты кого пытаешься ноебат')
            self._balance += self.amount
            print('Балик пополнен')
        except ValueError as error:
            print(error)

    def withdraw(self, amount):
        self.amount = amount
        try:
            if self.amount >= self._balance:
                raise ValueError('Иди нахуй нищеброд')
            self._balance -= self.amount
            print('Бабки сняты')
        except ValueError as error:
            print(error)

    def get_balance(self):
        print(f'Текущий балик: {self._balance}')


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance=0)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance += ((self._balance / 100)*self.interest_rate)
        print('Проценты капнули')

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        self.amount = amount
        self._balance -= self.amount
        print('Похуй один раз живем')




#Тест первого класса
my_acc = BankAccount('Иван', 0)
my_acc.deposit(100)
my_acc.withdraw(10)
my_acc.get_balance()


#Тест второго класса
myacc2 = SavingsAccount('Иван', balance=0, interest_rate = 1)
myacc2.deposit(2500)
myacc2.withdraw(300)
myacc2.apply_interest()
myacc2.get_balance()


#Тест третьего класса
myacc3 = CheckingAccount('Иоанн', 0)
myacc3.withdraw(1000)
myacc3.get_balance()







