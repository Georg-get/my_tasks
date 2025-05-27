### Условие задачи:
# Вам дан номер телефона в виде строки number. numberсостоит из цифр, пробелов ' 'и/или тире '-'.
# Вы хотите переформатировать номер телефона определенным образом. Во-первых, удалите все пробелы и тире.
# Затем сгруппируйте цифры слева направо в блоки длиной 3, пока не останется 4 или меньше цифр.
# Конечные цифры затем группируются следующим образом:
# 2 цифры: один блок длиной 2.
# 3 цифры: один блок длиной 3.
# 4 цифры: два блока длиной по 2 каждый.
# Затем блоки соединяются тире. Обратите внимание,
# что процесс переформатирования никогда не должен создавать блоки длиной 1 и создавать максимум два блока длиной 2.
# Верните номер телефона после форматирования.

# Example 1:
# Input: number = "1-23-45 6"
# Output: "123-456"
# Explanation: The digits are "123456".
# Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
# Step 2: There are 3 digits remaining, so put them in a single block of length 3. The 2nd block is "456".
# Joining the blocks gives "123-456".

# Example 2:
# Input: number = "123 4-567"
# Output: "123-45-67"
# Explanation: The digits are "1234567".
# Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
# Step 2: There are 4 digits left, so split them into two blocks of length 2. The blocks are "45" and "67".
# Joining the blocks gives "123-45-67".

# Example 3:
# Input: number = "123 4-5678"
# Output: "123-456-78"
# Explanation: The digits are "12345678".
# Step 1: The 1st block is "123".
# Step 2: The 2nd block is "456".
# Step 3: There are 2 digits left, so put them in a single block of length 2. The 3rd block is "78".
# Joining the blocks gives "123-456-78".

### Краткое условие:
# Верните номер телефона после форматирования.

# Алгоритм решение задачи:
# 0) Создаем строку numbers со значением строки number без - и пробелов, и пустую строку result.
# 1) Проходимся циклом ваилд пока длина строки numbers не станет больше 4,
# 1.1) добавляем в строку result буквы с индексами от 0 до 3
# 1.2) добавляем в строку number буквы с индексами от 3 до конца.
# 2) Если размер строки number больше 3, то увеличь строку result буквы с индексами от 3 до конца.
# 3) Если размер строки number НЕ больше 3, то увечичь строку result на буквы с индексами от 0 до 2,
# и увечичь строку number на буквы с индексами от 2 до конца
# 3.1) Если длина строки number больше 0, то увечичь строку result на "-" + строка number.
# 4) Верни строку result

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

number = "1-23-45 6"

def reformatNumber(number):
    number = number.replace("-", "").replace(" ", "")
    result = ''

    while len(number) > 4:
        result += number[0:3] + "-"
        number = number[3:]
    # result = 123-
    # number = 456
    if len(number) == 3:
        result += number[0:3]

    else:
        result += number[0:2]
        number = number[2:]

        if len(number) > 0:
            result += "-" + number

    return result

reformatNumber(number)

assert reformatNumber(number="1-23-45 6") == "123-456"
assert reformatNumber(number="123 4-567") == "123-45-67"
assert reformatNumber(number="123 4-5678") == "123-456-78"