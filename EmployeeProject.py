while True:
    print("1.Add Employee")
    print("2.View Employee")
    print("3.Search Employee")
    print("4.Delete Employee")
    print("5.Update Salary")
    print("6.EXIT")
    choice = input("Enter your choice : ")
    if choice == "1":
        name = input("Enter Employee name : ")
        salary = int(input("Enter salary : "))
        file = open("salary.txt", "a")
        file.write(name + " - " + str(salary) + "\n")
        file.close()
    elif choice == "2":
        file = open("salary.txt", "r")
        files = file.readlines()
        file.close()
        count = 1
        for line in files:
            print(count,line)
            count = count + 1
        file.close()
    elif choice == "3":
        file = open("salary.txt", "r")
        files = file.readlines()
        file.close()
        search = input("Enter Employee name : ").lower()
        found = False
        for line in files:
            if search in line.lower():
                print(line)
                found = True
        if found == False:
            print("Employee not existed")
    elif choice == "4":
        file = open("salary.txt", "r")
        files = file.readlines()
        file.close()
        count = 1
        for line in files:
            print(count, line)
            count = count + 1
        delete = int(input("Enter Employee number : "))
        files.pop(delete - 1)
        file = open("salary.txt", "w")
        for line in files:
            file.write(line)
        print("**Employee data deleted successfully**")
        file.close()
    elif choice == "5":
        file = open("salary.txt", "r")
        files = file.readlines()
        file.close()
        name = input("Enter Employee Name : ").lower()
        new_salary = input("Enter new salary : ")
        for i in range(len(files)):

            if name in files[i].lower():
                files[i] = name.title() + " - " + new_salary + "\n"
                print("Data updated successfully")
                file = open("salary.txt", "w")

        for line in files:
            file.write(line)

        file.close()
    elif choice == "6":
        break
