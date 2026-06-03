while True:
    print("1.Add book")##
    print("2.View book")##
    print("3.search book")##
    print("4.Delete book")##
    print("5.Borrow book")
    print("6.Return book")
    print("7.Exit")
    choice = input("Enter your choice : ")
    if choice == "1":
        add = input("Add book : ")
        file = open("books.txt", "a")
        file.write(add + " - Available" + "\n")
        file.close()
    elif choice == "2":
        file = open("books.txt", "r")
        count = 1
        for line in file:
            print(count,line)
            count = count + 1
        file.close()
    elif choice == "3":
        file = open("books.txt", "r")
        search = input("Enter Book name : ").lower()
        found = False
        for line in file:
            if search in line.lower():
                print("**Available**")
                found = True
        file.close()
        if found == False:
            print("**Not Available**")
    elif choice == "4":
        file = open("books.txt", "r")
        files = file.readlines()
        file.close()
        count = 1
        for line in files:
            print(count,line)
            count = count + 1
        file.close()
        delete = int(input("Enter book number : "))
        files.pop(delete - 1)
        file = open("books.txt", "w")
        for line in files:
            file.write(line)
        print("**Book deleted successfully**")
        file.close()
    elif choice == "5":

        file = open("books.txt", "r")

        files = file.readlines()

        file.close()

        borrow = input("Enter book name : ")

        for i in range(len(files)):

            if borrow.lower() in files[i].lower():

                if "Available" in files[i]:
                    files[i] = files[i].replace(
                        "Available",
                        "Borrowed"
                    )

                    print("**Book borrowed successfully**")

        file = open("books.txt", "w")

        for line in files:
            file.write(line)

        file.close()

    elif choice == "6":

        file = open("books.txt", "r")

        files = file.readlines()

        file.close()

        borrow = input("Enter book name : ")

        for i in range(len(files)):

            if borrow.lower() in files[i].lower():

                if "Available" in files[i]:
                    files[i] = files[i].replace(
                        "Borrowed",
                        "Available"
                    )

                    print("**Book is Available**")

            file = open("books.txt", "w")

            for line in files:
                file.write(line)

            file.close()

    elif choice == "7":

        break