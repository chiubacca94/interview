def reversed_triple_chars(s: str) -> str:
    # TODO: Implement the function that reform the string as described above
    length = len(s)
    ans = ""
    
    if length < 3:
        return s
    
    if length < 4:
        return s[::-1]
        
    remainder = length % 3
        
    i = 0
    while (i < length - remainder):
        reversed_string = s[i: i + 3][::-1] # inclusive: exclusive
        ans += reversed_string
        i += 3
        
    ans += s[i:] # from where it leaves off to the end
        
    return ans

def reversed_triple_chars_optimized(s: str) -> str:
    result = ''
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        result += group[::-1] if len(group) == 3 else group
    return result