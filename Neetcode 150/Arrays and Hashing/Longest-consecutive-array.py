class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        long = 0
        for i in nums:
            if (i-1) not in set1:
                length = 0
                while (i + length) in set1:
                    length += 1
                long = max(length, long)
        return long