# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#| label: houses-py

students = [
        {'name': 'Гаррі Поттер', 'house': 'Ґрифіндор'},
        {'name': 'Герміона Грейнджер', 'house': 'Ґрифіндор'},
        {'name': 'Рон Уізлі', 'house': 'Ґрифіндор'},
        {'name': 'Драко Малфой', 'house': 'Слизерин'},
        {'name': 'Том Реддл', 'house': 'Слизерин'},
        {'name': 'Седрик Діггорі', 'house': 'Гафелпаф'},
        {'name': 'Луна Лавґуд', 'house': 'Рейвенклов'}
]
#
#
#
#
#
#
#
#| label: houses-py-unique-houses

unique_houses = []
for student in students:
    if student['house'] not in unique_houses:
        unique_houses.append(student['house'])

print(unique_houses)
#
#
#
#
#
fruits = {'apple', 'apple', 'banana', 'orange'}
print(fruits)
#
#
#
#
#
#
#
#
#
#
#
fruits = {'apple', 'banana', 'orange'}
fruits.add('melon')
print(fruits)
#
#
#
#
#
fruits = {'apple', 'banana', 'orange'}
fruits2 = {'melon', 'watermelon'}
fruits3 = fruits.union(fruits2)
print(fruits3)
#
#
#
#
#
fruits = {'apple', 'banana', 'orange'}
fruits.clear()
print(fruits)
#
#
#
#
#
fruits = {'apple', 'banana', 'orange'}
fruits_copy = fruits.copy()
print(fruits_copy)
#
#
#
#
#
fruits = {'apple', 'banana', 'orange'}
fruits2 = {'apple', 'melon', 'watermelon'}
fruits3 = fruits.difference(fruits2)
print(fruits3)
#
#
#
#
#
fruits = {'apple', 'banana', 'orange'}
fruits.discard('apple')
print(fruits)
#
#
#
fruits = {'apple', 'banana', 'orange'}
fruits.discard('watermelon')
print(fruits)
#
#
#
#
#
fruits = {'apple', 'banana', 'orange'}
fruits.remove('apple')
print(fruits)
#
#
#
#| error: true
fruits = {'apple', 'banana', 'orange'}
fruits.remove('watermelon')
print(fruits)
#
#
#
#
#
fruits = {'apple', 'banana', 'orange'}
fruits2 = {'apple', 'melon', 'watermelon'}
fruits3 = fruits.intersection(fruits2)
print(fruits3)
#
#
#
#
#
fruits = {'apple', 'banana', 'orange'}
fruits2 = {'melon', 'watermelon'}
print(fruits.isdisjoint(fruits2))
#
#
#
#
#
fruits = {'apple', 'banana', 'orange', 'watermelon'}
fruits2 = {'banana', 'orange'}
print(fruits2.issubset(fruits))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| code-fold: true
#| code-summary: "Рішення"

list_1 = [1, 5, 3]
list_2 = [2, 8]

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| code-fold: true
#| code-summary: "Рішення"

menu = {'White Chocolate Mocha', 'Americano', 'Flat White', 'Latte', 
        'Blueberry Muffin', 'Chocolate Chip Cookie'}
stop = {'White Chocolate Mocha', 'Blueberry Muffin'}

menu_today = menu - stop
# або
menu_today = menu.difference(stop)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| code-fold: true
#| code-summary: "Рішення"

my_set = {0, 10, 100}
to_delete = 0
my_set.discard(to_delete)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| code-fold: true
#| code-summary: "Рішення"

students = {'Крупін Владислав', 'Крашеніннікова Олександра', 'Михолап Мар\'яна', 'Дробина Юлія', 'Алексєєва Віталіна'}
new_student = 'Піщікова Катерина'
churn_student = 'Михолап Мар\'яна'
students.add(new_student)
students.discard(churn_student)
# або
# students.remove(churn_student)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| code-fold: true
#| code-summary: "Рішення"

da_students = {'Крупін Владислав', 'Крашеніннікова Олександра', "Михолап Мар'яна", 'Дробина Юлія'}
dv_students = {"Михолап Мар'яна", 'Дробина Юлія', 'Алексєєва Віталіна'}
students = da_students & dv_students
# або
students = da_students.intersection(dv_students)
# або
students = da_students - dv_students
#
#
#
#
#
#
#
#
#
#
my_frozenset = frozenset([1, 2, 3])
print(my_frozenset)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| code-fold: true
#| code-summary: "Рішення"

numbers_list = [1, 1, 5, 3, 3, 5]
numbers_list_ordered = sorted(numbers_list, reverse=True)
numbers_set = set(numbers_list)
numbers_set.add(max(numbers_list) + 1)
numbers_frozenset = frozenset(sorted(set(numbers_list))[1:]) 
#
#
#
#
#
#
#
#
#
#
#
#
fruits = ['apple', 'banana', 'orange']
print(len(fruits))
#
#
#
fruits = {'apple', 'banana', 'banana', 'apple'}
print(len(fruits))
#
#
#
#
#
fruits = ['apple', 'banana', 'orange']
print(max(fruits))
#
#
#
numbers = [5, 2, 8, 1, 9]
print(max(numbers))
#
#
#
my_set = {5, 2, 8, 1, 8}
print(max(my_set))
#
#
#
#
#
fruits = ['apple', 'banana', 'orange']
print(min(fruits))
#
#
#
numbers = [5, 2, 8, 1, 9]
print(min(numbers))
#
#
#
#
#
fruits = ['banana', 'orange', 'apple']
print(sorted(fruits))
#
#
#
numbers = [5, 2, 8, 1, 9]
print(sorted(numbers, reverse=True))
#
#
#
#
#
my_set = {1, 1, 2, 2}
print(sorted(my_set))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# від 0 до 4 з кроком 1
list(range(5))
#
#
#
# від 2 до 9 з кроком 2
list(range(2, 10, 2))
#
#
#
# від 10 до 2 з кроком 1
list(range(10, 1, -1))
#
#
#
#
#
#
#
#
#
#
#
#
#
#| code-fold: true
#| code-summary: "Рішення"

var_1 = list(range(-100, 101, 1))
var_2 = list(range(250, -1, -2))
var_3 = list(range(101, 200, 2))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| code-fold: true
#| code-summary: "Рішення"

a = 1
b = 3
result = sum(range(a, b + 1))
#
#
#
#
#
#
#
#
#
#
# збережемо список у змінну my_list_1
my_list_1 = [3, 1, 2]

# у змінну my_list_2 збережемо список my_list_1
my_list_2 = my_list_1

# змінимо список my_list_1
my_list_1.append(4)
my_list_1.sort()
my_list_1[0] = 100

# подивимося на обидва списки
print("Результат списку my_list_1:", my_list_1)
print("Результат списку my_list_2:", my_list_2)
#
#
#
#
#
#
#
# збережемо список у змінну my_list_1
my_list_1 = [3, 1, 2]

# у змінну my_list_2 збережемо список my_list_1 з методом copy()
my_list_2 = my_list_1.copy()

# змінимо список my_list_1
my_list_1.append(4)
my_list_1.sort()
my_list_1[0] = 100

# подивимося на обидва списки
print("Результат списку my_list_1:", my_list_1)
print("Результат списку my_list_2:", my_list_2)
#
#
#
#
#
my_list = [1, 2, 3, -2]

# так правильно
my_list_ordered = sorted(my_list) # функція sorted повертає новий список, не змінює список my_list
print("Результат списку my_list_ordered:", my_list_ordered)
print("Результат списку my_list:", my_list)
#
#
#
#| include: false

del my_list_ordered
#
#
#
# так неправильно
my_list_ordered = my_list.sort() # метод sort нічого не повертає, а лише змінює список my_list
print("Результат списку my_list_ordered:", my_list_ordered)
print("Результат списку my_list:", my_list)
#
#
#
#
#
#
#
#
#
#
#
#| error: true

# створимо кортеж
months = ('January', 'February', 'March', 'April', 'May',
           'June', 'July', 'August', 'September', 'October', 'November', 'December')

# спробуємо додати тринадцятий місяць
months[12] = 'Undecimber'

# або змінити другий місяць
months[1] = 'Лютий'
#
#
#
#
#
#
#
month_index = 0
month_name = months[month_index] 
print(month_name)
#
#
#
#
#
#
#
#
#
#
#
#
#| code-fold: true
#| code-summary: "Рішення"

days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
#
#
#
#
#
#
#
#
#
#
x = [1, 2, 3]
y = ['a', 'b', 'c']

# Використовуємо функцію zip() для об'єднання елементів із двох списків
result = zip(x, y)

# Перетворюємо результат на список
result_list = list(result)

print(result_list)
#
#
#
#
#
#
#
#
#
