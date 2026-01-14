num = []

for _ in range(9):
    num.append(int(input()))

A, B  = max(enumerate(num, start=1), key=lambda x: x[1])
print(B)
print(A)