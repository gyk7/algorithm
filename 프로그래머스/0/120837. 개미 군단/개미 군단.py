def solution(hp):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    cnt1 = hp // 5
    cnt2 = hp % 5 // 3
    cnt3 = hp - cnt1 * 5 - cnt2 * 3
    
    return cnt1 + cnt2 + cnt3