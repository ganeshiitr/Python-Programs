from array import *

arr = array('i', [])

n = int(input("Enter number of elements in array"))

for i in range(n):
    num = int(input("Enter element"))
    arr.append(num)

print(arr)

num = int(input("Enter element to search in array"))

found = False

for i in range(n):
    if arr[i] == num:
        found = True
        break
if found:
    print("Element Found")
else:
    print("Element Not Found")

