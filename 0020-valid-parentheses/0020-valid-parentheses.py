class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 !=0 :
            return False 
        bracket_dictionary ={')':'(','}':'{',']':'['}
        closing_brackets = set(bracket_dictionary.keys())
        stack =[]
        for char in s :
            if char in closing_brackets:
                top_element = stack.pop() if stack else '#'
                if bracket_dictionary[char] != top_element:
                    return False
            else:
                stack.append (char)
        
        return not stack 
        