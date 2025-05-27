### Условие задачи:
# У нас есть два специальных символа:
# Первый символ может быть представлен одним битом 0.
# Второй символ может быть представлен двумя битами (10 или 11).
# Для заданного двоичного массива bits, заканчивающегося на 0, вернуть значение, true
# если последний символ должен быть однобитовым.

# Example 1:
# Input: bits = [1,0,0]
# Output: true
# Explanation: The only way to decode it is two-bit character and one-bit character.
# So the last character is one-bit character.

# Example 2:
# Input: bits = [1,1,1,0]
# Output: false
# Explanation: The only way to decode it is two-bit character and two-bit character.
# So the last character is not one-bit character.

### Краткое условие:
# Для заданного двоичного массива bits, заканчивающегося на 0, вернуть значение, true
# если последний символ должен быть однобитовым.

# Полное объяснение решение задачи:
# 0) Преоборазовывваем массив bits в строку bitString.
# 1) В строке simplifiedString заменяем все '11' и '10' на 'x'.
# 2) Если если в строке simplifiedString последний символ 0, то вернуть True.
# 3) Иначе, верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

bits = [1, 1, 1, 0]

def isOneBitCharacter(bits):
    # Преобразуем список бит в строку
    bitString = ''.join(map(str, bits))
    # 1110
    # Заменяем все '11' и '10' на 'x'
    simplifiedString = bitString.replace('11', 'x').replace('10', 'x')
    # xx
    # Проверяем, является ли последний символ '0'
    if simplifiedString[-1] == '0':
        return True
    else:
        return False

isOneBitCharacter(bits)

assert isOneBitCharacter(bits=[1, 0, 0]) == True
assert isOneBitCharacter(bits=[1, 1, 1, 0]) == False