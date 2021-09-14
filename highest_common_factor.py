def gcd(num1, num2, div):
    # print(div)
    if div == 1:
        return 1
    elif num1%div == 0 and num2%div==0:
        return div
    else:
        return gcd(num1, num2, div-1)

hcf_four_eight = gcd(4,8,4)
print(hcf_four_eight)

hcf_two_three = gcd(2,3,2)
print(hcf_two_three)

hcf_nine_21 = gcd(9,21,9)
print(hcf_nine_21)

