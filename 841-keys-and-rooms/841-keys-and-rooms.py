class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        d = defaultdict(list)
        for room, keys in enumerate(rooms):
            d[room].extend(keys)
        unlocked = set()
        unlocked.add(0) # Since Room 0 in unlocked by default
        nodes = 0
        dq = deque([(0, d[0])])
        while dq:
            room, keys = dq.popleft()
            for adj in d[room]:
                if adj not in unlocked:
                    unlocked.add(adj)
                    dq.append((adj, d[adj]))
                    if len(unlocked) == len(rooms):
                        return True
        return False
        