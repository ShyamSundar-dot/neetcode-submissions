class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)

        longest = 0

        for x in arr:
            if x-1 not in arr:
                length = 1

                while x + length in arr:
                    length += 1


                if length > longest:
                    longest = length

        return longest
        