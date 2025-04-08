from collections import deque
from typing import List

def rotate_left_till_zero(nums: List[int]) -> List[int]:
    # initialize a new deque out of nums
    queue = deque(nums)
    # continue the loop till front of queue is 0
    while queue[0] != 0:
        # remove the front of the queue and add it to the end
        queue.append(queue.popleft())
    # create a list out of the queue
    return list(queue)

if __name__ == "__main__":
    # nums = [int(x) for x in input().split()]
    nums = [3, 2, 1, 0, 4, 5]
    print(nums)
    res = rotate_left_till_zero(nums)
    print(" ".join(map(str, res)))
