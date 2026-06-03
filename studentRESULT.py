from openpyxl import Workbook
workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Name"
sheet["B1"] = "Math"
sheet["C1"] = "Pyhsics"
sheet["D1"] = "Chemistry"
sheet["E1"] = "Total"
sheet["F1"] = "Average"
sheet["G1"] = "Grade"

students = [
    ["rakesh",92,29,72],
    ["Ram",79,90,84],
    ["Sai",45,96,15]
    ]
row = 2

for student in students:
    total = student[1] + student[2] + student[3]
    average = total/3
    if student[1]<=35:
        grade = "Fail"
    elif student[2]<=35:
        grade = "Fail"
    elif student[3]<=35:
        grade = "Fail"
    else:
        grade = "Pass"
    sheet[f"A{row}"] = student[0]
    sheet[f"B{row}"] = student[1]
    sheet[f"C{row}"] = student[2]
    sheet[f"D{row}"] = student[3]
    sheet[f"E{row}"] = total
    sheet[f"F{row}"] = average
    sheet[f"G{row}"] = grade
    row = row + 1
workbook.save("Marks11.xlsx")


