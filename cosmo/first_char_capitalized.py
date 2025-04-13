def solution(input_str):
    # TODO: implement the function
    str_arr = input_str.split()
    ans = []
    
    for word in str_arr:
        first = word[0].upper()
        new_word = first + word[1:].lower()
        ans.append(new_word)
        
    return " ".join(ans)
        