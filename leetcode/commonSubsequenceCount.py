class CommonSubSequnce(object):
    def __init__(self) -> None:
        super().__init__()
    
    def commonSubsequenceCount(self,s1: str, s2:str) -> int:
        length1 = len(s1)
        length2 = len(s2)
        arr = [[0 for index in range(length1+1)] for index in range(length2+1)]
        for index1 in range(1, length1+1):
            for index2 in range(1, length2+1):
                if s1[index1-1] == s2[index2-1]:
                    # If Both char are same then it will be a sum of both side subsequence plus 1
                    arr[index1][index2] = (1 + arr[index1-1][index2] + arr[index1][index2-1])
                else:
                    # Both dp[i][j-1] and dp[i-1][j] contain dp[i-1][j-1] and hence it gets added two times 
                    # in our recurrence which takes care of doubling of count of all previous common sub-sequences.
                    # That (1+) dp[i-1][j-1] above gets added to both hence we need to subtact it once when chars don't match up.
                    arr[index1][index2] = arr[index1-1][index2] + arr[index1][index2-1] - arr[index1-1][index2-1]
        return arr[length1][length2]

if __name__ == "__main__":
    cls = CommonSubSequnce()
    str1 = "ajblqcpdz"
    str2 = "aefcnbtdi"
    print(cls.commonSubsequenceCount(str1, str2))