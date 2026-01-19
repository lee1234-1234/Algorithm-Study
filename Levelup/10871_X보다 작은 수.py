N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = [str(a) for a in A if a < X]
print(" ".join(ans))
