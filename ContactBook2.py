while True:
    print("1.Add contact")
    print("2.View contacts")
    print("3.Delete contact")
    print("4.Search contact")
    print("5.Exit")
    choice = input("Enter your choice : ")
    if choice == "1":
        name = input("Name : ")
        number = input("Number : ")
        file = open("contacts.txt", "a")
        file.write(name + " - "+ number + "\n")
        print("**Saved successfully**")
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
        file = open("contacts.txt", "r")
        files = file.readlines()
        file.close()
        count = 1
        for line in files:
            print(count,line)
            count = count + 1
        file.close()
        delete = int(input("Choice contact : "))
        files.pop(delete - 1)
        file = open("contacts.txt", "w")
        for line in files:
            file.write(line)
        print("**Contact Deleted successfully**")
        file.close()
    elif choice == "4":
        search = input("Name : ").lower()
        file = open("contacts.txt", "r")
        files = file.readlines()
        file.close()
        found = False
        for line in files:
            if search in line.lower():
                print(line)
                found =True
        if found ==False:
            print("\033[31mNo contacts found\033[0m")
            file.close()
    elif choice == "5":
        break