class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      mp = {}
      l = 0
      result = 0
      for i in range(len(s)):
        if s[i] in mp:
          l = max(l, mp[s[i]] + 1)
        mp[s[i]] = i
        result = max(result, i - l + 1)
      return result
