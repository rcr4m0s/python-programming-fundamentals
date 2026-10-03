phonebook = {
    "Juan": "09171234567",
    "Maria": "09189876543",
    "Pedro": "09201112222"
}

input = input("What's your name? ")

if input in phonebook:
    print(phonebook[input])
else:
    print("No contact found!")
