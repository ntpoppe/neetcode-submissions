class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        max_ending = nums[0]
        new_subarray = False

        for i in range(1, len(nums)):
            num = nums[i]
            if new_subarray:
                new_subarray = False
                max_ending = num
            else:
                max_ending += num

            res = max(res, max_ending)

            if max_ending < 0:
                new_subarray = True

        return res
