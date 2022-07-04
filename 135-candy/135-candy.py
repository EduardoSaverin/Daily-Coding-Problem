class Solution:
    def candy(self, ratings: List[int]) -> int:
        length, ans = len(ratings), [1]*len(ratings)
        # Forward
        for index in range(length-1):
            if ratings[index] < ratings[index+1]:
                ans[index+1] = max(1+ans[index], ans[index+1])
        
        #Backward
        for index in range(length-2, -1 , -1):
            if ratings[index] > ratings[index+1]:
                ans[index] = max(1+ans[index+1], ans[index])
                
        return sum(ans)