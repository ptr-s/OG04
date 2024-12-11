
print("Main function")

a, b, c = 6, 8, 5
summary = 0

for i in range(9):
    if i < a:
        summary += 2 * i
    elif i > b:
        summary += i ** 2
    else:
        summary += (c - 2)

print(f"Special result: {summary}")
