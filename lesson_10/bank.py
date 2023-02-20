import random


def get_random_digits(count: int):
    return ''.join([str(random.randint(0, 9)) for i in range(count)])


class BankAccount:
    def __init__(self, card_holder):
        self.card_holder = card_holder.upper()
        self.money = 0
        self.account_number = get_random_digits(20)
        self.card_number = get_random_digits(16)


class Bank:
    def __init__(self):
        self.bank_accounts : dict[str, BankAccount] = {}

    def open_account(self, card_holder):
        account = BankAccount(card_holder)
        self.bank_accounts[account.account_number] = account
        return account

    def add_money (self, account_number, money):
        account = self.bank_accounts[account_number]
        account.money += money

    def transfer_money (self, from_account_number, to_account_number, money):
        from_account = self.bank_accounts[from_account_number]
        from_account.money -= money
        to_account = self.bank_accounts[to_account_number]
        to_account.money += money

    def external_transfer(self, from_account_number, to_external_number, money):
        from_account = self.bank_accounts[from_account_number]
        from_account.money -= money
        to_somewhere = self.bank_accounts[to_external_number]
        print(f'Банк перевёл {money}$ с вашего счёта {from_account_number} на внешний счёт {to_external_number}')


class Controller:
    def __init__(self):
        self.bank = Bank()

    def run(self,):
        while True:
            print('0. Завершить программу')
            print('1. Открыть новый счёт')
            print('2. Просмотреть открытые счета')
            print('3. Положить деньги на счёт')
            print('4. Перевести деньги между счетами')
            print('5. Совершить платёж')
            num = int(input())
            if num == 0:
                print('До свидания!')
                break
            elif num == 1:
                print('Введите имя и фамилию держателя карты (на английском):')
                cart_holder = input('')
                self.bank.open_account(cart_holder)
                print(f'Счёт {cart_holder} создан.')
            elif num == 2:
                print(f'Ваши открытые счета: ')
                bank.bank_accounts()




if __name__ == '__main__':
    controller = Controller()
    controller.run()
