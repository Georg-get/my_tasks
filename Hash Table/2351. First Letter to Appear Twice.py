### Условие задачи:
# Учитывая строку s, состоящую из строчных английских букв, верните первую букву, которая встретится дважды.
# Примечание:
# Буква a появляется дважды перед другой буквой, b если второе появление a находится перед вторым появлением b.
# s будет содержать хотя бы одну букву, которая встречается дважды.

# Example 1:
# Input: s = "abccbaacz"
# Output: "c"
# Explanation:
# The letter 'a' appears on the indexes 0, 5 and 6.
# The letter 'b' appears on the indexes 1 and 4.
# The letter 'c' appears on the indexes 2, 3 and 7.
# The letter 'z' appears on the index 8.
# The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.

# Example 2:
# Input: s = "abcdd"
# Output: "d"
# Explanation:
# The only letter that appears twice is 'd' so we return 'd'.

### Краткое условие:
# Вернуть букву которая раньше всего повтаряется в строке s.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по строке s.
# 1.1) Если i есть в словаре dict, то вернуть i.
# 1.2) Если i НЕТу в словаре dict, то добавить i как ключ со значением 0 в словарь dict.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "abccbaacz"

def repeatedCharacter(s):
    dict = {}

    for i in s:
        if i in dict:
            # {'a': 0, 'b': 0, 'c': 0} - тут "c" раньше всех повторилось в строке s
            return i # c
        else:
            dict[i] = 0

repeatedCharacter(s)

assert repeatedCharacter(s="abccbaacz") == "c"
assert repeatedCharacter(s="abcdd") == "d"