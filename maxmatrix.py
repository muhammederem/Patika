from zmq import EMTHREAD


def ContinSeq(lst):
  size = len(lst)
  for start in range(size):
    for end in range(start+1,size+1):
      yield(start,end)

def getSubMat(mat,start_row,end_row,start_col,end_col):
  return [i[start_col:end_col] for i in mat[start_row:end_row]]

def get_all_sub_mat(mat):
  rows = len(mat)
  cols = len(mat[0])
  for start_row,end_row in ContinSeq(list(range(rows))):
    for start_col,end_col in ContinSeq(list(range(cols))):
      yield getSubMat(mat,start_row,end_row,start_col,end_col)


def MaximalRectangle(strArr):
  arr = []
  for x in strArr:
    news = []
    for y in x:
      if y.isnumeric():
        news.append(int(y))
    arr.append(news)
  all_matrixes = [x for x in get_all_sub_mat(arr)]
  # code goes here

  matrixes = []
  for x in all_matrixes:
      if len(x)>1:
        empty = []
        for y in x:
          for q in y:
              empty.append(q)
        matrixes.append(empty)                
      else:
        matrixes.append(x)  
      
  ones = []
  for matrix in matrixes:
    counter = matrix.count(1)
    result =  counter == len(matrix)
    if result:
        ones.append(matrix)
      
  return max([len(x) for x in ones])

  
    
      

print(MaximalRectangle(["1011", "0011", "0111", "1111"]))
