def SearchingChallenge(strParam):

  # code goes here
  numbers = 0
  chars = 0
  for x in strParam:
    if x.isnumeric():
      numbers += int(x)
    elif x.isalpha():
        chars+=1
        

  return round(numbers/chars)

print(SearchingChallenge('Hello6 9World 2, Nic8e D7ay!'))