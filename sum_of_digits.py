def sumDigits(n):
    if n==0:
        return 0
    else:
        return int(n%10) + sumDigits(n//10)

sum = sumDigits(4)
print(sum)