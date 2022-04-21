def Primes(num):

  # code goes here
  if num >2 :
    for i in range(2,num-1):
      if num%i == 0:
        return 'false'
    return 'true'
  elif num == 2 :
    return 'true'
#   elif num == 4:
#       return 'false'  
  else:
    return 'false'
    
  
print(Primes(4))