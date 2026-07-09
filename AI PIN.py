result = []

for num in range(10000):
    pin = f"{num:04d}"

    # Check all digits are even
    if all(int(d) % 2 == 0 for d in pin):
        # Check digit sum
        if sum(int(d) for d in pin) == 16:
            result.append(pin)

print("Total valid PINs:", len(result))
print(result)