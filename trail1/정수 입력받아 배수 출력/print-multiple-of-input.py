# 자연수 N 입력 받기
N = int(input())

# N부터 시작하여 N의 배수 5개 출력
for i in range(1, 6):
    print(N * i, end=' ')