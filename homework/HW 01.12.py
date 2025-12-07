### task 0
data = []
while True:
    numbers = input('Введите число:')
    items = numbers.split()
    filtered= [int(x) for x in items if x.isdigit and int(x) > 0 and int(x) %2 == 0]
    data.extend(filtered)
    if '0' in items:
        break
print('Результат:', data)
print('Длина списка:', len(data))

### task 1 (1)
celsius = [0, 15, 25, 30, 40, 100]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print('Градусы по Фаренгейту: ', fahrenheit)

### task 1 (2)
grades = [45, 85, 92, 33, 67, 78, 90, 55, 29, 88]
passed = [x for x in grades if x > 60]
print('Удовлетворительные оценки:', passed)

### task 2
transactions = [100, -50, 200, -30, 150, -20, 300]
taxes = [x * 0.15 for x in transactions if x > 0]
print('Налоги:', taxes)

### task 3
products = ['футболка', 'кружка', 'блокнот']
colors = ['красный', 'синий', 'зеленый']
combinations = [f"{product} - {color}" for product in products for color in colors]
print('Доступные комбинации:', combinations)

### task 4
employees = [('Иван', 45), ('Мария', 92), ('Петр', 33), ('Анна', 67)]
performance = [
    "Отлично" if percent >= 90 else "Хорошо" if percent >= 60 else "Требует улучшения" for name, percent, in employees
]
print(performance)

### task 5
sales = [ {'name': 'Алексей', 'sales': 150, 'returns': 10}, {'name': 'Ольга', 'sales': 200, 'returns': 5}, {'name': 'Дмитрий', 'sales': 80, 'returns': 25}, {'name': 'Елена', 'sales': 300, 'returns': 8}]
top_managers = [
    x["name"]
    for x in sales
    if (x["sales"] - x["returns"] >= 150) and (x["returns"] / x["sales"] * 100 < 10)
]
print(top_managers)