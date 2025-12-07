### task 1
new_list = list(range(10))
print(new_list)

### task 2
close_numbers = list(range(2, 21, 2))
print(close_numbers)

### task 3
new_list_2 = list(range(10, 0, -1 ))
print(new_list_2)

### task 4
words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
for i in range(len(words)):
    if 'a' in words[i]:
        words[i] = 'FOUND'
print(words)

### task 5
products = ['Ноутбук', "Мышь", "Клавиатура", "Монитор"]
prices = [50000, 2500, 4000, 30000]
quantities = [8, 45, 25, 12]
total_revenue = 0


### task 6
products = ["Телефон", "Планшет", "Ноутбук", "Наушники"]
prices = [30000, 45000, 80000, 15000]
stock = [15, 8, 5, 20]
discounts = [10, 15, 20, 5]  # Скидки в процентах
for i in range(len(products)):
    prices[i] = prices[i] * (100 - discounts[i]) / 100
    print(f"Товар: {products[i]}\nЦена: {prices[i]}\nКоличество: {stock[i]}\n")

### task 7
fruits = ["apple", "banana", "cherry"]
print("Фрукты в корзине:")
for number, fruits in enumerate(fruits, start=1):
    print(f"{number}. {fruits}")

### task 8
close_numbers = list(range(0, 21, 2))
print(close_numbers)

print([x for x in range(21) if x % 2 == 0])

#### task 9
words = ["python", "data", "science", "list"]
length = [len(word) for word in words]

print(length)

### task 10
words = ["cat", "elephant", "dog", "butterfly", "ox"]
new_list = [word for word in words if len(word) >= 4 ]
print(f"Список слов длиннее 4 символов: {new_list}")
