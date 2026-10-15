# map 
def square(n):
    return n * n
nums = [1,2,3,4,5]
sq = map(square, nums)
print(sq)

#filter
def is_even(x):
    if x%2==0:
        return True
    else:
        return False
nums = [1,2,3,4,5,6,7,8,9,10]
even_nums = filter(is_even, nums)
print(even_nums)

#reduce
from functools import reduce
def add(x,y):
    return x+y
nums = [1,2,3,4,5]
sum_nums = reduce(add, nums)
print(sum_nums)

# using lambda

nums = [1,2,3,4,5]
sq = map(lambda n: n*n , nums)
print(sq)

even_nums = filter(lambda x: x%2==0, nums)
print(even_nums)

sum_nums = reduce(lambda x,y: x+y, nums)
print(sum_nums)