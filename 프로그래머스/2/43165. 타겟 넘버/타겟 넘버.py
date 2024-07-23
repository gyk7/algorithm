def solution(numbers, target):
    li = [0]
    for num in numbers:
        li2 = []
        for i in li:
            li2.append(i+num)
            li2.append(i-num)
        li = li2
    return li2.count(target)