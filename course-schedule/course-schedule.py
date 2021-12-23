from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0]*numCourses
        d = defaultdict(list)
        q = deque()
        ans = []
        for prev,nxt in prerequisites:
            degree[nxt] += 1
            d[prev].append(nxt)
        for index in range(numCourses):
            if degree[index] == 0:
                q.append(index)
        while q:
            course = q.pop()
            ans.append(course)
            for adjCourse in d[course]:
                degree[adjCourse] -= 1
                if degree[adjCourse] == 0:
                    q.append(adjCourse)
        return True if len(ans) == numCourses else False