class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1 

        number_to_add = 1
        index = 2
        magical_arr = [1, 2, 2]

        while len(magical_arr) < n:
            count = magical_arr[index]
            magical_arr.extend([number_to_add] * count)
            index += 1
            number_to_add = 3 - number_to_add
        
        return magical_arr[:n].count(1)