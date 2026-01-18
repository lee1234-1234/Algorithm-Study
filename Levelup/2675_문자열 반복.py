S = int(input())

for _ in range(S):
    A, B = input().split()
    AA = int(A)
    p = ""
    for i in B:
        p += i*AA
    print(p)