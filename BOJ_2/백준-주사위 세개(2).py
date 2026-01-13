A, B, C = map(int, input().split())
x = sorted([A, B, C]) #순서대로 정렬

if x[0] == x[2]: # 첫과 끝이 같음 == 모두 같음
    print(10000 + x[0] * 1000)
elif x[0] == x[1]: # 첫과 둘째 같음
    print(1000 + x[0] * 100)
elif x[1] == x[2]: # 둘째와 셋째 같음
    print(1000 + x[2] * 100)
else: # 다 다름
    print(x[2] * 100)