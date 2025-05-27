### Условие задачи:
# Фраза является палиндромом, если после преобразования всех прописных букв в строчные и
# удаления всех не буквенно-цифровых символов она читается одинаково и вперед, и назад.
# Буквенно-цифровые символы включают буквы и цифры.
# Дана строка s, возвращает значение true, если это палиндром или false нет.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

### Краткое условие:
# Если предложение в строке s является палиндром то возвращаем true. Иначе возвращаем false.

# Краткое объяснение решение задачи:
# 1. Заменяем большие буквы на маленькие и убираем знаки припенания и пробелы в строке s.
# 2. Устанавливаем левый указатель в начало строки s, а правый указатель в конец строки s,
# если буква где установлен левый указатель не равна букве где установлен правый указатель то вернуть False.
# 3. Если левый и правый указатель пересеклись верни True.

# Полное объяснение решение задачи:
# 0) Избавляемся в строке s от:
# пробелов, знаков препинания
# и большие буквы переделать в маленькие буквы.
# 0.1) Создаем переменные: left со значением 0 и right со значением длины строки s-1.
# 1) Проходимся циклом ваилд пока left не станет меньше чем right,
# 1.1) Если буква на которой установлен левый указатель НЕ равна букве на которой установлен правый указатель, то верни False.
# 1.2) Иначе, увеличь левый указатель на 1 и уменьши правый указатель на 1.
# 2) Верни True

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

# import re

s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    # s = ''.join(char.lower() for char in s if
    #             char.isalnum()) # Удаление пробелов, знаков препинания и преобразование в нижний регистр

    # s = re.sub('[^A-Za-z0-9]+', '', s.lower()) # тоже самый эффект но через либу re

    string = ""
    for i in s:  # избовляемся от пробелов, знаков препинания
        if i.isalnum():
            string += i.lower()  # меняем большие буквы на маленькие если они попадутся нам
    s = string  # amanaplanacanalpanama

    left = 0
    right = len(s) - 1

    while left < right:  # пока левый и правый указатель не пересекутся
        if s[left] != s[right]:  # если буква в левом и правом указателе разные, то вернуть False !!!
            return False

        else:
            left += 1
            right -= 1

    return True

isPalindrome(s)

assert isPalindrome(s="A man, a plan, a canal: Panama") == True
assert isPalindrome(s="race a car") == False
assert isPalindrome(s="") == True  # Тест с пустой строкой
# Доп юнитесты для проверки некоторых условий:
assert isPalindrome(s="12321") == True  # Тест с палиндромом, содержащим цифры и буквы
assert isPalindrome(s="No 'x' in Nixon") == True  # Тест с игнорированием регистра и специальных символов
assert isPalindrome(s="aa") == True  # Тест с палиндромом, состоящим только из символов
assert isPalindrome(s=" ") == True  # Тест с пробелами и символами