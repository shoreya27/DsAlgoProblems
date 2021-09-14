def gcd_euclidean(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclidean(b, a%b)

fourty_eight_and_eighteen = gcd_euclidean(48, 18)
print(fourty_eight_and_eighteen)

three_and_two = gcd_euclidean(3, 2)
print(three_and_two)

twentyfive_and_fourty = gcd_euclidean(25, 40)
print(twentyfive_and_fourty)
