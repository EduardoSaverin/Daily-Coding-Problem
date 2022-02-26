class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph[0]) == 0:
            return 0
        total_length = len(graph)
        q = deque()
        for index in range(total_length):
            q.append((index, frozenset([index])))
        seen = set(q)
        steps = 0
        while q:
            new_q = deque()
            # print('-->', q)
            while q:
                curr, mask = q.popleft()
                mask = list(mask)
                for adj in graph[curr]:
                    mask.append(adj)
                    nextM = frozenset(mask)
                    if len(nextM) == total_length:
                        return steps + 1
                    if (adj, nextM) not in seen:
                        seen.add((adj, nextM))
                        new_q.append((adj, nextM))
                    mask.pop()
            steps += 1
            q = new_q
        return steps