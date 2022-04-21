sen = 'fun&!! time'
list_of_sen = []
str = ''
for x in sen:
    if x.isalpha():
        str+=x
    elif x.isspace():
        list_of_sen.append(str)
        str= ''
list_of_sen.append(str)
longest = max(list_of_sen,key = len)
print(list_of_sen)