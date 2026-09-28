coordinates = (1, 2, 3)

x, y, z = coordinates
print(y)


customer = {
    "name": "John Smith",
    "age": 23,
    "is_verified": True
}
print(customer.get("birthdate"))


phone = input("Phone: ")
nice = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for i in phone:
    output += nice.get(i, " ! ") + " "
print(output)


message = input(">")
words = message.split(' ')
emojis = {
    ":)": "nice",
    ":()": "longkot"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

