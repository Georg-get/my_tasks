### Условие задачи:
# Учитывая строку licensePlate и массив строк words, найдите самое короткое завершающее слово в words.
# Завершающее слово – это слово, содержащее все буквыlicensePlate . Игнорируйте цифры и пробелы в licensePlateи рассматривайте буквы как регистронезависимые .
# Если буква встречается в слове более одного раза licensePlate, то она должна встречаться в слове столько же или более раз.
# Например, если licensePlate = "aBc 12c", то он содержит буквы 'a', 'b'(без учета регистра) и 'c'дважды.
# Возможные завершающие слова: "abccdef", "caaacab", и "cbca".
# Вернуть самое короткое завершающее слово в формате words. Гарантировано, что ответ существует.
# Если существует несколько кратчайших завершающих слов, верните первое , которое встречается в words.

# Example 1:
# Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
# Output: "steps"
# Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
# "step" contains 't' and 'p', but only contains 1 's'.
# "steps" contains 't', 'p', and both 's' characters.
# "stripe" is missing an 's'.
# "stepple" is missing an 's'.
# Since "steps" is the only word containing all the letters, that is the answer.

# Example 2:
# Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
# Output: "pest"
# Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.

### Краткое условие:
# Надо вернуть слова из массива words которое можно собрать из букв строки licensePlate
# (Убирая пробелы и преобразование больших букв в маленькие).

# Алгоритм решение задачи:
# 0) Создаем пустую строку processedStringLicensePlate и пустые словари dict и dictProcessedStringLicensePlate.
# 1) Проходим циклом по строке, избавляемся от пробелов и преобразовываем большие буквы в маленькие и
# записывет результат в переменную processedStringLicensePlate.
# 2) Преврашаем строку processedStringLicensePlate в словарь dictProcessedStringLicensePlate,
# где ключ это буква из строки значение сколько раз эта буква повторяется.
# 3) Проходимся циклом по диапазону длины массив words,
# 3.1) Создаем переменную flag равен True.
# 3.2) Проходимся циклом по словарю dictProcessedStringLicensePlate,
# 3.2.1) Если элемент массива j есть в словаре dictProcessedStringLicensePlate меньше count, то flag равен False.
# 3.3) Если переменная flag равена True, то добавь ключ слова из массива words со значением длины слова.
# 4) Верни ключ с самым маленьким значением из словаря dict.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]

def shortestCompletingWord(licensePlate, words):
    processedStringLicensePlate = ''
    dict = {}
    dictProcessedStringLicensePlate = {}

    for i in licensePlate.lower():
        if i != ' ' and not i.isdigit():
            processedStringLicensePlate += i
    # spst
    for i in processedStringLicensePlate:
        if i in dictProcessedStringLicensePlate:
            dictProcessedStringLicensePlate[i] += 1
        else:
            dictProcessedStringLicensePlate[i] = 1
    # {'s': 2, 'p': 1, 't': 1}
    for j in range(len(words)):
        flag = True
        for char, count in dictProcessedStringLicensePlate.items():
            if words[j].count(char) < count:
                flag = False

        if flag == True:
            dict[words[j]] = len(words[j])
    # {'steps': 5}
    return min(dict, key=dict.get)

shortestCompletingWord(licensePlate, words)

assert shortestCompletingWord(licensePlate="1s3 PSt", words=["step", "steps", "stripe", "stepple"]) == "steps"
assert shortestCompletingWord(licensePlate="1s3 456", words=["looks", "pest", "stew", "show"]) == "pest"