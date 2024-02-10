"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""


def countSubstrings(s: str) -> int:
    count = 0
    for ind1 in range(len(s)):
        sym = s[ind1]
        for ind2 in range(ind1 + 1, len(s), 1):
            if s[ind2] == sym:
                if s[ind1:ind2 + 1] == s[ind1:ind2 + 1][::-1]:
                    count += 1
    return count + len(s)
