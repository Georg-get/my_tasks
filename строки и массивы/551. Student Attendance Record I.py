### Условие задачи:
# Вам предоставляется строка, sпредставляющая запись посещаемости учащегося, где каждый символ обозначает, отсутствовал ли учащийся,
# опоздал или присутствовал в этот день.
# Запись содержит только следующие три символа:
# 'A': Отсутствующий.
# 'L': Поздно.
# 'P': Подарок.
# Студент имеет право на получение награды за посещаемость, если он соответствует обоим следующим критериям:
#
# Студент отсутствовал ( 'A') строго менее 2 дней.
# Студент ни разу не опоздал ('L') на 3 и более дней подряд.
# Вернитесь true, если учащийся имеет право на получение награды за посещаемость или false иным образом.


# Example 1:
# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.

# Example 2:
# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

### Краткое условие:
# Вернуть True если буква A не повторяется больше одного раза и три подрят L нету в строке s.

# Алгоритм решение задачи:
# 0) Если в строке s буква А не повторяется больше 1 раза и три буквы L нету в строке s, то верни True.
# 1) Иначе, верни False.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

s = "PPALLP"

def checkRecord(s):

    if s.count('A') < 2 and 'LLL' not in s: # count сколько раз буква "A" повторяется в строке s.
        return True
    else:
        return False

checkRecord(s)

assert checkRecord(s="PPALLP") == True
assert checkRecord(s="PPALLL") == False
assert checkRecord(s="AAAA") == False
assert checkRecord(s="A") == True