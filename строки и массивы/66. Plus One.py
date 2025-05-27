### Условие задачи:
# Вам дано большое целое число, представленное в виде массива целых чисел digits, где каждая цифра digits[i]— это цифра целого числа.
# Цифры упорядочены от наиболее значимых к наименее значимым слева направо.
# Большое целое число не содержит начальных '.ith0
# Увеличьте большое целое число на единицу и верните полученный массив цифр.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

### Краткое условие:
# Увеличьте большое целое число на единицу и верните полученный массив цифр.

# Полное объяснение решение задачи:
# 0) Создаем массив result,
# 1) Преобразовываем массив digits в число number и увеличисваем число number на 1.
# 2) Проходимся циклом по строке числа number,
# 2.1) В массив result добавляем число i.
# 3) Вернуть массив result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

digits = [1, 2, 3]

def plusOne(digits):

    result = []
    number = int(''.join(map(str, digits)))
    number += 1

    for i in str(number):
        result.append(int(i))

    return result

plusOne(digits)

assert plusOne(digits=[1, 2, 3]) == [1, 2, 4]
assert plusOne(digits=[4, 3, 2, 1]) == [4, 3, 2, 2]
assert plusOne(digits=[9]) == [1, 0]
