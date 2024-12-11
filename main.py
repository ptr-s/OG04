
print("Test new function")

a = 3
b = 7
c = 1
summary = 0

for i in range(9):
    if i < a:
        summary += i
    elif i > b:
        summary += i // 2
    else:
        summary += c

print(f"Some result: {summary}")
