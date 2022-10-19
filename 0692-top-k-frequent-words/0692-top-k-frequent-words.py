class Word:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        h = []
        for word, count in counter.items():
            heapq.heappush(h, Word(word, count))
            if len(h) > k:
                heapq.heappop(h)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(h).word)
        return result[::-1]