num = int(input())
bin = bin(num)
oct = oct(num)
hex = hex(num)

print(str(bin[2:]))
print(str(oct[2:]))
print(str(hex[2:].upper()))