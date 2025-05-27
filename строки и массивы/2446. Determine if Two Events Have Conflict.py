### Условие задачи:
# Вам даны два массива строк, которые представляют два инклюзивных события, произошедших в один и тот же день, event1и event2,
# где:
# event1 = [startTime1, endTime1] и
# event2 = [startTime2, endTime2].
# Время событий указано в 24-часовом формате в формате HH:MM.
# Конфликт возникает, когда два события имеют некоторое непустое пересечение (т. е. некоторый момент является общим для обоих событий).
# Верните true, если между двумя событиями есть конфликт. В противном случае верните false.

# Example 1:
# Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
# Output: true
# Explanation: The two events intersect at time 2:00.

# Example 2:
# Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
# Output: true
# Explanation: The two events intersect starting from 01:20 to 02:00.

# Example 3:
# Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
# Output: false
# Explanation: The two events do not intersect.

### Краткое условие:
# Верните true, если между двумя событиями есть конфликт. В противном случае верните false.

# Алгоритм решение задачи:
# 0) Если первый элемента массива event1 равен или меньше второго элемента массива event2, и перый элемент массив event2 равен или меньше второго элемента массива event1,
# 0.1) Верни True
# 1) Иначе, верни False.

# Сложность:
# 1) Время O(1)
# 2) Память O(1)

event1 = ["01:15", "02:00"]
event2 = ["02:00", "03:00"]

def haveConflict(event1, event2):

    if event1[0] <= event2[1] and event2[0] <= event1[1]:
        return True
    else:
        return False

haveConflict(event1, event2)

assert haveConflict(event1=["01:15", "02:00"], event2=["02:00", "03:00"]) == True
assert haveConflict(event1=["01:00", "02:00"], event2=["01:20", "03:00"]) == True
assert haveConflict(event1=["10:00", "11:00"], event2=["14:00", "15:00"]) == False