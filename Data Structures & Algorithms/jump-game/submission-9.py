class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        n = len(nums)
        goal = n - 1
        curr = n - 2
        full_reach = False
        # [1,2,0,1,0]

        while curr >= 0:
            if curr + nums[curr] >= goal:
                goal = curr
                curr = curr - 1

                if curr == 0:
                    full_reach = True
            else:
                curr = curr - 1

        return full_reach