class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a = set()
        set_b = set()
        curr_res, result = 0, []
        n = len(A)

        for i in range(n):
            if A[i] in set_b:
                curr_res += 1
            if B[i] in set_a:
                curr_res += 1
            if A[i] == B[i]:
                curr_res += 1
            
            set_a.add(A[i])
            set_b.add(B[i])
            result.append(curr_res)

        return result