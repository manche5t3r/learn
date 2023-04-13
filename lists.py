phones = ['iPhone 14', "Samsung Galaxy S23", 'Xiaomi 13']
phones.append('OnePlus 11')

print('iPhone 14' in phones)
del phones[1]
print(phones)

phones.remove('OnePlus 11')
print(phones)

numbers = [3, 5, 7, 9, 10.5]
print(numbers)
numbers.append('Python')
print(len(numbers))
print(numbers[0])
print(numbers[5])
print(numbers[1:4])
numbers.remove('Python')
print(numbers)