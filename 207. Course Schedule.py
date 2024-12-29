class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited_course = set()

        for c, p in prerequisites:
            adj[c].append(p)

        def dfs(course):
            if course in visited_course:
                return False
            if adj[course] == []:
                return True

            visited_course.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False

            visited_course.remove(course)
            adj[course] = []
            
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True