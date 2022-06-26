class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        total = sum(cardPoints)
        current = sum(cardPoints[:size])
        minimum_sum = current
        for index in range(len(cardPoints)-size):
            # Simple Slide Window
            current += (cardPoints[index+size] - cardPoints[index])
            minimum_sum = min(minimum_sum, current)
        return total - minimum_sum