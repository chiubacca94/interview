from math import sqrt

def solution(numbers):
    # TODO: implement this function
    opposites = []
    length = len(numbers)
    i = 0

    while i < length:
        opposite = numbers[length-1-i]
        mean = round(sqrt(numbers[i] * opposite), 2)
        opposites.append((numbers[i], mean))
        i += 1
    
    return opposites

test_numbers = [1, 2, 3, 4, 5]

print(solution(test_numbers))


def solution2(numbers):
    # TODO: implement solution here
    numbers_set = set(numbers)
    ans = []
    
    for n in numbers:
        # reverse the n number by making it a string
        number_string = str(n)
        reversed_number = int(number_string[::-1])
        if reversed_number in numbers_set:
            ans.append((n, reversed_number))
            
    return ans
        
        
def solution3(numbers):
    # TODO: Implement solution here
    numbers_length = len(numbers)
    ans = []
    
    for i in range(int(numbers_length / 2)):
        ans.append(numbers[i] + numbers[numbers_length - i - 1])
        
    if numbers_length % 2 == 1:
        ans.append(numbers[int(numbers_length / 2)] * 2)
             
    return ans