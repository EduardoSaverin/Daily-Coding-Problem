class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        d = defaultdict(list)
        for product in products:
            for index in range(1, len(product)+1):
                d[product[:index]].append(product)
        result = []
        # print(d)
        for index in range(1, len(searchWord)+1):
            char = searchWord[:index]
            result.append(sorted(d[char])[:3])
        return result
                