class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        string = "abc"
        k = [k]  
        result = []

        def backtrack(index, path):
            if len(path) == n:
                k[0] -= 1
                if k[0] == 0:
                    result.append("".join(path))  
                return

            for i in range(3):  
                if index >= 0 and path[index] == string[i]:  
                    continue  
                
                backtrack(index + 1, path + string[i])  

                if result: 
                    return

        backtrack(-1, "")
        return result[0] if result else ""
