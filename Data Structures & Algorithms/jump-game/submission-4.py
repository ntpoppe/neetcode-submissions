class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # If we end up after the last index, false
        # If we land on a 0, false

        curr_pos = 0
        length = len(nums)
        last_idx = length - 1
        while curr_pos < last_idx:
            valid_idxs = []
            possible_idxs = list(range(1, nums[curr_pos] + 1))
            print(f"{possible_idxs=}")
            for i in possible_idxs:
                if i + curr_pos >= last_idx:
                    return True
                    
                if nums[i + curr_pos] > 0:
                    valid_idxs.append(i + curr_pos)

            print(f"{valid_idxs=}")
            if len(valid_idxs) == 0:
                return False

            max_idx = valid_idxs[0]
            for idx in valid_idxs:
                if nums[idx] > nums[max_idx]:
                    max_idx = idx

            curr_pos = curr_pos + max_idx

        return True