T = int(input())

for test_case in range(1, T + 1):
    a = input()
    result = []
    current_segment = ""
    ans = ""
    for char in a:
        if char in "SDHC":
            if current_segment:
                result.append(current_segment)  # 이전 값을 결과에 추가
            current_segment = char  # 현재 문자를 새로 시작
        else:
            current_segment += char  # 숫자를 이어 붙임

    if current_segment:
        result.append(current_segment)  # 마지막 항목 추가

    
    cnt_S = 13
    cnt_D = 13
    cnt_H = 13
    cnt_C = 13
        
    for k in range(len(result)) :
        if result[k].startswith('S') :
            cnt_S -= 1
        elif result[k].startswith('D') :
            cnt_D -=1 
        elif result[k].startswith('H') :
            cnt_H -=1
        elif result[k].startswith('C') :
            cnt_C -= 1
    for j in range(len(result)-1):
        for r in range(j+1,len(result)) :
            if result[j] == result[r] :
                ans = "ERROR"
    
    if ans == "ERROR" :
        print(f"#{test_case} ERROR")
    else :
        print(f"#{test_case} {cnt_S} {cnt_D} {cnt_H} {cnt_C}")
     
    
    
