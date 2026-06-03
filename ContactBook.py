while True:
    print("1.Add contact")
    print("2.View contacts")
    print("3.Search contact")
    print("4.Delete contact")
    print("5.Exit")
    choice = input("Enter your choice : ")
    if choice == "1":
        name = input("Name : ")
        number = int(input("Number : "))
        file = open("contacts.txt", "a")
        file.write(name +" - " +str(number) + "\n")
        print("**Contact added successfully**")
        file.close()
    elif choice == "2":
        file = open("contacts.txt", "r")
        files = file.readlines()
        file.close()
        count = 1
        for line in files:
            print(count,line)
            count = count + 1
        file.close()
    elif choice == "3":
        search = input("Enter name : ").lower()
        file = open("contacts.txt", "r")
        found = False
        for line in file:
            if search in line.lower():
                print(line)
                found = True
                file.close()
        if found == False:
            print("No Contact found")
    elif choice == "4":
        file = open("contacts.txt", "r")
        files = file.readlines()
        file.close()
        count = 1
        for line in files:
            print(count,line)
            count = count + 1
        file.close()
        delete = int(input("Select contact : "))
        confirm = input("Confirm to delete?(YES/NO) : ").lower()
        if confirm =="yes".lower():
            files.pop(delete - 1)
            file = open("contacts.txt", "w")
            for line in files:
                file.write(line)
            print("**Contact deleted successfully**")
            file.close()
        else:
            file.close()
    elif choice == "5":
        break

