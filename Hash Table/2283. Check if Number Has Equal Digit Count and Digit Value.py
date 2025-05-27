### Условие задачи:
# Вам дана строка длины с нулевым индексом, состоящая из цифр.numn
# Возврат true, если для каждого индекса i в диапазоне 0 <= i < n цифра i встречается num[i] раз в num,
# в противном случае возврат false.

# Example 1:
# Input: num = "1210"
# Output: true
# Explanation:
# num[0] = '1'. The digit 0 occurs once in num.
# num[1] = '2'. The digit 1 occurs twice in num.
# num[2] = '1'. The digit 2 occurs once in num.
# num[3] = '0'. The digit 3 occurs zero times in num.
# The condition holds true for every index in "1210", so return true.

# Example 2:
# Input: num = "030"
# Output: false
# Explanation:
# num[0] = '0'. The digit 0 should occur zero times, but actually occurs twice in num.
# num[1] = '3'. The digit 1 should occur three times, but actually occurs zero times in num.
# num[2] = '0'. The digit 2 occurs zero times in num.
# The indices 0 and 1 both violate the condition, so return false.

### Краткое условие:
# Вернуть true, если все ключи идут по возврастанию, false по убыванию.

# Алгоритм решение задачи:
# 0) Создаем переменную lenNum со значением длины строки num и словарь dict с ключами от 0 до 9 со значениеями 0.
# 1) Проходимся циклом по строке num,
# 1.1) Если ключ i есть в словаре dict, то увеличь значение ключа i на 1.
# 2) Проходимся циклом по диапазону длины строки num,
# 2.1) Если ключ не равен значению, вернуть False.
# 3) Вернуть True.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

num = "1210"

def digitCount(num):
    dict = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}

    for i in num:
        if i in dict:
            dict[i] += 1
    # {'0': 1, '1': 2, '2': 1, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for j in range(len(num)):
        if int(num[j]) != dict[str(j)]:
            return False
    # дошли до конца строки и значение ключа из словаря dict совпали со строкой num !!!
    return True

digitCount(num)

assert digitCount(num="1210") == True
assert digitCount(num="030") == False