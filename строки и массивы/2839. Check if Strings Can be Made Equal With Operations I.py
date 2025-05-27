### Условие задачи:
# Вам даны две строки s1 и s2, обе длиной 4, состоящие из строчных английских букв.
# Вы можете применить следующую операцию к любой из двух строк любое количество раз:
# Выберите любые два индекса i и j такие, что j - i = 2, затем поменяйте местами два символа в этих индексах в строке.
# Верните true, если вы можете сделать строки s1 и s2 равными, false в противном случае.

# Example 1:
# Input: s1 = "abcd", s2 = "cdab"
# Output: true
# Explanation: We can do the following operations on s1:
# - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
# - Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.

# Example 2:
# Input: s1 = "abcd", s2 = "dacb"
# Output: false
# Explanation: It is not possible to make the two strings equal.

### Краткое условие:
# Верните true, если вы можете сделать строки s1 и s2 равными, false в противном случае.

# Алгоритм решение задачи:
# 0) Создаем левый и правый указатель.
# 1) Проходимся циклом ваилд пока правый указатель не дойдет до конца строки s1,
# 1.1) Если (левый указатель в строке s1 равен правому указателю в строке s2 и правый указатель в строке s1 равен левому указателю в строке s2)
# или левый указатель в строке s1 равен левый указателю в строке s1 и правому указатель в строке s1 равен правому указателю в строке s2,
# 1.2) То смести на +1 оба указателя.
# 1.3) Иначе, верни False.
# 2) Верни True.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

s1 = "abcd"
s2 = "cdab"

def canBeEqual(s1, s2):
    left = 0
    right = 2

    while right < len(s1):

        if (s1[left] == s2[right] and s1[right] == s2[left]) or (s1[left] == s2[left] and s1[right] == s2[right]):
            left += 1
            right += 1

        else:
            return False

    return True

canBeEqual(s1, s2)

assert canBeEqual(s1="abcd", s2="cdab") == True
assert canBeEqual(s1="abcd", s2="dacb") == False