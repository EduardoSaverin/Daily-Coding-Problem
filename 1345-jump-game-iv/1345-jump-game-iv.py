from collections import defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = defaultdict(list)
        _ = [d[x].append(i) for i, x in enumerate(arr)]
        q = [(0,0)]
        visited = {
            
        }
        while q:
            pos, step = q.pop(0)
            if pos == (len(arr)-1):
                return step
            if pos-1 >= 0 and (pos-1) not in visited:
                visited[pos-1] = 1
                q.append((pos-1, step+1))
            if pos+1 <= len(arr) and (pos+1) not in visited:
                visited[pos+1] = 1
                q.append((pos+1, step+1))
            for index in d[arr[pos]]:
                if index not in visited:
                    visited[index] = 1
                    q.append((index, step+1))
            d[arr[pos]] = list()
        return -1