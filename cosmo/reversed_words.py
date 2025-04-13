def solution(s):
    # TODO: Implement the solution here
    s_arr = s.split()
    reversed_words = []
    
    for word in s_arr:
        word = word[-1] + word[:-1]
        reversed_words.append(word)
    
    return " ".join(reversed_words)
        