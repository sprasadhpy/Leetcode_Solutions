
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


Algorithm Steps
## Algorithm Steps

### 1. Initialize Variables
- Create an empty set `char_set` to store unique characters in the current substring.
- Set `left` pointer to `0`, the starting point of the sliding window.
- Set `max_length` to `0`, to store the length of the longest substring found.

### 2. Traverse the String with `right` Pointer
- Use a `for` loop to move the `right` pointer from the start to the end of the string.

### 3. Check for Duplicates
- While `s[right]` is in `char_set` (indicating a duplicate):
  - Remove `s[left]` from `char_set`.
  - Move the `left` pointer one step right to shrink the window and remove duplicates.

### 4. Add Current Character
- Add `s[right]` to `char_set` after ensuring there are no duplicates.

### 5. Update Maximum Length
- Calculate the current window length as `right - left + 1`.
- Update `max_length` with the maximum of its current value and the current window length.

### 6. Return Result
- After the loop, `max_length` contains the length of the longest substring without repeating characters.
- Return `max_length`.



Time Complexity: 

O(n), where 
n is the length of the string s.
Space Complexity: 

O(min(m,n)), where 
m is the size of the character set (typically 128 for ASCII or up to 65,536 for Unicode).
