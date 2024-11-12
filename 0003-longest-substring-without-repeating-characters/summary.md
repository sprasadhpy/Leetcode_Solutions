class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()  # This will store characters in the current substring without duplicates
        left = 0  # Left pointer for the sliding window
        max_length = 0  # This will store the maximum length of any substring without repeating characters

        for right in range(len(s)):  # Right pointer for the sliding window
            while s[right] in char_set:  # If there's a duplicate
                char_set.remove(s[left])  # Remove the character at `left` from the set
                left += 1  # Move the `left` pointer one step to the right
            char_set.add(s[right])  # Add the current character at `right` to the set
            max_length = max(max_length, right - left + 1)  # Update max_length if we have a new maximum

        return max_length


Time Complexity: 

O(n), where 
n is the length of the string s.
Space Complexity: 

O(min(m,n)), where 
m is the size of the character set (typically 128 for ASCII or up to 65,536 for Unicode).
