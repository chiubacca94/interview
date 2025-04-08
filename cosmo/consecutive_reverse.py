def solution(s):
    # TODO: implement the algorithm to find consecutive groups of characters in the reverse order
    length = len(s)
    last_char = s[length-1]
    cur_length = 1  # Start at 1 to count the first character
    ans = []
    
    for i in range(length-2, -1, -1):  # Start from the second last character
        # if s[i].isalnum():
        if s[i] == last_char:
            cur_length += 1
        else:
            ans.append((last_char, cur_length))
            cur_length = 1
            last_char = s[i]
            
    # if last_char.isalnum():
    ans.append((last_char, cur_length))
    
    return ans
    
# Indexing Error: The loop should iterate from length-1 to -1 to include the first character.
# Character Comparison: Use s[c] instead of c for character comparison.
# Initial cur_length: Start cur_length at 1 since the last character is already counted.
# Appending the Last Group: Ensure the last group is appended after the loop.
# Non-Alphanumeric Characters: Consider ignoring non-alphanumeric characters.
# Resetting cur_length: It should be reset to 1 instead of 0 when a new character is encountered.
# Return Statement: Use ans.append((last_char, cur_length)) before returning ans to ensure the last group is included.