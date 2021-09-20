def function(numbers, n):
    new_list = []
    counter = 0
    
    while(counter < len(numbers)):
        new_list.append(int(numbers[counter]))
        counter += 1
    
    for i in range(1,len(new_list)):
        val = new_list[i]
        j = i-1
        while(j>= 0 and val < new_list[j]):
            new_list[j+1] = new_list[j]
            j -= 1
        new_list[j+1] = val


    new_list = "".join([str(x) for x in new_list])

    if(str(n) in new_list):
        count = new_list.find(str(n))
        new_list = new_list + str(count)
        return(new_list)
    else:
        return(new_list)

    

print(function('11111', 1))