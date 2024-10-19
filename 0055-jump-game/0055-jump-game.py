class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        max_jump = 0  # The farthest index we can reach

        for i in range(n):
            # If the current index is greater than the max_jump, we cannot proceed
            if i > max_jump:
                return False

            # Update the farthest index we can reach from the current position
            max_jump = max(max_jump, i + nums[i])

            # If at any point we can reach or go beyond the last index, return True
            if max_jump >= n - 1:
                return True

        # After the loop, check if we can reach the last index
        return max_jump >= n - 1
