class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word_counts = {}
        for b in words2:
            tmp = Counter(b)
            for key, count in tmp.items():
                if key not in word_counts:
                    word_counts[key] = count
                else:
                    word_counts[key] = max(word_counts[key], count)
        result = []
        for word in words1:
            tmp = Counter(word)
            if all([k in tmp and v <= tmp[k] for k,v in word_counts.items()]):
                result.append(word)
        return result
        
