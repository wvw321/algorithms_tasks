"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


def lengthOfLongestSubstring(s: str) -> int:
    Len_s = len(s)
    if Len_s == 0:
        return 0
    if Len_s == 1:
        return 1
    len_set_s = len(set(s))
    if len_set_s == 1:
        return 1

    for y in range(len_set_s, 1, -1):

        for x in range(0, Len_s - y + 1, 1):

            count = len(set(s[0 + x: y + x]))

            if y == count:
                return count
    return 1
