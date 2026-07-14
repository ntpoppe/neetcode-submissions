class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i):
            if i == len(nums) - 1:
                return nums[i]
            elif i >= len(nums):
                return 0
            return max(nums[i] + dfs(i + 2), dfs(i + 1))

        return dfs(0)