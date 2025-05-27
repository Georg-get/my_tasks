### Условие задачи:
# Элис и Боб едут в Рим на отдельные деловые встречи.
# Вам даны 4 строки arriveAlice, leaveAlice, arriveBob, и leaveBob.
# Алиса будет находиться в городе с даты arriveAliceпо leaveAlice( включительно ), а Боб будет находиться в городе с даты arriveBobпо leaveBob( включительно ).
# Каждая будет 5-символьной строкой в формате "MM-DD", соответствующей месяцу и дню даты.
# Верните общее количество дней, в течение которых Алиса и Боб находятся в Риме вместе.
# Вы можете предположить, что все даты происходят в одном календарном году, который не является високосным.
# Обратите внимание, что количество дней в месяце можно представить как: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

# Example 1:
# Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
# Output: 3
# Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19.
# They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.

# Example 2:
# Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
# Output: 0
# Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.

### Краткое условие:
# Верните общее количество дней, в течение которых Алиса и Боб находятся в Риме вместе.

# Полное объяснение решение задачи:
# 0) Создаем словарь dict в котором ключ это месяц, а значение это дни в текущем году предшествующие месяцу.
# 1) Мы разделяем месяц и день месяца и используем эти целые числа и dict, чтобы определить день года для каждой даты.
# 2) Определяем дату более раннего выезда и более позднего прибытия.
# 3) Возвращаем перекрытие (если есть).

# Сложность:
# 1) Время O(1)
# 2) Память O(1)

arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"

def countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob):
    dict = {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334}

    def days(date):
        mon, day = date.split('-')
        return dict[int(mon)] + int(day)

    arrive, leave = ( max(days(arriveAlice), days(arriveBob)), min(days(leaveAlice), days(leaveBob)) )

    return max(leave - arrive + 1, 0)

countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)

assert countDaysTogether(arriveAlice="08-15", leaveAlice="08-18", arriveBob="08-16", leaveBob="08-19") == 3
assert countDaysTogether(arriveAlice="10-01", leaveAlice="10-31", arriveBob="11-01", leaveBob="12-31") == 0