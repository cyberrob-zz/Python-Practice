class Account:
   
    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.target_file_path = filepath        
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount
        self.commit()
        
    def deposit(self, amount):
        self.balance += amount
        self.commit()
        
    def commit(self):
        with open(self.target_file_path, 'w') as file:
            file.write(str(self.balance))



class Checking(Account):

    def __init__(self, filepath, fee = 10):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, receipt_account, amount):
        if receipt_account != '':
            self.balance -= (amount + self.fee)
            self.commit()
            return receipt_account
        else:
            print("No receipt account")
            return ''


checking = Checking('balance.txt')
transfer_account = checking.transfer('98732', 100)
print("Transfer ${} to {} with fee ${}. \nChecking amount: ${}".format(100, transfer_account, 10, checking.balance))

#
# account = Account('balance.txt')
# print("init amount: {}".format(account.balance))
#
# account.withdraw(100)
# print("amount: {}".format(account.balance))
#
# account.deposit(1203)
# print("amount: {}".format(account.balance))
#
