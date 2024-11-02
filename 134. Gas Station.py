class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        curr_gas = 0
        result_idx = 0
        for i in range(len(gas)):
            curr_gas += (gas[i] - cost[i])

            if curr_gas < 0:
                curr_gas = 0
                result_idx = i + 1
        
        return result_idx 