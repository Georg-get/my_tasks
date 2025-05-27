### Условие задачи:
# Предложение — это список токенов, разделенных одним пробелом без начальных или конечных пробелов. Каждый токен — это либо положительное число,
# состоящее из цифр 0-9 без начальных нулей, либо слово, состоящее из строчных английских букв.
# Например, "a puppy has 2 eyes 4 legs"это предложение с семью токенами: "2"и "4"— числа, а другие токены, такие как "puppy"— слова.
# Дана строка s, представляющая предложение, и необходимо проверить, все ли числа в ней строго возрастают s слева направо
# (т. е., за исключением последнего числа, каждое число строго меньше числа справа от него в). s
# Вернитесь, true если это так, или false в противном случае.

# Example 1:
# Input: s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
# Output: true
# Explanation: The numbers in s are: 1, 3, 4, 6, 12.
# They are strictly increasing from left to right: 1 < 3 < 4 < 6 < 12.

# Example 2:
# Input: s = "hello world 5 x 5"
# Output: false
# Explanation: The numbers in s are: 5, 5. They are not strictly increasing.

# Example 3:
# Input: s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
# Output: false
# Explanation: The numbers in s are: 7, 51, 50, 60. They are not strictly increasing.

### Краткое условие:
# Вернитесь, true если это так, или false в противном случае.

# Полное объяснение решение задачи:
# 0) Создаем result со значением 0.
# 1) Проходимся циклом по массиву s,
# 1.1) Если i это цифра,
# 1.1.1) Если число i меньше или равно result, то верни False.
# 1.1.2) Иначе, result равно числу i.
# 2) Верни True.

# Сложность:
# 1) Время O(n)
# 2) Память O(m)

s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"

def areNumbersAscending(s):

    result = 0

    for i in s.split():

        if i.isdigit():

            if int(i) <= result:
                return False

            else:
                result = int(i)
    return True

areNumbersAscending(s)

assert areNumbersAscending(s="1 box has 3 blue 4 red 6 green and 12 yellow marbles") == True
assert areNumbersAscending(s="hello world 5 x 5") == False
assert areNumbersAscending(s="sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s") == False