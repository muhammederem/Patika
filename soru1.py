flatted = []
def flatten(liste):
    for a in liste:
        if type(a) == list:
            flatten(a)
        else:
            flatted.append(a)
    
        

flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(flatted)