### Условие задачи:
# Учитывая две строки sи t, возвращайте true значение, если они равны, когда обе вводятся в пустые текстовые редакторы .
# '#'означает символ возврата. Обратите внимание, что после возврата пустого текста текст останется пустым.

# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

### Краткое условие:
# Необходимо вернуть true, если строки s и t равны после удаление букву перед символом '#' и символа '#'.
# Иначе вернуть false.

# Краткое объяснение решение задачи:
# 1. Пишем функцию processString которая обрабатывает строку, игнорируя символы # и удаляя предыдущие символы.
# 2. Если две строки s и t равны после обработки функцией processString, то возвращает True, иначе — False.

# Полное объяснение решение задачи:
# 0) Создать функцию processString
# 1) В функции processString создать пустой массив (stack)
# 2) Пройтись for по элементам строки
# 2.1) если элемент строки не равен '#' то довавить этот элемент в стек, stack.append(i)
# 2.2) если элемент строки '#' , то удаляем в стеке последний элемент, stack.pop()
# 3) Сравниваем две строки

# Сложность:
# 1) Время O(n + m)
# 2) Память O(n + m)

s = "a#c"
t = "b"

def backspaceCompare(s, t):
    def processString(string):
        stack = []

        for i in string:
            if i != '#':
                stack.append(i)
            elif len(stack) > 0:
                stack.pop()

        return stack

        #       ['c']        ['b']
    if processString(s) == processString(t):
        return True
    else:
        return False
    # return processString(s) == processString(t)

backspaceCompare(s, t)

assert backspaceCompare(s="ab#c", t="ad#c") == True
assert backspaceCompare(s="ab##", t="c#d#") == True  # Тест с разными строками с символами удаления
assert backspaceCompare(s="a#c", t="b") == False  # Тест с различными символами и удалениями
# Доп юнитесты для проверки некоторых условий:
assert backspaceCompare(s="", t="") == True  # Тест с пустыми строками
assert backspaceCompare(s="a#", t="") == True  # Тест с одной пустой и одной непустой строкой
assert backspaceCompare(s="###", t="") == True  # Тест с множественными удалениями в обеих строках