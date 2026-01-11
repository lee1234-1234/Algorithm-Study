H, M = map(int, input().split())

RM = M - 45
if RM < 0:
    TM = RM + 60
    if H > 0:
        print(H - 1, TM)
    else:
        print(-(H -23), TM)
elif RM >= 0:
    if RM > 60:
        print(H + 1, RM)
    else:
        print(H, RM)