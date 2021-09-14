def dec_to_bin(n):
    assert int(n) == n , "number should be a decimal number"
    if n == 0:
        return '' 
    return dec_to_bin(n//2) + str(n%2)

convert_7 = dec_to_bin(7)
print(convert_7)

convert_64 = dec_to_bin(64)
print(convert_64)

convert_1 = dec_to_bin(1)
print(convert_1)

convert_13 = dec_to_bin(13)
print(convert_13)