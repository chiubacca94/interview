def solution(n):
    # TODO: implement
    ans = 0
    
    while n > 0:
        last_digit = n % 10
        n //= 10
        
        digit = n % 10
        if digit == last_digit:
            ans += 1
        
        
    return ans
        