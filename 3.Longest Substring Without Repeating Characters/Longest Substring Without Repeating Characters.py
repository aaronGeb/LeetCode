class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setVal = set()
        left = 0
        longest = 0
        for right in range(len(s)):
            while s[right] in setVal:
                setVal.remove(s[left])
                left += 1
            setVal.add(s[right])
            longest = max(longest, right-left+1)
        return longest
