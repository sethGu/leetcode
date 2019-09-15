class Solution(object):
    def reverseParentheses(self, s):
        while '(' in s:
            posopen = s.rfind('(')
            posclose = s.find(')', posopen + 1)
            s = s[:posopen] + s[posopen + 1:posclose][::-1] + s[posclose + 1:]
        return s;

