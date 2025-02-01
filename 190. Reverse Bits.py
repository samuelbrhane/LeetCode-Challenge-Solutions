class Solution:
    def reverseBits(self, n: int) -> int:
        int_binary = format(n, "032b")
        binary_arr = [char for char in int_binary]
        n = len(binary_arr)
        left, right = 0, n - 1
        
        while left < right:
            temp = binary_arr[left]
            binary_arr[left] = binary_arr[right]
            binary_arr[right] = temp
            left += 1
            right -= 1

        return int("".join(binary_arr), 2)