# 738. Monotone Increasing Digits

## Medium

***

An integer has **monotone increasing digits** if and only if each pair of adjacent digits `x` and `y` satisfy `x <= y`.

Given an integer `n`, return _the largest number that is less than or equal to_ `n` _with **monotone increasing digits**_.

&#x20;

**Example 1:**

```
Input: n = 10
Output: 9
```

**Example 2:**

```
Input: n = 1234
Output: 1234
```

**Example 3:**

```
Input: n = 332
Output: 299
```

&#x20;

**Constraints:**

* `0 <= n <= 109`

```python
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        string = list(str(n))
        length = len(string)
        startpoint = length
        for index in range(length-1, 0, -1):
            # print('Index', index)
            if string[index-1] > string[index]:
                startpoint = index-1
                num = int(string[index-1])
                # print(num)
                string[index-1] = str(num-1)
        for index in range(startpoint+1, length):
            string[index] = '9'
        # print(string)
        return int(''.join(string))
```
