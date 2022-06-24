[1,1,1,1,1]
​
[8,5]
[3,5]
[3,2]
[1,2]
[1,1]
​
[9,3,5]
[1,3,5]
[1,3,1]
[1,1,1]
​
class Solution:
def isPossible(self, target: List[int]) -> bool:
arr = []
for num in target:
arr.append(-1*num)
heapify(arr) # Created Max Heap using negative value
while len(arr)!=0:
num = heappop(arr)
num *= -1
if num == 1:
continue
num += sum(arr)
if num < 1:
return False
heappush(arr, -num)
return True
​