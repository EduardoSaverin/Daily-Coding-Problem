"""
Problem 31
Description : The edit distance between two strings refers to the minimum number of character insertions, deletions, 
and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” 
is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
"""

class Problem31(object):
    def __init__(self) -> None:
        super().__init__()

    def findDistance(self, str1: str, str2: str) -> int:
        """[Solution 1 of edit distance, number of operations to convert string 1 to string 2]
        Complexity : O(mxn)

        Args:
            str1 (str): [String 1]
            str2 (str): [String 2]

        Returns:
            [int]: [Returns number of difference between two strings]
        """
        rows, cols = len(str1)+1, len(str2)+1
        arr = [[0 for x in range(cols)] for y in range(rows)]
        for i in range(1, rows):
            arr[i][0] = i
        
        for j in range(1, cols):
            arr[0][j] = j

        for i in range(1, rows):
            for j in range(1, cols):
                if str1[i-1] == str2[j-1]:
                    arr[i][j] = arr[i-1][j-1]
                else:
                    arr[i][j] = min(arr[i][j-1], arr[i-1][j], arr[i-1][j-1]) + 1
        self.visualize_array(arr)
        return arr[rows-1][cols-1]

    def visualize_array(self, arr):
        for row in arr:
            print(row, end="\n")
        print("=="*20)


    def findDistanceSolution2(self, str1: str, str2: str) -> int:
        arr = [[0 for x in range(len(str2)+1)] for y in range(2)]
        for i in range(len(str2)+1):
            arr[0][i] = i
        
        for i in range(1, len(str1) + 1):
            for j in range(0, len(str2)+1):
                if j == 0:
                    arr[i%2][j] = i
                elif str2[j-1] == str1[i-1]:
                    arr[i%2][j] = arr[(i-1)%2][j-1]
                else:
                    arr[i%2][j] = 1 + min(arr[i%2][j-1], arr[(i-1)%2][j], arr[(i-1)%2][j-1])
                self.visualize_array(arr)
        return arr[len(str1)%2][len(str2)]

if __name__ == "__main__":
    pb31 = Problem31()
    print("Enter Strings to find edit distance", end="\n")
    str1 = str(input("String 1: "))
    str2 = str(input("String 2: "))
    print(pb31.findDistanceSolution2(str1, str2))