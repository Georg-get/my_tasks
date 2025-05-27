### Условие задачи:
# Вам дан массив items, где каждый описывает тип, цвет и название элемента . Вам также дано правило,
# представленное двумя строками и .items[i] = [type i, color i, name i] i th ruleKey ruleValue
# Говорят, что элемент соответствует правилу, если выполняется одно из следующих условий:ith
# ruleKey == "type"и .ruleValue == type i
# ruleKey == "color"и .ruleValue == color i
# ruleKey == "name"и .ruleValue == name i
# Верните количество элементов, соответствующих заданному правилу .

# Example 1:
# Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
# Output: 1
# Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

# Example 2:
# Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
# Output: 2
# Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.

### Краткое условие:
# Верните количество элементов, соответствующих заданному правилу.

# Полное объяснение решение задачи:
# 0) Создаем словарь с ключем название и значением числом, и result со значением 0.
# 1) Проходимся циклом по массиву items,
# 1.1) i равно значению ключа ruleKey из словаря dict.
# 1.2) Если массиве есть слова ruleKey и оно равно ruleValue, то увеличь result на 1.
# 2) Верни result.

# Сложность:
# 1) Время O(n)
# 2) Память O(n)

items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
ruleKey = "color"
ruleValue = "silver"

def countMatches(items, ruleKey, ruleValue):
    dict = {"type": 0, "color": 1, "name": 2}
    result = 0
    
    for item in items:

        i = dict[ruleKey]

        if item[i] == ruleValue:
            result += 1
            
    return result

countMatches(items, ruleKey, ruleValue)

assert countMatches(items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
                    ruleKey="color", ruleValue="silver") == 1
assert countMatches(items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
                    ruleKey="type", ruleValue="phone") == 2