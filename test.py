# arr = [7, 6, 4, 1, 7, -2, 3, 12]

# target = arr[0]
# arr = arr[1:]
# new_list = []
# for x in range(len(arr)):
#     for y in range(x+1,len(arr)):
#         if arr[x]+arr[y] == target:
#             new_list.append(arr[x])
#             new_list.append(arr[y])
# print(new_list)
import numpy as np

a=np.arange(1,21).reshape(4,5)
b = np.all(a>8,axis=1)
print(b)


'''Numpy için temel konular


- Zero array 
- Belirli elemanlardan array oluşturma
- Ardışık sayılardan array oluşturma
- Normal Dist
- RandomDist
- Identity Matrix
- Array Op
- Array Attribute
- Reshape
- Concat
- Stack
- Split
- Multidimensional Array
- Fancy Index
- Subarray
- Filter
- Sum
- All
- Any


'''