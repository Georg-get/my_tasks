### Условие задачи:
# Предложение — это список слов, разделенных одним пробелом, без начальных и конечных пробелов.
# Каждое из слов состоит только из заглавных и строчных английских букв (без знаков препинания).
# Например, "Hello World", "HELLO"и "hello world hello world"— все предложения.
# Вам дано предложение sи целое число k. Вы хотите усечь s так, чтобы оно содержало только первые k слова. Возврат после
# s усечения.

# Example 1:
# Input: s = "Hello how are you Contestant", k = 4
# Output: "Hello how are you"
# Explanation:
# The words in s are ["Hello", "how" "are", "you", "Contestant"].
# The first 4 words are ["Hello", "how", "are", "you"].
# Hence, you should return "Hello how are you".

# Example 2:
# Input: s = "What is the solution to this problem", k = 4
# Output: "What is the solution"
# Explanation:
# The words in s are ["What", "is" "the", "solution", "to", "this", "problem"].
# The first 4 words are ["What", "is", "the", "solution"].
# Hence, you should return "What is the solution".

# Example 3:
# Input: s = "chopper is not a tanuki", k = 5
# Output: "chopper is not a tanuki"

### Краткое условие:
# Вам дано предложение sи целое число k. Вы хотите усечь s так, чтобы оно содержало только первые k слова.
# Возврат после s усечения.

# Алгоритм решение задачи:
# 0) Создаем массив result с словами из строки s.
# 1) Возращаем преобразованую строку result борезаную до k индекса.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

s = "Hello how are you Contestant"
k = 4

def truncateSentence(s, k):
    result = s.split(" ") # ['Hello', 'how', 'are', 'you', 'Contestant']
    return " ".join(result[:k]) # "Hello how are you"

truncateSentence(s, k)

assert truncateSentence(s="Hello how are you Contestant", k=4) == "Hello how are you"
assert truncateSentence(s="What is the solution to this problem", k=4) == "What is the solution"
assert truncateSentence(s="chopper is not a tanuki", k=5) == "chopper is not a tanuki"
assert truncateSentence(
    s="n a ro XBlvtpOnAh nc xKRPeYqG IioAbUh wOx xaY D CE u Wkyrslk F dn DH W u Tn wZHmz Q D b HqWkyK uQ taJxaXmh zI yLzMmC ucKdK tHH WJ m B",
    k=15) == "n a ro XBlvtpOnAh nc xKRPeYqG IioAbUh wOx xaY D CE u Wkyrslk F dn"
# Не проходят все юниттесты 47 / 72 testcases passed
# def truncateSentence(s, k):
#     result = []
#     listS = s.split()
#     # ['Hello', 'how', 'are', 'you', 'Contestant']
#
#     for i in listS:
#         if listS.index(i) <= k - 1:
#             result.append(i)
#
#     return " ".join(result)