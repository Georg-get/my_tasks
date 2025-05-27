### Условие задачи:
# Вам даны строка s и целочисленный массив indices одинаковой длины.
# Строка s будет перетасована таким образом, что символ в позиции переместится в перетасованную строку.ithindices[i]
# Верните перетасованную строку.

# Example 1:
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

# Example 2:
# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.

### Краткое условие:
# Вернуть перетасованную строку. В массиве indices находится индексы буквы которые надо перетасовать, а в строке s буквы.

# Алгоритм решение задачи:
# 0) Создаем словарь dict и пустую строку result.
# 1) Проходимся циклом по диапазону длины стороки s,
# 1.1) Добавляем в словарь dict ключ со значением из массива indices со значением буквый из строки s.
# 2) Проходимся циклом по отсортированым ключам в словаре dict,
# 2.1) Увеличиваем переменную result на значение ключа из словаря dict.
# 3) Вернуть строку result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

def restoreString(s, indices):
    dict = {}
    result = ''

    for i in range(len(s)):
        dict[indices[i]] = s[i]
    # {4: 'c', 5: 'o', 6: 'd', 7: 'e', 0: 'l', 2: 'e', 1: 'e', 3: 't'}
    for i in sorted(dict.keys()): # [0, 1, 2, 3, 4, 5, 6, 7]
        result += dict[i]

    return result # leetcode

restoreString(s, indices)

assert restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]) == "leetcode"
assert restoreString(s="abc", indices=[0, 1, 2]) == "abc"