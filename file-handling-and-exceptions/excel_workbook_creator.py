import openpyxl

# Lumikha ng bagong Excel workbook
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Sheet1"

# Data mula sa tutorial ni Mosh
data = [
    ["transaction_id", "product_id", "price"],
    [1001, 1, 5.95],
    [1002, 2, 6.95],
    [1003, 3, 7.95]
]

# Isulat ang data sa mga rows
for row in data:
    sheet.append(row)

# I-save ang file bilang transactions.xlsx
wb.save("transactions.xlsx")

print("Ayun! Na-create na ang transactions.xlsx!")