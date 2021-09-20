def function(*list):
    len_list = len(list)
    i , j = 0 ,0
    
    new_list = []

    while (i < len_list):
        j = 0
        while(j < len(list[i])):
            new_list.append(list[i][j])
            j += 1
        i += 1
    return(new_list)

    



print(function( [8, "hi"], ["s", 6.5]))