### Условие задачи:
# Была протестирована новая клавиатура, в которой тестировщик нажимал последовательность nклавиш по одной за раз.
# Вам дана строка keysPressedдлины n, где keysPressed[i]была нажата клавиша в тестовой последовательности,
# и отсортированный список , где было время, когда клавиша была отпущена. Оба массива индексированы 0.
# Клавиша была нажата в момент , и каждая последующая клавиша была нажата в точное время, когда предыдущая клавиша была отпущена.ithreleaseTimesreleaseTimes[i]ith0th0
# Тестировщик хочет узнать клавишу нажатия, которая имела самую большую длительность . Нажатие клавиши имело длительность ,
# а нажатие клавиши имело длительность .ith releaseTimes[i] - releaseTimes[i - 1]0threleaseTimes[0]
# Обратите внимание, что одна и та же клавиша могла быть нажата несколько раз во время теста,
# и эти многократные нажатия одной и той же клавиши могли иметь разную продолжительность .
# Возвращает клавишу нажатия клавиши, которая имела наибольшую длительность.
# Если таких нажатий несколько, возвращает лексикографически наибольшую клавишу из нажатий клавиш.

# Example 1:
# Input: releaseTimes = [9,29,49,50], keysPressed = "cbcd"
# Output: "c"
# Explanation: The keypresses were as follows:
# Keypress for 'c' had a duration of 9 (pressed at time 0 and released at time 9).
# Keypress for 'b' had a duration of 29 - 9 = 20 (pressed at time 9 right after the release of the previous character and released at time 29).
# Keypress for 'c' had a duration of 49 - 29 = 20 (pressed at time 29 right after the release of the previous character and released at time 49).
# Keypress for 'd' had a duration of 50 - 49 = 1 (pressed at time 49 right after the release of the previous character and released at time 50).
# The longest of these was the keypress for 'b' and the second keypress for 'c', both with duration 20.
# 'c' is lexicographically larger than 'b', so the answer is 'c'.

# Example 2:
# Input: releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
# Output: "a"
# Explanation: The keypresses were as follows:
# Keypress for 's' had a duration of 12.
# Keypress for 'p' had a duration of 23 - 12 = 11.
# Keypress for 'u' had a duration of 36 - 23 = 13.
# Keypress for 'd' had a duration of 46 - 36 = 10.
# Keypress for 'a' had a duration of 62 - 46 = 16.
# The longest of these was the keypress for 'a' with duration 16.

### Краткое условие:
# Возвращает клавишу нажатия клавиши, которая имела наибольшую длительность.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь dict.
# 1) Проходимся циклом по диапазону от 0 до длины массива releaseTimes,
# 1.1) Если i равна 0, то ключ равно keysPressed[i] а значение releaseTimes[i] в словаре dict.
# 1.2) Если i НЕ равна 0, то releaseTime равно releaseTimes[i] - releaseTimes[i - 1],
# 1.2.1) Если keysPressed[i] есть в словаре dict и releaseTime > dict[keysPressed[i]], то dict[keysPressed[i]] = releaseTime
# 1.2.2) Если ключа keysPressed[i] нету в словаре dict , то dict[keysPressed[i]] = releaseTime.
# 2) Создаем переменную maxReleaseTime со значением максивального значние из словаря dict и пустую строку result.
# 3) Проходимя циклом по словарю dict, если значнее ключа i равно maxReleaseTime и j больше result, то result = j.
# 4) Верни строку result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

releaseTimes = [9, 29, 49, 50]
keysPressed = "cbcd"

def slowestKey(releaseTimes, keysPressed):
    dict = {}

    for i in range(len(releaseTimes)):
        if i == 0:
            dict[keysPressed[i]] = releaseTimes[i]
        else:
            releaseTime = releaseTimes[i] - releaseTimes[i - 1]

            if keysPressed[i] in dict and releaseTime > dict[keysPressed[i]]:
                dict[keysPressed[i]] = releaseTime
            elif keysPressed[i] not in dict:
                dict[keysPressed[i]] = releaseTime
    # {'c': 20, 'b': 20, 'd': 1}
    maxReleaseTime = max(dict.values()) # 20
    result = ""

    for j in dict:
        if dict[j] == maxReleaseTime and j > result:
            result = j
                
    return result

slowestKey(releaseTimes, keysPressed)

assert slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd") == "c"
assert slowestKey(releaseTimes=[12, 23, 36, 46, 62], keysPressed="spuda") == "a"