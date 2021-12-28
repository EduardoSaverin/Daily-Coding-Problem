# 394. Decode String

## Medium

***

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there won't be input like `3a` or `2[4]`.

&#x20;

**Example 1:**

```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

**Example 2:**

```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

**Example 3:**

```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

**Example 4:**

```
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
```

&#x20;

**Constraints:**

* `1 <= s.length <= 30`
* `s` consists of lowercase English letters, digits, and square brackets `'[]'`.
* `s` is guaranteed to be **a valid** input.
* All the integers in `s` are in the range `[1, 300]`.

```python
class Solution:
    def decodeString(self, s: str) -> str:
        # Let's first find out all string within different []
        # This thing will help us in recursion calling
        closingBracket = {}
        stack = []
        for index, char in enumerate(s):
            if char == '[':
                stack.append(index)
            elif char == ']':
                closingBracket[stack.pop()] = index
        # Uncomment below line to se what we get from above code
        # self.printBracketStrings(s, closingBracket)
        return self.helper(s, 0, len(s)-1, closingBracket)
        
    
    def printBracketStrings(self, s:str, closingBracket):
        for key,value in closingBracket.items():
            print(s[key+1:value])
        
    def helper(self, s, left, right, closingBracket):
        # left and right are boundaries of string within []
        num = 0
        result = []
        while left <= right:
            if s[left].isdigit():
                num = num*10 + int(s[left])
            elif s[left] == '[':
                value = num*self.helper(s, left+1, closingBracket[left] - 1, closingBracket)
                num = 0
                result.append(value)
                left = closingBracket[left]
            else:
                # Simple Characters
                result.append(s[left])
            left += 1
        return "".join(result)
```
