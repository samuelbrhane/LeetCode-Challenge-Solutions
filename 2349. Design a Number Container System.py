class NumberContainers:
    def __init__(self):
        self.hash_map = defaultdict(list)  
        self.index_map = {}  

    def change(self, index: int, number: int) -> None:
        if index in self.index_map:
            old_number = self.index_map[index]
            if old_number != number:
                heapq.heappush(self.hash_map[number], index)
                self.index_map[index] = number 
                heapq.heappush(self.hash_map[old_number], -1) 
        else:
            heapq.heappush(self.hash_map[number], index)
            self.index_map[index] = number  
            
    def find(self, number: int) -> int:
        if number not in self.hash_map or not self.hash_map[number]:
            return -1

        while self.hash_map[number] and (self.hash_map[number][0] not in self.index_map or self.index_map[self.hash_map[number][0]] != number):
            heapq.heappop(self.hash_map[number]) 

        return self.hash_map[number][0] if self.hash_map[number] else -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)