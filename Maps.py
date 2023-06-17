# Way with Maps :
# Python program to triple all numbers of given list of integers.

nums = ( 1, 2, 3, 4, 5, 6, 7) 
print("Given list: ", nums)
result = map(lambda x: x + x + x, nums)
print("\nTtiple of list numbers:")
print(list(result))