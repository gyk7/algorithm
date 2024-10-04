from itertools import permutations

def is_prime(n):
    n = int(n)  # 문자열을 정수로 변환
    if n < 2:  # 0 또는 1은 소수가 아님
        return False
    for i in range(2, int(n**0.5) + 1):  # 2부터 n의 제곱근까지 검사
        if n % i == 0:
            return False
    return True

def solution(numbers):
    cnt = 0
    unique_numbers = set()  # 중복 숫자를 방지하기 위해 집합 사용
    
    for i in range(1, len(numbers) + 1):  # 숫자 길이에 따라 순열 생성
        for j in permutations(numbers, i):
            num_str = ''.join(j)  # 순열을 문자열로 변환
            if is_prime(num_str):  # 소수인지 확인
                unique_numbers.add(int(num_str))  # 소수인 경우 집합에 추가
    
    return len(unique_numbers)  # 중복된 소수를 제외한 소수의 개수