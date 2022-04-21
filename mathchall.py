# import itertools


# def MathChallenge(num):
#   # code goes here
#     liste = [int(x) for x in str(num)]
#     permutation = itertools.permutations(liste)
#     y= list(set(permutation))
#     new_one = []
#     y = sorted(y)
#     data = [[str(x) for x in tup] for tup in y]
#     for element in data:
#         string = ''.join(element)
#         new_one.append(int(string))
    
#     return new_one[new_one.index(num)+1]

# print(MathChallenge(11121))

def PermutationsStep(num):
    
    string = str(num)
    if len(string) == 1:
        return -1
    for i in range(len(string)-2,-1,-1):
        if string[i] < string[i+1]:
            return int(string[:i] + string[i+1:] + string[i])
    else:
        return -1
# keep this function call here 
print(PermutationsStep(41352))