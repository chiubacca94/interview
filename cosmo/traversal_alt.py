def unusual_traversal(array):
    # TODO: implement this function
    length = len(array)
    mid_length = length // 2
    mid = array[mid_length]
    ans = []
    ans.append(mid)
    
    left = mid_length - 1
    right = mid_length + 1
    
    # wrong: while left - 1 > 0 and right + 1 < length:
    while left > -1 and right < length - 1:
        ans.append(array[left - 1])
        ans.append(array[left])
        ans.append(array[right])
        ans.append(array[right + 1])
        
        left -= 2
        right += 2
      
    
    # the rest
    while left > -1:
        ans.append(array[left])
        left -= 1
        
    while right < length:
        ans.append(array[right])
        right += 1
        
    return ans
        
        
        