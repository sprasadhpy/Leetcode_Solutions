class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the values we have seen so far
        seen = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the difference between the target and the current number
            complement = target - num
            
            # If the complement is already in the dictionary, return its index and the current index
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, store the current number's index in the dictionary
            seen[num] = i
