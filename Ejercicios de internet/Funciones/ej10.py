def dec_to_binary(num):
    num = round(num)
    return bin(num)

def binary_to_dec(binary):
    return int(binary,2)

num = 2.5

binary = dec_to_binary(num)
print(binary)

res = binary_to_dec(binary)
print(res)
