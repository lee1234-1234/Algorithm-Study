A, B, C = map(int, input().split())

if A == B == C:
    print(A * 1000 + 10000)
elif A == B or B == C or A == C:
    if A == B:
        print(A * 100 + 1000)
    elif B == C:
        print(B * 100 + 1000)
    else:
        print(C * 100 + 1000)
else:
    if A > B and A > C:
        print(A * 100)
    elif C > B and C > A:
        print(C * 100)
    else: 
        print(B * 100)