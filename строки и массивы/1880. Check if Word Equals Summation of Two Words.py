### Условие задачи:
# Буквенное значение буквы — это ее позиция в алфавите, начиная с 0 (т.е. 'a' -> 0, 'b' -> 1, 'c' -> 2и т. д.).
# Числовое значение некоторой строки строчных английских букв s представляет собой объединение буквенных значений каждой буквы в s,
# которое затем преобразуется в целое число.
# Например, если s = "acb" мы объединяем буквенное значение каждой буквы, в результате чего получаем "021".
# После преобразования получим 21.
# Вам даны три строки firstWord, secondWordи targetWord, каждая из которых состоит из строчных букв английского алфавита 'a'до 'j' включительно .
# Возврат , true если сумма числовых значенийfirstWord и secondWordравна числовому значениюtargetWord или в противном случае false.

# Example 1:
# Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
# Output: true
# Explanation:
# The numerical value of firstWord is "acb" -> "021" -> 21.
# The numerical value of secondWord is "cba" -> "210" -> 210.
# The numerical value of targetWord is "cdb" -> "231" -> 231.
# We return true because 21 + 210 == 231.

# Example 2:
# Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
# Output: false
# Explanation:
# The numerical value of firstWord is "aaa" -> "000" -> 0.
# The numerical value of secondWord is "a" -> "0" -> 0.
# The numerical value of targetWord is "aab" -> "001" -> 1.
# We return false because 0 + 0 != 1.

# Example 3:
# Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
# Output: true
# Explanation:
# The numerical value of firstWord is "aaa" -> "000" -> 0.
# The numerical value of secondWord is "a" -> "0" -> 0.
# The numerical value of targetWord is "aaaa" -> "0000" -> 0.
# We return true because 0 + 0 == 0.

### Краткое условие:
# Если сумма все индексов всех букв встроках firstWord и secondWord равна сумме все индексов всех букв в строке targetWord,
# то верни True, иначе False.

# Алгоритм решение задачи:
# 0) Создаем словарь с англискими буквами от a до j, где буква это ключ а значение это индекс в алфовите (который начинается с 0),
# 0.1) и пустые строки resultFirstWord,resultSecondWord,resultTargetWord.
# 1) Проходимся циклом по строке firstWord, увеличиваем строку resultFirstWord на dict[i].
# 2) Проходимся циклом по строке secondWord, увеличиваем строку resultSecondWord на dict[j].
# 3) Проходимся циклом по строке targetWord, увеличиваем строку resultTargetWord на dict[k].
# 4) Если сложить числа resultFirstWord и resultSecondWord, и они будут равны числу resultTargetWord, то вернуть True.
# 5) Если сложить числа resultFirstWord и resultSecondWord, и они будут НЕ равны числу resultTargetWord, то вернуть False.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"

def isSumEqual(firstWord, secondWord, targetWord):
    dict = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'}
    resultFirstWord = ""
    resultSecondWord = ""
    resultTargetWord = ""

    for i in firstWord:
        resultFirstWord += dict[i]

    for j in secondWord:
        resultSecondWord += dict[j]

    for k in targetWord:
        resultTargetWord += dict[k]

    if int(resultFirstWord) + int(resultSecondWord) == int(resultTargetWord):
        return True
    else:
        return False

isSumEqual(firstWord, secondWord, targetWord)

assert isSumEqual(firstWord="acb", secondWord="cba", targetWord="cdb") == True
assert isSumEqual(firstWord="aaa", secondWord="a", targetWord="aab") == False
assert isSumEqual(firstWord="aaa", secondWord="a", targetWord="aaaa") == True