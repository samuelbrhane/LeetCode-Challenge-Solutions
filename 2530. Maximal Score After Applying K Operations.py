import heapq
import math

def max_score(nums, k):
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)
    
    score = 0
    
    # Perform k operations
    for _ in range(k):
        # Extract the largest element 
        max_value = -heapq.heappop(max_heap)
        score += max_value
        new_value = math.ceil(max_value / 3)
        
        # Push the new value back into the heap
        heapq.heappush(max_heap, -new_value)
    
    return score

# Example 1
nums1 = [10, 10, 10, 10, 10]
k1 = 5
print(max_score(nums1, k1))  # Output: 50

# Example 2
nums2 = [1, 10, 3, 3, 3]
k2 = 3
print(max_score(nums2, k2))  # Output: 17
