### Условие задачи:
# Каждый действительный адрес электронной почты состоит из локального имени и имени домена , разделенных знаком '@'.
# Помимо строчных букв, электронное письмо может содержать один или несколько '.'символов '+'.
# Например, в "alice@leetcode.com"— "alice"локальное имя , а "leetcode.com"— доменное имя .
# Если вы добавите точки '.'между некоторыми символами в части локального имени адреса электронной почты,
# отправленная на него почта будет пересылаться на тот же адрес без точек в локальном имени. Обратите внимание,
# что это правило не распространяется на доменные имена .
# Например, "alice.z@leetcode.com"и "alicez@leetcode.com"переслать на тот же адрес электронной почты.
# Если вы добавите плюс '+'в локальное имя , все, что находится после первого знака плюса, будет игнорироваться .
# Это позволяет фильтровать определенные электронные письма. Обратите внимание, что это правило не распространяется на доменные имена .
# Например, "m.y+name@email.com"будет перенаправлено на "my@email.com".
# Возможно использование обоих этих правил одновременно.
# Учитывая массив строк emails, на каждую из которых мы отправляем по одному электронному письму emails[i],
# верните количество различных адресов, на которые фактически приходят письма .

# Example 1:
# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

# Example 2:
# Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
# Output: 3


### Краткое условие:
# Надо вернуть количестово эмейлов которые ходь как-то могут совпадать.

# Алгоритм решение задачи:
# 0) Создаем пустой словарь mails с set()
# 1) Проходимся циклом по массиву emails,
# 1.1) Убераем часть стороки после @, записываем значение домена почты в переменную в d,
# 1.2) Убераем часть стороки после +,
# 1.3) Присоединяес часть строки после точки,
# 1.4) Добавляем в словарь mails кортедж из (d, localName).
# 2) Вернуть длину словаря mails.

# Сложность:
# 1) Время O(n) (n*m)
# 2) Память O(m) (n*m)

emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

def numUniqueEmails(emails):
    mails = set()

    for i in emails:
        localName, d = i.split('@')  # d = leetcode.com # localName = test.email+alex
        localName = localName.split('+')[0]  # test.email
        localName = ''.join(localName.split('.'))  # testemail
        mails.add((d, localName))  # {('leetcode.com', 'testemail')}

    return len(mails)

numUniqueEmails(emails)

assert numUniqueEmails(
    emails=["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]) == 2
assert numUniqueEmails(emails=["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]) == 3