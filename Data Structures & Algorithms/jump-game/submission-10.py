class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True 
        # If we end up after the last index, false
        # If we land on a 0, false

        n = len(nums)
        goal = n - 1
        curr = n - 2
        full_reach = False
        # [1,2,0,1,0]

        while curr >= 0:
            if curr + nums[curr] >= goal:
                if curr == 0:
                    full_reach = True

                goal = curr
                curr = curr - 1
            else:
                curr = curr - 1

        return full_reach