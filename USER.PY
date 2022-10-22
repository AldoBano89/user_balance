from bank_account import BankAccount
class User:
    def __init__(self, name):
        self.name=name
        self.account = {
            "checking": BankAccount (0.2,1200 ),
            "savings": BankAccount (0.5 , 200 ),
        }

    def print_balance(self):
        print(f"{self.name} Savings Balance is {self.account['savings'].balance} and Checking Balance is {self.account['checking'].balance}")

    def transfert(self , user2 , amount):
        self.account['checking'].withdraw(amount)
        user2.account['checking'].deposit(amount)

sabrina = User('Sabrina')
fatjon = User('Fatjon')
sabrina.print_balance()
sabrina.transfert(fatjon , 300)
sabrina.print_balance()
fatjon.print_balance()


