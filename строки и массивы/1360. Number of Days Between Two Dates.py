### Условие задачи:
# Напишите программу для подсчета количества дней между двумя датами.
# Две даты указаны в виде строк, их формат YYYY-MM-DD показан в примерах.

# Example 1:
# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1

# Example 2:
# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15

### Краткое условие:
# Напишите программу для подсчета количества дней между двумя датами.

# Полное объяснение решение задачи:
# 0) Создаем функцию convertStringToDate, которая помогает конвертнуть строку в дату.
# 1) Возврашаем результаты вычесление date1 - date2.

# Сложность:
# 1) Время O(1)
# 2) Память O(1)

from datetime import datetime

date1 = "2019-06-29"
date2 = "2019-06-30"

def daysBetweenDates(date1, date2):

    def convertStringToDate(date):
        exactDate = datetime.strptime(date, '%Y-%m-%d').date()
        return exactDate

    return abs((convertStringToDate(date1) - convertStringToDate(date2)).days)

daysBetweenDates(date1, date2)

assert daysBetweenDates(date1="2019-06-29", date2="2019-06-30") == 1
assert daysBetweenDates(date1="2020-01-15", date2="2019-12-31") == 15