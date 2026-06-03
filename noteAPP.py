#Note APP
while True:
    print("1.Add note")
    print("2.View notes")
    print("3.Delete note")
    print("4.Exit")

    choice = input("Enter your choice : ")
    if choice == "1":
        note = input("Enter note : ")
        file = open("notes.txt", "a")
        file.write(note +"\n")
        file.close()
    elif choice == "2":
        file = open("notes.txt", "r")
        count = 1
        for line in file:
            print(count,line)
            count = count + 1
        file.close()
    elif choice == "3":
        file = open("notes.txt", "r")
        files = file.readlines()
        file.close()
        count = 1
        for line in files:
            print(count, line)
            count = count + 1
        note_number= int(input("Enter note number : "))
        files.pop(note_number - 1)
        file = open("notes.txt", "w")
        for line in files:
            file.write(line)
        file.close()
    elif choice == "4":
        break



