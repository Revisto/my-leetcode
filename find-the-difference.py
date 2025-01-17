class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_list = list(t)
        for letter in s:
            t_list.remove(letter)

        return t_list[0]
