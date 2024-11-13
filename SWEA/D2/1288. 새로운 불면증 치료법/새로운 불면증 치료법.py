T = int(input())

for test_case in range(1, T + 1):
    a = int(input())
    B = set()  # 중복을 허용하지 않는 집합 사용
    k = 1
    
    while len(B) < 10:  # 모든 0-9 숫자가 나올 때까지 반복
        n = a * k
        B.update(map(int, str(n)))  # 집합에 현재 숫자들 추가
        k += 1  # 각 반복 후 k 증가
    
    print(f"#{test_case} {n}")