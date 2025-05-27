### Условие задачи:
# Дана date строка в виде  dictDay dictMonth Year, где:
# dictDay есть в наборе {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
# dictMonth есть в наборе {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
# Year находится в диапазоне [1900, 2100].
# Преобразуйте строку даты в формат YYYY-MM-DD, где:
# YYYY обозначает 4-значный год.
# MM обозначает месяц из двух цифр.
# DD обозначает день из двух цифр.

# Example 1:
# Input: date = "20th Oct 2052"
# Output: "2052-10-20"

# Example 2:
# Input: date = "6th Jun 1933"
# Output: "1933-06-06"

# Example 3:
# Input: date = "26th May 1960"
# Output: "1960-05-26"

### Краткое условие:
# Переоброзовать строку date с европейской даты в американскую дату.

# Алгоритм решение задачи:
# 0) Создаем два словаря dictMon с ключем месяц со значсением номер месяца в календаре
# и dictDay с ключем числа на анг со значсением номер дня в календаре.
# 1) Создаем массив dateList со значением из строки date.
# 2) Возращаем строку которая состоит из:
# второго элемента массива dateList + "-" + значение ключа из словаря dictMon + "-" + значение ключа из словаря dictDay +

# Сложность:
# 1) Время O(1)
# 2) Память O(1)

date = "20th Oct 2052"

def reformatDate(date):
    dictMon = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
               "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
               "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

    dictDay = {"1st": "01", "2nd": "02", "3rd": "03", "4th": "04",
               "5th": "05", "6th": "06", "7th": "07", "8th": "08", "9th": "09",
               "10th": "10", "11th": "11", "12th": "12", "13th": "13",
               "14th": "14", "15th": "15", "16th": "16", "17th": "17",
               "18th": "18", "19th": "19", "20th": "20", "21st": "21",
               "22nd": "22", "23rd": "23", "24th": "24", "25th": "25",
               "26th": "26", "27th": "27", "28th": "28", "29th": "29",
               "30th": "30", "31st": "31"}

    dateList = date.split()

    return str(dateList[2]) + "-" + str(dictMon[dateList[1]]) + "-" + str(dictDay[dateList[0]])

reformatDate(date)

assert reformatDate(date="20th Oct 2052") == "2052-10-20"
assert reformatDate(date="6th Jun 1933") == "1933-06-06"
assert reformatDate(date="26th May 1960") == "1960-05-26"