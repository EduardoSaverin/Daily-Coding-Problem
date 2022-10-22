class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        start, end = 0,0
        i = 0
        for j, char in enumerate(s, 1):
            # If char count is still > 0 then it will counted in missing
            if need[char] > 0:
                missing -= 1
            # Decrease need of char by 1
            need[char] -= 1
            # Missing Reaches 0 it means we found all chars
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                # Find first window or minimum
                if end == 0 or j-i < end-start:
                    start, end = i, j
                need[s[i]] += 1
                missing += 1
                
                i += 1
        return s[start:end]
                