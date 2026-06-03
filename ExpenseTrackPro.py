from openpyxl import Workbook
workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Expense"
sheet["B1"] = "Amount"
sheet["C1"] = "Category"

expenses = [
    ["Food",500],
    ["Movie",400],
    ["Internet",600]
    ]
row = 2
total_expense = 0
for expense in expenses:

    total_expense = total_expense + expense[1]
for expense in expenses:
    if expense[1]>=500:
        category = "Need"
    else:
        category = "Wants"
    sheet[f"A{row}"] = expense[0]
    sheet[f"B{row}"] = expense[1]
    sheet[f"C{row}"] = category
    row = row + 1
sheet[f"A{row}"] = "Total Expense"
sheet[f"B{row}"] = total_expense
workbook.save("Expenses3.xlsx")
