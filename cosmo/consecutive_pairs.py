def solution(s):
    # TODO: Implement the function here
    length = len(s)
    pairs = []
    count = 1
    ans = ""
    
    for i in range(0, length, 2):
        pairs.append(s[i:i + 2])
    
    last_pair = pairs[0]
    
    for i in range(1, len(pairs)):
        if last_pair == pairs[i]:
            count += 1
        else:
            ans += last_pair + str(count)
            last_pair = pairs[i]
            count = 1
            
    ans += last_pair + str(count)
    
    return ans
        
            
    

# def solution(s):
#     length = len(s)
#     last_char = s[length-1]
#     cur_length = 1  # Start at 1 to count the first character
#     ans = []
    
#     for i in range(length-2, -1, -1):  # Start from the second last character
#         if s[i] == last_char:
#             cur_length += 1
#         else:
#             ans.append((last_char, cur_length))
#             cur_length = 1
#             last_char = s[i]
            
#     ans.append((last_char, cur_length))  # Append the last group
    
#     return ans