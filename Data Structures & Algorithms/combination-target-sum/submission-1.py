class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Loop through each of the numbers
        # For each number, we loop through each number again
        # Check to see if the running sum of the path is greater than/equal to the target
        # If it's greater than, continue to the next number in current scope
        # If it's equal to, append path to results
        # If it's less than, continue recursively searching

        results = []
        nums.sort()

        def backtrack(remain, path, start):
            for i in range(start, len(nums)):
                if nums[i] > remain:
                    break

                if nums[i] == remain:
                    copy = path.copy()
                    copy.append(nums[i])
                    results.append(copy)

                path.append(nums[i])
                backtrack(remain - nums[i], path, i)
                path.pop()

        backtrack(target, [], 0)   

        return results