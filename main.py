
print("function test")

a, b, c = 4, 6, 2
summary = 0

for i in range(9):
    if i < a:
        summary -= i
    elif i > b:
        summary -= i // 2
    else:
        summary -= c

print(f"result: {summary}")
