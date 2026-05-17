# 문제 2. 최대 선택 가능한 과일 종류

# 과일 번호가 담긴 배열 fruits가 주어집니다.
# 당신은 전체 과일 중 절반만 가져갈 수 있습니다.
# 가져갈 수 있는 과일 종류 수의 최댓값을 return 하세요.

def solution(fruits):
    return min(len(fruits) // 2, len(set(fruits)))

print(solution([1, 1, 2, 2, 3, 3]))