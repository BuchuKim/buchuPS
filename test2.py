def gyo(a,b):
    answer = 0
    for i in a:
        if (i in b):
            answer += 1
    return answer
def hap(a,b,g):
    return len(a) + len(b) - g
def solution(str1, str2):
    # 두 글자씩 끊어! (공백, 숫자, 특수문자는 글자쌍버려.)
    # 대문자/소문자 차이 무시
    ja = 0
    alpha = "abcdefghijklmnopqrstuvwxyz"
    s1 = []
    s2 = []
    for i in range(len(str1)-1):
        first,second = str1[i:i+2]
        first = first.lower()
        second = second.lower()
        if (first not in alpha or second not in alpha):
            continue
        s1.append(first+second)
    for i in range(len(str2)-1):
        first,second = str2[i:i+2]
        first = first.lower()
        second = second.lower()
        if (first not in alpha or second not in alpha):
            continue
        s2.append(first+second)
    if (len(s1)==0 and len(s2)==0):
        ja = 1
    else:
        # 교집합과 합집합을 구해야해
        g = gyo(s1,s2)
        h = hap(s1,s2,g)
        ja = gyo/hap
    answer = int(65536 * ja)
    return answer
print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))