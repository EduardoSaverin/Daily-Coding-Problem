# 227. Basic Calculator II

## Medium

***

Given a string `s` which represents an expression, _evaluate this expression and return its value_.&#x20;

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-231, 231 - 1]`.

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

&#x20;

**Example 1:**

```
Input: s = "3+2*2"
Output: 7
```

**Example 2:**

```
Input: s = " 3/2 "
Output: 1
```

**Example 3:**

```
Input: s = " 3+5 / 2 "
Output: 5
```

&#x20;

**Constraints:**

* `1 <= s.length <= 3 * 105`
* `s` consists of integers and operators `('+', '-', '*', '/')` separated by some number of spaces.
* `s` represents **a valid expression**.
* All the integers in the expression are non-negative integers in the range `[0, 231 - 1]`.
* The answer is **guaranteed** to fit in a **32-bit integer**.

Solution

```python
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        sign = "+"
        for index in range(len(s)):
            char = s[index]
            if char.isdigit():
                num = num*10 + int(char)
            if char in ["+", "-", "*", "/"] or index == len(s)-1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    temp = stack.pop()
                    stack.append(int(temp/num))
                num = 0
                sign = char
        return sum(stack)
```
