import bank

banken = bank.Bank()


# banken.add_customer('Camilo Chavez', 9304300505)
# banken.add_customer('Anna Marnfeldt', 9805453224)
# banken.add_customer('Cristina Chavez', 98010121054)
# banken.remove_customer(9304300505)
# banken.get_customers()
# banken.add_account(98010121054)
# banken.add_account(98010121054)
# banken.show_customer_info(98010121054)
# banken.change_customer_name('Crissy Chavez', 98010121054)
# banken.show_customer_info(98010121054)
# banken.deposit(98010121054, 1002, 50000)
# banken.get_account(98010121054, 1002)
# banken.add_customer('Camilo', 98010121054)
# banken.get_customers()


def get_menu():

    run = True
    print("Welcome to the bank!")
    while run:

        print("Choose one of the following\n1.Get all customers\n2.Get specific customer\n"
              "3.Add new customer\n4.Change customer name\n5.Delete customer\n6.Add account to customer\n"
              "7.Get account\n"
              "8.Withdraw /Deposit money\n9.Close account\n0.Exit")
        try:
            add_new_customer("Camilo Chavez", 9304300505)
            add_new_customer("Anna Marnfeldt", 9805453224)
            add_new_customer("Cristina Chavez", 98010121054)

            answer = int(input("Type in your choice:\n"))
            if answer == 1:
                get_all_customers()

            elif answer == 2:
                pnr = input("Insert your pnr:\n")
                get_specific_customer(pnr)

            elif answer == 3:
                name = input("Insert your name:\n")
                pnr = input("Insert your pnr:\n")
                add_new_customer(name, pnr)

            elif answer == 4:
                name = input("Insert your new name:\n")
                pnr = input("Insert your pnr:\n")
                change_customer_name(name, pnr)

            elif answer == 5:
                pnr = input("Insert your pnr:\n")
                delete_customer(pnr)

            elif answer == 6:
                pnr = input("Insert your pnr:\n")
                add_account_to_customer(pnr)

            elif answer == 7:
                pnr = input("Insert your pnr\n")
                account_nr = input("Insert you account number\n")
                get_account(pnr, account_nr)

            elif answer == 8:
                pnr = input("Insert your pnr:\n")
                account_nr = input("Insert your account number:\n")
                amount = int(input("Insert the amount of money you want to deposit:\n"))
                deposit_money(pnr, account_nr, amount)

                pnr = input("Insert your pnr:\n")
                account_nr = input("Insert your account number:\n")
                amount = int(input("Insert the amount of money you want to withdraw:\n"))
                withdraw_money(pnr, account_nr, amount)

            elif answer == 9:
                pnr = input("Insert your pnr:\n")
                account_nr = input("Insert your account number:\n")
                close_account(pnr, account_nr)

            else:
                print("WHAT ARE YOU DOING?")

        except ValueError:
            print("Please be kind to the app and only use numbers")


def get_all_customers():
    banken.get_customers()


def get_specific_customer(pnr):
    banken.show_customer_info(pnr)


def add_new_customer(name, pnr):
    banken.add_customer(name, pnr)


def change_customer_name(new_name, pnr):
    banken.change_customer_name(new_name, pnr)


def delete_customer(pnr):
    banken.remove_customer(pnr)


def add_account_to_customer(pnr):
    banken.add_account(pnr)


def deposit_money(pnr, account_nr, amount):
    banken.deposit(pnr, account_nr, amount)


def withdraw_money(pnr, account_nr, amount):
    banken.withdrawal(pnr, account_nr, amount)


def close_account(pnr, account_nr, ):
    banken.close_account(pnr, account_nr)


def get_account(pnr, account_nr):
    banken.get_account(pnr, account_nr)


get_menu()
