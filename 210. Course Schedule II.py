class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        result = []
        cycle_cell, visited_cell = set(), set()

        for course, pre in prerequisites:
            adj[course].append(pre)

        def dfs(course):
            if course in cycle_cell:
                return False
            if course in visited_cell:
                return True

            cycle_cell.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            
            cycle_cell.remove(course)
            visited_cell.add(course)
            result.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return result