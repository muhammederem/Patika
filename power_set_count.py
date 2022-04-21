def PowerSetCount(arr):

  # code goes here
  len_arr = len(arr)
  if len_arr == 0:
    return 0
  return (2**len_arr)

    

  return arr

# keep this function call here 
print(PowerSetCount(input()))