# Finding squares of given list:
# Python program to square the elements of a list useing map() function.

def square_num(n):
    return n * n 
nums = [4, 5, 2, 9]
print("Given ListL: ",nums)
results = map(square_num, nums)
print("Square of num elements of the list :")
print(list(results))
