# Valid Parentheses Checker

## Description
This Python class implements a method to validate if a string containing only the characters '(', ')', '{', '}', '[' and ']' is valid. A string is deemed valid if:
1. Every opening bracket has a corresponding closing bracket.
2. Brackets close in the correct order.

## Algorithm
The algorithm leverages a stack to manage opening brackets and ensures each one is correctly closed by its corresponding type in the right sequence.

### Steps:
1. **Initialize**:
   - Define a dictionary mapping each closing bracket to its corresponding opening bracket.
   - Initiate an empty stack to store opening brackets.

2. **Iterate through the string**:
   - For each character:
     - If it is a closing bracket (as identified in the dictionary):
       - Check if the stack is not empty and pop the top element.
       - Compare the popped element with the expected opening bracket from the dictionary.
       - If they do not match, or if the stack was empty when a closing bracket was encountered, return `False`.
     - If the character is an opening bracket, push it onto the stack.

3. **Final Check**:
   - After processing all characters, if the stack is not empty (indicating unmatched opening brackets), return `False`. Otherwise, return `True`.

## Complexity
- **Time Complexity**: `O(n)`, where `n` is the length of the string. Each character is processed exactly once.
- **Space Complexity**: `O(n)`, in the worst case where all characters are opening brackets.

## Usage
```python
sol = Solution()
print(sol.isValid("()"))         # Output: True
print(sol.isValid("()[]{}"))     # Output: True
print(sol.isValid("(]"))         # Output: False
print(sol.isValid("([])"))       # Output: True
