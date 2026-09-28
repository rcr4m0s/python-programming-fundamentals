def calculate_bill(prices):
    subtotal = 0
    
    for price in prices:
        subtotal += price
        
    if subtotal >= 1000:
            discount = subtotal * 0.10
    elif subtotal >= 500 and subtotal < 1000:
            discount = subtotal * 0.05
    elif subtotal < 500:
            discount = 0

    final_total = subtotal - discount
    
    print("---RECEIPT---")
    print(f"Subtotal: {subtotal}")
    print(f"Discount: {discount}")
    print(f"Final Total: {final_total}")

user_ques = []

for i in range(3):
    faq = float(input(f"Enter price for item {i + 1}: "))
    user_ques.append(faq)

calculate_bill(user_ques)