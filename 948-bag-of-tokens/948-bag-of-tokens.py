class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        result = 0
        current = 0
        d = deque(sorted(tokens))
        while d and (d[0] <= power or current):
            if d[0] <= power:
                power -= d.popleft() # Subtract min when subtracting
                current += 1
            else:
                power += d.pop() # Pick Max When picking
                current -= 1
            result = max(result, current)
        return result