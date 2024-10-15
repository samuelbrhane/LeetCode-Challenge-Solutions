import heapq
import math

def max_score(nums, k):
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)
    
    score = 0
    
    for _ in range(k):
        max_value = -heapq.heappop(max_heap)
        score += max_value
        new_value = math.ceil(max_value / 3)
        
  
        heapq.heappush(max_heap, -new_value)
    
    return score
