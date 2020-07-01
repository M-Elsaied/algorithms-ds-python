def isAnagram( s, t):
    s = list(s)
    t = list(t)
    if len(s) != len(t):
        return False
    countListS = [0]*26
    countListT = [0]*26
    for i in range(len(s)):
        idx= ord(s[i])-ord('a')
        countListS[idx]+=1
        idx= ord(t[i])-ord('a')
        countListT[idx]+=1
    return countListS == countListT