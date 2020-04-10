
# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".

class Solution:
    def findEnding(self, S: str) -> str:
        skip = 0
        index = len(S) - 1
        while (index >= 0):
            if S[index] == '#':
                skip += 1 
            elif skip == 0:
                return S[:index+1] 
            else: 
                skip -= 1
            index -= 1   
        return ''

            
    def backspaceCompare(self, S: str, T: str) -> bool:
        while S != '' or T != '':
            s_substr = self.findEnding(S)
            t_substr = self.findEnding(T)
            print ('s', s_substr)
            print ('t', t_substr)
            if  s_substr == '' and t_substr == '':
                return True
            if s_substr == '' or t_substr == '' or s_substr[-1] != t_substr[-1]:
                return False
            S, T  = s_substr[: -1], t_substr[: -1]
   
        return True
