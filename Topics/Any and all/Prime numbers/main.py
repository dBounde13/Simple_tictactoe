import math
prime_numbers = [2, 3, 5]
for i in range(7, 1001):
    if all([i % x != 0 for x in range(2, math.ceil(i ** 0.5) + 1)]):
        prime_numbers.append(i)


