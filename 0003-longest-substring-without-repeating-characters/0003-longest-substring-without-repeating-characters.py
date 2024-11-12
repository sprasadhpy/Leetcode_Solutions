class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Array to track characters; assume 128 ASCII characters
        char_array = [False] * 128  
        left = 0  # Left pointer for the sliding window
        max_length = 0  # To store the maximum length of substring without duplicates

        for right in range(len(s)):
            # Convert character to ASCII value to use as an index
            char_index = ord(s[right])  
            
            # Check if the character at `right` is already in the window
            while char_array[char_index]:  
                # Remove the character at `left` from the window
                char_array[ord(s[left])] = False  
                left += 1  # Move `left` pointer to the right
            
            # Mark the character at `right` as present
            char_array[char_index] = True  
            
            # Calculate the length of the current substring and update max_length
            max_length = max(max_length, right - left + 1)
        
        return max_length
