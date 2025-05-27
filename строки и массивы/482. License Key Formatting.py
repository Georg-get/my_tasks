### Условие задачи:
# Вам предоставляется лицензионный ключ, представленный в виде строки s, состоящей только из букв, цифр и тире.
# Строка разделяется на n + 1группы n дефисами. Вам также дано целое число k.
# Мы хотим переформатировать строку s так, чтобы каждая группа содержала ровно k символы, за исключением первой группы,
# которая может быть короче, k но все равно должна содержать хотя бы один символ.
# Кроме того, между двумя группами должно быть вставлено тире, а все строчные буквы следует преобразовать в прописные.
# Верните переформатированный лицензионный ключ.

# Example 1:
# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.

# Example 2:
# Input: s = "2-5g-3-J", k = 2
# Output: "2-5G-3J"
# Explanation: The string s has been split into three parts,
# each part has 2 characters except the first part as it could be shorter as mentioned above.

### Краткое условие:
# Надо заменить маленькие буквы на большие в строке s начаная с индекса k.

# Алгоритм решение задачи:
# 0) Создаем строку newString со значением больших букв из строки s и без символа "-" и задам наперед, и пустой массив result.
# 1) Проходимся циклом по диапазону от 0 до длины страки newString и k,
# 1.1) Добавляем в массив result символы от i от k.
# 2) Вернуть перевернутый строку result с тере в середине.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "5F3Z-2e-9-w"
k = 4

def licenseKeyFormatting(s, k):
    newString = s.upper().replace('-', '')[::-1]  # W9E2Z3F5
    result = []

    for i in range(0, len(newString), k):  # range(0, 8, 4)
        result.append(newString[i:i + k])
    # ['W9E2', 'Z3F5']
    return '-'.join(result)[::-1]  # 5F3Z-2E9W

licenseKeyFormatting(s, k)

assert licenseKeyFormatting(s="5F3Z-2e-9-w", k=4) == "5F3Z-2E9W"
assert licenseKeyFormatting(s="2-5g-3-J", k=2) == "2-5G-3J"