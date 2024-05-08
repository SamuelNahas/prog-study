def aVeryBigSum(n):
    total_sum = 0
    
    for i in range(n):
        total_sum += 100000000 + i + 1
    
    return total_sum

print(aVeryBigSum(5))