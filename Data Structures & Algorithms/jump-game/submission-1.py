class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # If we end up after the last index, false
        # If we land on a 0, false

        curr_pos = 0
        length = len(nums)
        last_idx = length - 1
        while curr_pos != last_idx:
            if nums[curr_pos] == 0:
                return False

            curr_pos += nums[curr_pos]

        return True