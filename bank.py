import customer as ctm
import itertools


class Bank:
    account_id = itertools.count(1001)
    customer_id = itertools.count(11111)

    def __init__(self):
        self.customer_list = []
        self.account_nr = 1

    def load(self):
        with open('customers.txt', 'r') as f:
            content = f.read()
            print(content)

    def get_customers(self):
        for customer in self.customer_list:
            print(customer)

    def add_customer(self, customer_name, pnr):
        for customer in self.customer_list:
            if customer.pnr == pnr:
                print("Customer with pnr already exists")
                return False
        new_customer = ctm.Customer(customer_name, pnr, next(self.customer_id))
        self.customer_list.append(new_customer)
        print(f"{new_customer.name} has been added to the bank with id: {new_customer.id}")
        return True

    def get_customer(self, pnr):
        for customer in self.customer_list:
            if pnr == customer.pnr:
                return customer

    def get_customer_info(self, pnr):
        lst = []
        for customer in self.customer_list:
            if pnr == customer.pnr:
                lst.append(customer.name)
                lst.append(customer.pnr)
                lst.append(customer.id)
                for account in customer.account_list:
                    lst.append(account)

        return lst

    def change_customer_name(self, new_name, pnr):
        try:
            customer = self.get_customer(pnr)
            customer.name = new_name
            return True
        except:
            print(f"Could not find customer with pnr of: {pnr}")
            return False

    def remove_customer(self, pnr):
        accounts = []
        customer = self.get_customer(pnr)
        accounts = customer.get_all_accounts()
        amount = customer.close_all_accounts()
        self.customer_list.remove(customer)
        print(f"Customer removed - {accounts} - {amount} returned")

    def add_account(self, pnr):
        customer = self.get_customer(pnr)
        try:
            customer.create_account(next(self.account_id))
        except:
            print("Customer does not exist!")

    def show_customer_info(self, pnr):
        customer = self.get_customer(pnr)
        customer.show_customer_info()

    def get_account(self, pnr, account_nr):
        customer = self.get_customer(pnr)
        print(customer.show_account_info(account_nr))

    def deposit(self, pnr, account_nr, amount):
        customer = self.get_customer(pnr)
        if customer.deposit(account_nr, amount):
            print('true')
            return True
        else:
            print('did not work')

    def withdrawal(self, pnr, account_nr, amount):
        customer = self.get_customer(pnr)
        if customer.deposit(account_nr, amount):
            print('true')
            return True
        else:
            print('did not work')

    def close_account(self, pnr, account_nr):
        customer = self.get_customer(pnr)
        balance = customer.close_account(account_nr)
        print(balance)

# def deposit(self):
