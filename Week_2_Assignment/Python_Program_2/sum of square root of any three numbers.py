import math

def sum_of_square_roots():
    nums = [float(input("Enter number {}: ".format(i+1))) for i in range(3)]
    return sum(math.sqrt(num) for num in nums)

print("Sum of square roots: ", sum_of_square_roots())
