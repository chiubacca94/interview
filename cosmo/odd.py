def solution(n):
    # TODO: implement
    product = 1
    odd_digit_counter = 0
    
    while n > 0:
        digit = n % 10
        
        if digit % 2 == 1:
            product *= digit
            odd_digit_counter += 1
        
        n //=10
        
    if odd_digit_counter == 0:
        product = 0

    return product


solution(34556)
