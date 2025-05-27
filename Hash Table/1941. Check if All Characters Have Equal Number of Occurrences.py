### Условие задачи:
# Учитывая строку s, верните true, если s это хорошая строка, или false в противном случае.
# Строка s является хорошей, если все входящие в нее символы s
# имеют одинаковое количество вхождений (т. е. одинаковую частоту).

# Example 1:
# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

# Example 2:
# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

### Краткое условие:
# Вернуть true если количество совпадающих букв в строке равна между собой, false если одна буква больше повторяется.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Пройтись циклом по строке s,
# 1.1) Если i есть в словаре dict, то увеличь значение этого ключа на 1.
# 1.2) Если i НЕТу в словаре dict, то добавь i как ключ со значением 1 в словарь dict.
# 2) Если длина уникальных значений словаря dict ровна 1, то верни True.
# 3) Верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "aaabb"

def areOccurrencesEqual(s):
    dict = {}

    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # {'a': 3, 'b': 2}
    #           2
    if len(set(dict.values())) == 1:  # Если длина уникальных значений словаря dict =1
        return True
    else:
        return False

areOccurrencesEqual(s)

assert areOccurrencesEqual(s="abacbc") == True
assert areOccurrencesEqual(s="aaabb") == False