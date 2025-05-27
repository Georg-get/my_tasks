### Условие задачи:
# Вам дан массив символов letters, отсортированный в неубывающем порядке, и символ target.
# В файле, есть как минимум два разных персонажа letters.
# Возвращает наименьший символ, letters который лексикографически больше target.
# Если такого символа не существует, верните первый символ в letters.

# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

# Example 3:
# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

### Краткое условие:
# Возвращает наименьший символ, letters который лексикографически больше target.
# Если такого символа не существует, верните первый символ в letters.

# Алгоритм решение задачи:
# 0) Определить границы поиска.(left и right) и пройтись циклом.
# 1) Найти середину
# 2) Если элемент в середине массива letters больше target, то двигайся в права.
# 2.1) Если нет двигайся в лево.
# 3) Если элемент в массиве letters больше target, верни этот элемент.
# 3.1) Если нет верни первый элемент массива letters.

# Сложность:
# 1) памяти O(n log n)
# 2) времени O(1)

letters = ["c", "f", "j"]
target = "a"

def nextGreatestLetter(letters, target):
    left = 0
    right = len(letters) - 1  # 2

    while left < right:
        mid = (left + right) // 2

        if letters[mid] > target:
            right -= 1
        else:
            left += 1

    if letters[left] > target:
        return letters[left]
    else:
        return letters[0]

nextGreatestLetter(letters, target)

assert nextGreatestLetter(letters=["c", "f", "j"], target="a") == "c"
assert nextGreatestLetter(letters=["c", "f", "j"], target="c") == "f"
assert nextGreatestLetter(letters=["x", "x", "y", "y"], target="z") == "x"