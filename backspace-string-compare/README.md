# 844. Backspace String Compare

## Easy

***

Given two strings `s` and `t`, return `true` _if they are equal when both are typed into empty text editors_. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

&#x20;

**Example 1:**

```
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
```

**Example 2:**

```
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
```

**Example 3:**

```
Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
```

**Example 4:**

```
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
```

&#x20;

**Constraints:**

* `1 <= s.length, t.length <= 200`
* `s` and `t` only contain lowercase letters and `'#'` characters.

&#x20;**Solution**

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        str1 = []
        str2 = []
        for char in list(s):
            if char == '#':
                if str1:
                    str1.pop()
            else:
                str1.append(char)
        for char in list(t):
            if char == '#':
                if str2:
                    str2.pop()
            else:
                str2.append(char)
        print(str1, str2)
        return str1 == str2
```

**Follow up:** Can you solve it in `O(n)` time and `O(1)` space?
