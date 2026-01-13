A, B = map(int, input().split())
C = int(input())
    
B = B + C
RH = B // 60 # 분에서 60을 나눠서 시간이 얼마나 플러스 되는지
RM = B % 60
H = (A + RH) % 24 # A(원래 시간) + RH(플러스 되는 시간) % 24시가 되면 0으로 시작하게
print(H, RM)