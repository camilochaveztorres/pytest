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
            banken.add_customer('Camilo Chavez', 9304300505)
            banken.add_customer('Anna Marnfeldt', 9805453224)
            banken.add_customer('Cristina Chavez', 98010121054)
            answer = int(input("Type in your choice:\n"))
            if answer == 1:
                banken.get_customers()

            elif answer == 2:
                pnr = input("Insert your pnr:\n")
                banken.show_customer_info(pnr)

            elif answer == 3:
                name = input("Insert your name:\n")
                pnr = input("Insert your pnr:\n")
                banken.add_customer(name, pnr)

            elif answer == 4:
                new_name = input("Insert your new name:\n")
                pnr = input("Insert your pnr:\n")
                if banken.change_customer_name(new_name, pnr) == True:
                    print(f"Your new name is {new_name}")

            elif answer == 5:
                pnr = input("Insert your pnr:\n")
                banken.remove_customer(pnr)

            elif answer == 6:
                pnr = input("Insert your pnr:\n")
                banken.add_account(pnr)

            elif answer == 7:
                pnr = input("Insert your pnr\n")
                account_nr = input("Insert you account number\n")
                banken.get_account(pnr, account_nr)

            elif answer == 8:
                val = input("Type 1 to withdraw - Type 2 to deposit\n")
                if val == 1:
                    pnr = input("Insert your pnr:\n")
                    account_nr = input("Insert your account number:\n")
                    amount = int(input("Insert the amount of money you want to withdraw:\n"))
                    banken.withdrawal(pnr, account_nr, amount)
                elif val == 2:
                    pnr = input("Insert your pnr:\n")
                    account_nr = input("Insert your account number:\n")
                    amount = int(input("Insert the amount of money you want to deposit:\n"))
                    banken.deposit(pnr, account_nr, amount)
                else:
                    print("Error")


            elif answer == 9:
                pnr = input("Insert your pnr:\n")
                account_nr = input("Insert your account number:\n")
                banken.close_account(pnr, account_nr)

            else:
                print("WHAT ARE YOU DOING?")

        except ValueError:
            print("Please be kind to the app and only use numbers")


get_menu()
