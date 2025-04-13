def solution(input_str):
    # TODO: implement the string transformation function
    
    input_str_arr = input_str.split()
    input_str_arr = [input_str_arr[-1]] + input_str_arr[:-1]
    ans = []
    # print(input_str_arr)
    
    for word in input_str_arr:
        transformed_word = ""
        # print(word)
        for letter in word:
            opposite = None
            if letter.isupper():
                opposite = chr(ord('Z') + ord('A') - ord(letter))
            else:
                opposite = chr(ord('z') + ord('a') - ord(letter))
            
            transformed_word += opposite
        
        ans.append(transformed_word)
        
        
                
    return ' '.join(ans)