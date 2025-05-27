### Условие задачи:
# n В компании есть сотрудники, пронумерованные от 0 до n - 1. Каждый сотрудник i отработал hours[i] часов в компании.
# Компания требует от каждого сотрудника отработать не менее target часов.
# Вам дан индексированный начиная с 0 массив неотрицательных целых чисел hours длины n и неотрицательное целое число target.
# Верните целое число, обозначающее количество сотрудников, отработавших не менее target часов.

# Example 1:
# Input: hours = [0,1,2,3,4], target = 2
# Output: 3
# Explanation: The company wants each employee to work for at least 2 hours.
# - Employee 0 worked for 0 hours and didn't meet the target.
# - Employee 1 worked for 1 hours and didn't meet the target.
# - Employee 2 worked for 2 hours and met the target.
# - Employee 3 worked for 3 hours and met the target.
# - Employee 4 worked for 4 hours and met the target.
# There are 3 employees who met the target.

# Example 2:
# Input: hours = [5,1,4,2,2], target = 6
# Output: 0
# Explanation: The company wants each employee to work for at least 6 hours.
# There are 0 employees who met the target.

### Краткое условие:
# Надо вернуть колличество чисел больше или равно target из массив hours.

# Алгоритм решение задачи:
# 0) Создаем переменную count со значением 0.
# 1) Проходимся циклом по массиву hours,
# 1.1) Если i больше или равно target, то увеличь count на 1.
# 2) Верни count.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

hours = [0, 1, 2, 3, 4]
target = 2

def numberOfEmployeesWhoMetTarget(hours, target):
    count = 0

    for i in hours:
        if i >= target:
            count += 1

    return count

numberOfEmployeesWhoMetTarget(hours, target)

assert numberOfEmployeesWhoMetTarget(hours=[0, 1, 2, 3, 4], target=2) == 3
assert numberOfEmployeesWhoMetTarget(hours=[5, 1, 4, 2, 2], target=6) == 0