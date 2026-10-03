numbers = [3, 6, 1, 2, 2, 8, 10]
unik = []
for number in numbers:
    if number not in unik:
        unik.append(number)
    print(unik)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)


numbor = (1, 2, 3)
print(numbor[0])