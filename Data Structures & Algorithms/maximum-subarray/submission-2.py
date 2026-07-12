class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Start at i, then i + 1, sum, stored, then i + 1 and i + 2, sum, store
        # if greater, etc.

        res = -999999
        for i in range(len(nums)):
            if (len(nums) == 1):
                return nums[i]

            for j in range(len(nums[i:])):
                sub_sum = nums[i]
                for k in range(j):
                    sub_sum += nums[i + k + 1]

                if sub_sum > res:
                    res = sub_sum

        return res