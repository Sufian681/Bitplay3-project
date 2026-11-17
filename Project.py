a, b = 12, 5

a = a + b
b = a - b
a = a - b
print("Arithmetic Swap:", a, b)

a = a ^ b
b = a ^ b
a = a ^ b
print("XOR Swap:", a, b)
