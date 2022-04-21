def MatrixSpiral(strArr):
  string = ''
  new_arr = []

  for x in strArr:
    arr = x[1:-1].split(',')
    maps = map(int,arr)
    new_arr.append(list(maps))

    
  strArr = new_arr

  # code goes here
  if not strArr or not len(strArr):
    return

  top = left = 0
  bottom = len(strArr) - 1
  right = len(strArr[0]) - 1

  while True:
    if left > right:
      break
    
    for i in range(left,right + 1):
      string += str(strArr[top][i])+' '
    top = top + 1

    if top > bottom:
      break

    
    #sag taraf
    for i in range(top, bottom + 1):
      string += str(strArr[i][right])+' '
    right = right -1

    if left > right:
      break

    #son satir

    for i in range(right, left - 1, -1):
      string += str(strArr[bottom][i])+' '
    bottom = bottom -1

    if top > bottom:
      break

    #sol sutun

    for i in range(bottom , top - 1, -1):
      string += str(strArr[i][left])+ ' '
    left = left +1
    
  return string[:-1]

print(MatrixSpiral(["[1, 2]", "[10, 14]"]))