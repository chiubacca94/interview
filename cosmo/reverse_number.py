def solution(n):
    # TODO: implement the solution here
    reversed_number = 0
    
    while n > 0:
        digit = n % 10
        
        reversed_number = reversed_number * 10 + digit
        
        n //= 10
        
    return reversed_number
        
print(solution(1234))