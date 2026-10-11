k = 1
s = 0

for i in range(1000000):
    # even index elements are positive
    if i % 2 == 0:
        s += 4 / k
    # odd index elements are negative
    else:
        s -= 4 / k
    # denominator is odd
    k += 2

print("PI:", s)
