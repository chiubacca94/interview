def encode_rle(s):
    # TODO: implement
    if s == "":
        return ""
        
    lastChar = s[0]
    char_count = 1
    ans = ""
    
    for i in range(1, len(s)):
        if s[i].isalnum():
            if s[i] == lastChar:
                char_count += 1
            else:
                ans += lastChar + str(char_count)
                lastChar = s[i]
                char_count = 1
    
    return ans + lastChar + str(char_count)