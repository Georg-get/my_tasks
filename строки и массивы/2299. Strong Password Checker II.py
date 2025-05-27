### Условие задачи:
# Пароль считается надежным, если он удовлетворяет всем следующим критериям:
# В нем есть как минимум 8 символы.
# Он содержит как минимум одну строчную букву.
# Он содержит как минимум одну заглавную букву.
# Он содержит как минимум одну цифру.
# Он содержит по крайней мере один специальный символ. Специальные символы — это символы в следующей строке: "!@#$%^&*()-+".
# Он не содержит 2 одинаковых символов в соседних позициях (т.е. "aab"нарушает это условие, но "aba"не является).
# Если задана строка password, вернуть, true если это надежный пароль. В противном случае вернуть false.

# Example 1:
# Input: password = "IloveLe3tcode!"
# Output: true
# Explanation: The password meets all the requirements. Therefore, we return true.

# Example 2:
# Input: password = "Me+You--IsMyDream"
# Output: false
# Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.

# Example 3:
# Input: password = "1aB!"
# Output: false
# Explanation: The password does not meet the length requirement. Therefore, we return false.

### Краткое условие:
# Если задана строка password, вернуть, true если это надежный пароль. В противном случае вернуть false.

# Алгоритм решение задачи:
# 0) Создаем переменные со значением 0: countDict, countSmallLetters, countСapitalLetters, countNumber и
# переменную lenPassword со значением длины строки password и словарь dict где хранятся все симвлолы.
# 1) Если lenPassword меньше 8, то верни False.
# 2) Проходимся циклом по диапазоны от 0 до длины строки password,
# 2.1) Если i больше 0 и символ i равен символу i-1, то верни False.
# 2.2) Если символ i маленькая буква, то увеличь countSmallLetters на 1.
# 2.3) Если символ i большая буква, то увеличь countСapitalLetters на 1.
# 2.4) Если символ i цифра, то увеличь countNumber на 1.
# 2.5) Если ключ i есть в словаре dict, то увеличь countDict на 1.
# 3) Если countSmallLetters больше 0 и countСapitalLetters больше 0, и countNumber больше 0, и countDict больше 0,
# 3.1) То верни True.
# 4) Иначе, верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

password = "11A!A!Aa"

def strongPasswordCheckerII(password):
    countDict = 0
    countSmallLetters = 0
    countСapitalLetters = 0
    countNumber = 0

    lenPassword = len(password)
    dict = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"}

    if lenPassword < 8:
        return False

    for i in range(lenPassword):

        if i > 0 and password[i] == password[i - 1]:
            return False

        if password[i].islower():
            countSmallLetters += 1
        elif password[i].isupper():
            countСapitalLetters += 1
        elif password[i].isdigit():
            countNumber += 1
        elif password[i] in dict:
            countDict += 1

    if countSmallLetters > 0 and countСapitalLetters > 0 and countNumber > 0 and countDict > 0:
        return True
    else:
        return False

strongPasswordCheckerII(password)

assert strongPasswordCheckerII(password="IloveLe3tcode!") == True
assert strongPasswordCheckerII(password="Me+You--IsMyDream") == False
assert strongPasswordCheckerII(password="1aB!") == False
assert strongPasswordCheckerII(password="11A!A!Aa") == False
assert strongPasswordCheckerII(
    password="zd!&1w!rod7&x+6t(c+^hb2+dgp$@40by0#l#7^v960f%(h8e@aw39jz2ml&5h!)s0^$jfqmwx9") == False