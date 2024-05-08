def compareTriplets(a, b):
    alice_points = 0
    bob_points = 0
    # Write your code here
    for i in range(len(a)):
        if a[i] > b[i]:
            alice_points += 1
        elif a[i] < b[i]:
            bob_points += 1
        else:
            continue
    return alice_points, bob_points

a = [5, 6, 7]
b = [3, 6, 10]

print(compareTriplets(a, b))