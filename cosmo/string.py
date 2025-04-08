
def get_substring(input, start, end):
    """
    Returns the substring of input between start and end indices.
    start: inclusive
    end: exclusive
    """
    return input[start:end]


# Example usage: 
print(get_substring("abcdefghijklmnopqrstuvwxyz", 0, 5))