#ATM
balance = 5000

while True:
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Cash")
    print("4.Exit")

    choice = input("Enter your choice : ")
    if choice == "1":
        print("Balance : ",balance)
    elif choice == "2":
        amount = int(input("Enter deposit amount : "))
        balance = int(amount) + int(balance)
        print("Updated Balance : ",balance)
    elif choice == "3":
        withdraw = int(input("Enter amount : "))
        if withdraw>balance:
            print("Insufficient amount")
        else:
            print("Remaining Balance : ", balance - withdraw)
    elif choice == "4":
        break


