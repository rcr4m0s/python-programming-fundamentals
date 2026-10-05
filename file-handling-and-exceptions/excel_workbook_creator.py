import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Sheet1"

data = [
    ["transaction_id", "product_id", "price"],
    [1001, 1, 5.95],
    [1002, 2, 6.95],
    [1003, 3, 7.95]
]

for row in data:
    sheet.append(row)

wb.save("transactions.xlsx")

print("Ayun! Na-create na ang transactions.xlsx!")