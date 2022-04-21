

num1,num2 = 2,3
z = num1/num2
z = format(z,".4f")
str_result = str(z)
floats = str_result[-5:]
ints = str_result[:-5]
last_index = len(ints)
result = []
ints = ints[::-1]
for index in range(0,last_index,3):
    
    result.append(ints[index:index+3])

string_result = ','.join(result)
string_result = string_result[::-1]
string_result+= floats
print(string_result)