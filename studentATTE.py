from openpyxl import Workbook
workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Name"
sheet["B1"] = "Present Days"
sheet["C1"] = "Attendance %"
sheet["D1"] = "Verdict"

students = [
    ["Rakesh",156],
    ["Sai",142],
    ["Ram",139]
    ]
row = 2

for student in students:
    total_days = 200
    attendance = (student[1]/total_days)*100
    if attendance >=75:
        verdict = "Good"
    else:
        verdict = "Bad"
    sheet[f"A{row}"] = student[0]
    sheet[f"B{row}"] = student[1]
    sheet[f"C{row}"] = attendance
    sheet[f"D{row}"] = verdict
    row = row + 1
workbook.save("Attendance1.xlsx")