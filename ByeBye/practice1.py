# 문제 1. 중복 숫자 제거 후 개수 구하기

def solution(nums):
    return len(set(nums))

print(solution([1, 2, 3, 1, 2]))
# nums = [1, 2, 3, 1, 2]
# result = 3