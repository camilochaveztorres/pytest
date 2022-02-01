import account as ac


class Customer:
    def __init__(self, name, pnr, customer_id):
        self.name = name
        self.pnr = pnr
        self.id = customer_id
        self.account_list = []

    def __str__(self):
        return f"Name: {self.name} - Pnr: {self.pnr}"

    def create_account(self, account_nr):
        new_account = ac.Account(account_nr, self.id)
        self.account_list.append(new_account)
        print(f"Account created - Account number: {account_nr}")

    def show_customer_info(self):
        accounts = []
        for account in self.account_list:
            accounts.append(str(account))
        print(f"{self.name} : id {self.id} : Accounts :{accounts}")

    def get_all_accounts(self):
        accounts = []
        for account in self.account_list:
            accounts.append(str(account))
        return accounts

    def show_account_info(self, account_nr):
        for account in self.account_list:
            if account.account_nr == account_nr:
                return account

    def deposit(self, account_nr, amount):
        for account in self.account_list:
            if account.account_nr == account_nr:
                account.balance += amount
                return True

    def withdrawal(self, account_nr, amount):
        for account in self.account_list:
            if account.account_nr == account_nr:
                account.balance -= amount
                return True

    def close_account(self, account_nr):
        for account in self.account_list:
            if account.account_nr == account_nr:
                self.account_list.remove(account)
                return account.balance

    def close_all_accounts(self):
        money = 0
        for account in self.account_list:
            self.account_list.remove(account)
            money += account.balance
