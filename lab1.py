# Smart PIN Generator

even_digits = [0, 2, 4, 6, 8]
valid_pins = []

for d1 in even_digits:
    for d2 in even_digits:
        for d3 in even_digits:
            for d4 in even_digits:

                total = d1 + d2 + d3 + d4

                if total == 16:
                    pin = f"{d1}{d2}{d3}{d4}"
                    valid_pins.append((pin, total))

print("=" * 40)
print("SMART PIN GENERATOR")
print("=" * 40)

print(f"{'PIN':<10}{'SUM'}")
print("-" * 20)

for pin, total in valid_pins:
    print(f"{pin:<10}{total}")

print("-" * 20)
print("Total Valid PINs:", len(valid_pins))