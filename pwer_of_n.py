def power_of_n(base, power):
    assert power >= 0 and int(power) == power , "power should be greater than 0"
    if power == 0:
        return 1
    else:
        return base * power_of_n(base, power-1)
    
two_pow_seven = power_of_n(2, 7) #128
print(two_pow_seven)

three_pow_one = power_of_n(3,1) #3
print(three_pow_one)

four_pow_zero = power_of_n(4,0) #1
print(four_pow_zero)

minus_two_pow_three = power_of_n(-2, 3)
print(minus_two_pow_three)

negative_power = power_of_n(3, -2) #error
print(negative_power)