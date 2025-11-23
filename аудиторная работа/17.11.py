my_list = [0, 1, 2, 3]
my_list[2] = 'two'
print(my_list)
print(type(my_list))
# 0, 1, two, 3

my_tuple = (0, 1, 2, 3)
print(type(my_tuple))

my_set = {0, 1, 2, 2, 3}
print(my_set)
# 0, 1, 2, 3
print(type(my_set))

fruits = ["яблоко", "банан"]
fruits.append("апельсин")
print(fruits)  # ["яблоко", "банан", "апельсин"]

mylist = [42, 'word', []]

coordinates = (59.923040, 30.303444)
mytuple_fix = ('id123', 'id321', 'id456')

my_str = ('programming')
my_str = set(my_str)
print(my_str)

data = "программирование"
data = set(data)
print(data)

set('word')
list('word')
tuple('word')

x = "программирование"
print(tuple(x))

hse_coordinates = (59.9339, 30.3061) 
math_constants = (3.14159, 2.71828, 1.61803)
students_id = (22234, 22235, 22236)

print(tuple(hse_coordinates))

stack = []

# Добавляем элементы (push)
stack.append("тарелка1")  # низ стека
stack.append("тарелка2")
stack.append("тарелка3")  # верх стека
print(stack)
# Удаляем элементы (pop) - всегда с КОНЦА!
last_item = stack.pop()
print(last_item)  # 'тарелка3'
print(stack)      # ['тарелка1', 'тарелка2']

# Стек операций отмены (Undo)
actions = []

# Пользователь делает действия
actions.append("напечатал А")
actions.append("напечатал Б") 
actions.append("напечатал В")
print(actions)
# CTRL+Z - отмена последнего действия
last_action = actions.pop()
print(f"Отменили: {last_action}")  # "Отменили: напечатал В"

numbers = [10, 20, 30]
# 1. Добавьте число 40 в конец
# 2. Удалите число 20
# 3. Вставьте число 5 на начало списка
# Выведите результат
numbers.append(40)
numbers.remove(20)
numbers.insert(0, 5)
print(numbers)

# Создание
person = ("Анна", 25, "инженер")

# Чтение - можно
name = person[0]        # "Анна"
age = person[1]         # 25
# person[1] = 26        # ОШИБКА!

rgb = (255, 128, 0)
# 1. Выведите второй элемент кортежа
# 2. Попробуйте изменить первый элемент на 200
# 3. Объясните, какая ошибка возникла
print(rgb[1])
print(rgb)

students_math = {"Аня", "Боря", "Вова"}
students_physics = {"Боря", "Галя", "Дима"}

# Объединение
all_students = students_math | students_physics
# {"Аня", "Боря", "Вова", "Галя", "Дима"}
# Пересечение
both_subjects = students_math & students_physics
# {"Боря"}

# Добавление
students_math.add("Зоя")

# Дано:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Найдите:
# 1. Общие элементы (пересечение)
# 2. Все уникальные элементы (объединение)
# 3. Элементы, которые есть в set1, но нет в set2
both_sets = set1 | set2
unique_elements = set1 & set2
unique_set1 = set1 - set2
print(both_sets,'\n',unique_elements,'\n',unique_set1)

#### поменять
mixed_data = [
    1, 
    "hello", 
    3.14, 
    [1, 2], 
    42, 
    "world", 
    0, 
    (5, 6),
    {"name": "John"},
    True,
    {7, 8, 9}
]
lists = []
tuples = []
sets = []
numbers = []
strings = []
float_numbers = []

for structure in mixed_data: 
   if isinstance(structure, list): 
       lists.append(structure)
   elif isinstance(structure, tuple): 
       tuples.append(structure)
   elif isinstance(structure, int): 
       numbers.append(structure)
   elif isinstance(structure, str): 
       strings.append(structure)
   elif isinstance(structure, float): 
       float_numbers.append(structure)
   elif isinstance(structure, set): 
       sets.append(structure)
print(f"Целые числа: {numbers}, \nСтроки: {strings}, \nДробные числа: {float_numbers}, \nСписки: {lists}, \nКортежи: {tuples}, \nМножества' {sets}")

###
a = 0
while a != 5:
    a += 5 

###
while True:
    condition = input()
    if condition == 'stop':
        break

#####
a = 0
while a<5:
    a+=1
    print(a)

###
while True:
    if word == 'stop':
        break
    word = input('Введите слово:')
    print(list(word))

####
correct_password = "secret123"
logged_in = False
attempts = 0
max_attempts = 3
while attempts < max_attempts and logged_in == False:
    password = input('Введите пароль:')
    if password == correct_password:
        logged_in = True
        break
    else:
        attempts +=1
if logged_in == True:
    print('you are in')
else:
    print('you are blocked')