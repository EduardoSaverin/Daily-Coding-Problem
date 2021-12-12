class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k:
            return False
        target=total//k
        length=len(nums)
        used=[False]*length

        def Helper(i,k,currentSum):
            if k==0:
                return True
            if currentSum==target:
                return Helper(0,k-1,0)
            for j in range(i,length):
                newCurrentSum=currentSum+nums[j]
                if used[j] or newCurrentSum>target:
                    continue
                used[j]=True
                if Helper(j,k,newCurrentSum):
                    return True
                used[j]=False
            return False
        return Helper(0 , k, 0)