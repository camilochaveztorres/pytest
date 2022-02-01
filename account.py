class Account:

    def __init__(self, account_nr, customer_id):
        self.balance = 0
        self.account_type = "Debit account"
        self.account_nr = account_nr
        self.customer_id = customer_id

    def __str__(self):
        return f"Account number: {self.account_nr}, Balance: {self.balance}, Account type: {self.account_type}"

