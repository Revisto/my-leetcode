class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        mapping = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for letter in s:
            needed_letter = mapping.get(letter, None)
            if needed_letter and stack and stack[-1] == needed_letter:
                stack.pop()
            else:
                stack.append(letter)
        if stack:
            return False
        return True