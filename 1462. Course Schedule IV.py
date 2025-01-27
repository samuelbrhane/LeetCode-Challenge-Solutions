class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        direct_pre = defaultdict(list)
        all_pre = {}
        result = []

        for pre, course in prerequisites:
            direct_pre[course].append(pre)

        def dfs(course):
            if course in all_pre:
                return all_pre[course]

            course_pres = set(direct_pre[course])

            for pre in direct_pre[course]:
                course_pres |= dfs(pre)

            all_pre[course] = course_pres

            return course_pres

        for course in range(numCourses):
            dfs(course)

        for pre, course in queries:
            result.append(pre in all_pre[course])

        return result