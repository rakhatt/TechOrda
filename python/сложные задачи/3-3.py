n = int(input("Введите число: "))

k = bin(n)

print(f"{n} в двоичной системе: {k[2:]}")
high_bits = n >> 4
low_bits = n & 0x0F
swapped = (low_bits << 4) | high_bits
print(swapped)
