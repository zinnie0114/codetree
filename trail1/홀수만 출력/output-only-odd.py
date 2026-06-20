# 두 정수 A와 B 입력 받기
A, B = map(int, input().split())

# A부터 B까지 반복 (B를 포함해야 하므로 B + 1까지)
for i in range(A, B + 1):
    # 2로 나눈 나머지가 0이 아니면 홀수
    if i % 2 != 0:
        print(i, end=" ")