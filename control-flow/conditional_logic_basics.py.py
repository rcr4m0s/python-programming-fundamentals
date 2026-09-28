#IF/ELIF/ELSE

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day!")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day!")
print("Enjoy your day")



has_good_credit = True
price = 1000000
if has_good_credit:
    down_payment = 0.1 * price
    print("You need to put down 10%")
else:
    down_payment = 0.2 * price
    print("You need to put down 20%")
print(down_payment)



has_gudcredit = True
has_highincome = False

if has_gudcredit or has_highincome:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


temparature = 30

if temparature > 30:
    print("It's a hot day")
else: 
    print("It's not a hot day")



name = (input("What's your name? "))

if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 20:
    print("Name must be a max of 20 characters")
else:
    print("Name looks good")




weight = int(input("Weight: "))
convert = (input("(L)bs or (K)g: "))
if convert.upper() == "L":
    converted = weight * 0.45
    print(converted)
else:
    converted = weight * 2.2
    print(converted)