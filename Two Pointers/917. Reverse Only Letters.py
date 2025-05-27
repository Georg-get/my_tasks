### Условие задачи:
# Учитывая строку s, переверните строку в соответствии со следующими правилами:
# Все символы, кроме английских букв, остаются на прежнем месте.
# Все английские буквы (строчные или прописные) следует поменять местами.
# Вернитесь s после его изменения.

# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"

# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

# Example 3:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

### Краткое условие:
# Вернуть перевернутую строку s и оставить символы на месте.

# Алгоритм решение задачи:
# 0) Создаем переменные left со значенеим 0 и right со значением длины строки s -1, и массив result со значенеиме букв из строки s.
# 1) Проходимся циклома ваилд пока left не станет меньше right,
# 1.1) Если левый указатель попал на символе, то увеличь занчением переменной left на 1.
# 1.2) Если правый указатель попал на символе, то уменьши занчением переменной right на 1.
# 1.3) Иначе, поменяй метсами буквы которые находится левый и правый указатель, и увеличь занчением переменной left на 1,
# и уменьши значением переменной right на 1.
# 2) Верни строку из массива result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "ab-cd"

def reverseOnlyLetters(s):
    left = 0
    right = len(s) - 1
    result = list(s)  # ['a', 'b', '-', 'c', 'd']

    while left < right:

        if not result[left].isalpha(): # если левый указачеть попал на символ !!!
            left += 1
        elif not result[right].isalpha(): # если правый указачеть попал на символ !!!
            right -= 1
        else:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
    # ['d', 'c', '-', 'b', 'a']
    return "".join(result)  # dc-ba

reverseOnlyLetters(s)

assert reverseOnlyLetters(s="ab-cd") == "dc-ba"
assert reverseOnlyLetters(s="a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
assert reverseOnlyLetters(s="Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"