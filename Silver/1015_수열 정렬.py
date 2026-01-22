N = int(input())
A = list(map(int, input().split()))

A_list = list(enumerate(A))
A_list.sort(key=lambda x: x[1])

P = [0] * N

for rank, (original_index, value) in enumerate(A_list):
    P[original_index] = rank
    
print(*P)