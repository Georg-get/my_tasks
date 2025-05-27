### Условие задачи:
# Даны два целочисленных массива startTime и endTime и дано целое число queryTime.
# Ученик ith начал выполнять домашнее задание вовремя startTime[i]и закончил его вовремя endTime[i].
# Верните количество студентов, выполняющих домашнее задание в момент времени queryTime.
# Более формально, верните количество студентов, где queryTime лежит в интервале [startTime[i], endTime[i]]включительно.

# Example 1:
# Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
# Output: 1
# Explanation: We have 3 students where:
# The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
# The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
# The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.

# Example 2:
# Input: startTime = [4], endTime = [4], queryTime = 4
# Output: 1
# Explanation: The only student was doing their homework at the queryTime.

### Краткое условие:
# Верните количество студентов, выполняющих домашнее задание в момент времени queryTime.

# Алгоритм решение задачи:
# 0) Создаем переменную result со значением 0.
# 1) Проходимся циклом по диапазону от 0 до длины массива startTime,
# 1.1) Если queryTime больше или равно startTime[i] и endTime[i] больше или равно queryTime, то увеличь result на 1.
# 2) Верни result.

# Сложность:
# 1) Время O(n)
# 2) Память O(1)

startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4

def busyStudent(startTime, endTime, queryTime):
    result = 0

    for i in range(len(startTime)):

        if queryTime >= startTime[i] and endTime[i] >= queryTime:
            result += 1

    return result

busyStudent(startTime, endTime, queryTime)

assert busyStudent(startTime=[1, 2, 3], endTime=[3, 2, 7], queryTime=4) == 1
assert busyStudent(startTime=[4], endTime=[4], queryTime=4) == 1