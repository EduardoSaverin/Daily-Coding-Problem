class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data = [str(bin(seq)[2:].zfill(8)) for seq in data]
        while data:
            seq = data.pop(0)
            if seq.startswith("0"): continue
            if seq.startswith("110"):
                if not self.rest(data, 1): return False
            elif seq.startswith("1110"):
                if not self.rest(data, 2): return False
            elif seq.startswith("11110"):
                if not self.rest(data, 3): return False
            else: return False
        return True
        
    def rest(self, data, i):
        if len(data) < i: return False
        for _ in range(i):
            if not data.pop(0).startswith("10"): return False
        return True