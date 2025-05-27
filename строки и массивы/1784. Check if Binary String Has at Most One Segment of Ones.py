### Условие задачи:
# Если задана двоичная строка s без начальных нулей,
# вернуть, если true содержит не более одного непрерывного сегмента единиц. В противном случае вернуть.s false

# Example 1:
# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.

# Example 2:
# Input: s = "110"
# Output: true

### Краткое условие:
# Надо проверить есть ли в в числе s строка "01", если да то вернуть False, если нет то вернуть True.

# Алгоритм решение задачи:
# 0) Если в строке s есть строка "01", то верни False.
# 1) Если в строке s НЕТУ строка "01", то верни True.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

s = "1001"

def checkOnesSegment(s):

    if "01" in str(s):
        return False
    else:
        return True

checkOnesSegment(s)

assert checkOnesSegment(s="1001") == False
assert checkOnesSegment(s="110") == True

                        #### Два указателя !!! ###
# Сложность:
# 1) Время O(n)
# 2) Память O(1)

# s = "1001"
#
# def checkOnesSegment(s):
#     left = 0
#     right = left + 1
#
#     while left < right and right < len(s):
#
#         if s[left] == '0' and s[right] == '1':
#             return False
#
#         left += 1
#         right += 1
#
#     return True
#
# checkOnesSegment(s)