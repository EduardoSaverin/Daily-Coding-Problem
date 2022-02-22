class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""
        else:
            # Why -1 here , think using 'A' character it will be clear
            return self.convertToTitle((columnNumber-1)//26) + chr((columnNumber-1) % 26 + ord('A'))