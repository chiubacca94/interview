def solution(s):
    # TODO: implement
    total = 0
    length = len(s)
    
    i = 0
    while i < length:
        j=1
        if s[i].isnumeric():
            while s[i + j].isnumeric():
                j+=1
            
            total += int(s[i:i + j])
        i += j
            
    return total
