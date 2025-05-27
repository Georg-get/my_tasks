### Условие задачи:
# Вам дана строка, num представляющая большое целое число.
# Целое число является хорошим, если оно удовлетворяет следующим условиям:
# Это подстрока длиной num3.
# Он состоит только из одной уникальной цифры.
# Возвращает максимальное целое число в виде строки или пустую строку, ""если такого целого числа не существует.
# Примечание:
# Подстрока — это непрерывная последовательность символов внутри строки.
# Могут быть ведущие нули или num хорошее целое число.

# Example 1:
# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".

# Example 2:
# Input: num = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.

# Example 3:
# Input: num = "42352338"
# Output: ""
# Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

### Краткое условие:
# Надо найти в строке num три повторяющеся подряд числа и вернуть их , если в строке num нету таких чисел вернуть пустую строку.

# Алгоритм решение задачи:
# 0) Создаем словарь dict с ключом повсторяюмся трех чисел и с таким же значением.
# 1) Проходимся циклом по словарю dict, если ключ i есть в строке num, то верни i.
# 2) Верни пустую строку.

# Сложность:
# 1) Время O(n) (n*m)
# 2) Память O(1)

num = "6777133339"

def largestGoodInteger(num):
    dict = {'999': '999', '888': '888', '777': '777', '666': '666', '555': '555', '444': '444', '333': '333',
            '222': '222', '111': '111', '000': '000'}

    for i in dict:
        if dict[i] in num:
            return i

    return ""

largestGoodInteger(num)

assert largestGoodInteger(num="6777133339") == "777"
assert largestGoodInteger(num="2300019") == "000"
assert largestGoodInteger(num="42352338") == ""