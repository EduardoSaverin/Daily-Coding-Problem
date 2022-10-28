class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(int)
        group = defaultdict(list)
        for string in strs:
            for char in list(string):
                d[char] += 1
            key = ""
            for k in sorted(d.keys()):
                key += k + str(d[k])
            group[key].append(string)
            d = defaultdict(int)
        result = []
        for key, value in group.items():
            result.append(value)
        return result
            