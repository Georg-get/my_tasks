### Условие задачи:
# Ваш друг печатает свое nameна клавиатуре. Иногда при вводе символа cклавиша может быть долго нажата , и символ будет набран 1 или более раз.
# Вы изучаете typed символы клавиатуры. Верните, True если возможно, что это было имя вашего друга,
# при длительном нажатии некоторых символов (возможно, ни одного).

# Example 1:
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanarighton: 'a' and 'e' in 'alex' were long pressed.

# Example 2:
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanarighton: 'e' must have been pressed twice, but it was not in the typed output.

### Краткое условие:
# Если при удаление всех дубликатов букв из строки typed получиться строка name то вернуть true, иначе false.

# Краткое объяснение решение задачи:
# 1. Устанавливаем левый указатель в начало строки name и правый указатель в начало строки typed
# 2. Пока левый указатель не дойдет до конца строки name и правый указаетль не дойдет до конца строки typed:
#    - Если текущий символ в typed совпадает с текущим символом в name, оба указателя увеличиваются.
#    - Если текущий символ в typed равен предыдущему символу в name,
#    только указатель right увеличивается (это означает длительное нажатие).
#    - Если ни одно из условий не выполняется, функция возвращает False.
# 3. Проверяем достигли ли оба указателя конца своих строк.
# Если да, возвращается True; если нет, возвращается False.


# Полное объяснение решение задачи:
# 0) Создаем переменные: left со значением 0 и right со значением 0.
# 1) Проходимся циклом ваилд пока left не станет меньше или ранвно чем длина строки name и пока right не станет меньше или ранвно чем длина строки typed,
# 1.1) Если left не станет меньше или ранвно чем длина строки name и буква где установлен правый указатель в строке typed равен буква где установлен левый указатель в строке name,
# 1.1.1) Увеличь значением переменной right на 1 и увеличь значением переменной left на 1.
# 1.2) Если буква где установлен правый указатель в строке typed равна букве где установлен левый указатель -1 в строке name и left НЕ равно 0, увеличь значением переменной right на 1.
# 1.3) Иначе, вернуть False.
# 2) Вернуть left равную длине строки name и right равно длине строки typed.

# Сложность:
# 1) Время O(m) (n)
# 2) Память O(1) (n)

name = "alex"
typed = "aaleex"

def isLongPressedName(name, typed):
    left = 0
    right = 0

    while left <= len(name) and right < len(typed): #  left <= len(name) Зашита от 5 юнитеста !!!

        if left < len(name) and name[left] == typed[right]:
            right += 1
            left += 1

        elif name[left - 1] == typed[right] and left != 0:  # and left != 0: это от 4 юнитеста !!!
            right += 1

        else:           #  Зашита от 2 юнитеста !!!
           return False

    if left == len(name) and right == len(typed):  # Защита от 3 юнитеста !!!
        return True
    else:
        return False
    # return left == len(name) and right == len(typed)

isLongPressedName(name, typed)

assert isLongPressedName(name="alex", typed="aaleex") == True
assert isLongPressedName(name="saeed", typed="ssaaedd") == False #  else: return False
assert isLongPressedName(name="alexd", typed="ale") == False  # left == len(name) and right == len(typed):
assert isLongPressedName(name="zlexya", typed="aazlllllllllllllleexxxxxxxxxxxxxxxya") == False  # and left != 0:
assert isLongPressedName(name="vtkgn", typed="vttkgnn") == True  # while left <= len(name) and right < len(typed):
# Доп юнитесты для проверки некоторых условий:
assert isLongPressedName(name="leelee", typed="lleeelee") == True  # Полное совпадение
assert isLongPressedName(name="la", typed="aaaaaaaaaaaaa") == False  # Длительное нажатие в начале
assert isLongPressedName(name="", typed="") == True  # Пустая строка
assert isLongPressedName(name="aa", typed="aaa") == True  # Имя с повторяющимися символами
assert isLongPressedName(name="abc", typed="abcccc") == True  # Длительное нажатие в конце