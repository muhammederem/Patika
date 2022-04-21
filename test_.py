new_arr = []

for x in ["[1, 2]", "[10, 14]"]:
    arr = x[1:-1].split(',')
    maps = map(int,arr)
    new_arr.append(list(maps))
print(new_arr)