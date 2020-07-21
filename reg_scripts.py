#Регулярные выражения

print(r"hello\nworld") #понятие сырой строки имеет синтаксис r перед строкой
print("hello\nworld")

import re
# print(re.match) #проверяет подходит ли строка под шаблон
# print(re.search) # находит первую подстроку под шаблон
# print(re.findall) #находит все подстроки под шаблон
# print(re.sub) #заменяет подстроки чем нибудь другим

# [] -- внутри указываются подмножества подходящих символов
# \ . ^ $ * + ? {} [] \ | () -- метасимволы
# \d - [0-9] -- цифры
# \D - [^0-9]
# \s - [ \t\n\r\f\v] -- пробельные символы
# \S - [^ \t\n\r\f\v]
# \w - [a-zA-Z0-9_] -- буквы + цифры + _
# \W - [^a-zA-Z0-9_]

pattern = r"a[a-zA-Z]c"
string = "abc"
match_object = re.match(pattern, string)
print(match_object)

string="abc, acc, aac"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)
