def ArrayCouples(arr):
  last_arr = []
  for x in range(0,len(arr),2):
    liste = []
    liste.append(arr[x])
    liste.append(arr[x+1])
    last_arr.append(liste)

  for x in last_arr:
    reverse = x[::-1]
    if reverse in last_arr:
      last_arr.remove(x)
      last_arr.remove(reverse)
    

  liste = [x for x in last_arr]
  string = ''
  for x in liste:
    for y in range(len(x)):
      if y % 2 == 0:
        string+= str(x[y])
        string+=','
      else:
        string+= str(x[y])
        string+=' '
  string = string[:-1]

  # code goes here
  if len(string )== 0:
    return 'yes'
  else:
    return string
# keep this function call here 
print(ArrayCouples(input()))