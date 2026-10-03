def calculate_move_bill(ages):
    
    total = 0
    kids = 0
    regular = 0
    seniors = 0
    for age in ages:

       
        if age < 12:
            kids += 1
            bill = 100
        elif age >= 12 and age <60:
            regular += 1
            bill = 200
        elif age >= 60:
            seniors += 1
            bill = 120
        total += bill


    print("---SINEHAN RECEIPT---")
    print(f"Kids (<12): {kids}")
    print(f"Regular (12-59): {regular}")
    print(f"Seniors (60+): {seniors}")

    print(f"Total Bill: (P{total})")

ilan  = []

for i in range(3):
    wew = int(input("What is the age of the customer? "))
    ilan.append(wew)


calculate_move_bill(ilan)