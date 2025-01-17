class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

        # if needle in haystack:
        #     for i_haystack in range(len(haystack)):
        #         output = i_haystack
        #         if haystack[i_haystack] == needle[0]:
        #             for i_needle in range(1, len(needle)):
        #                 if haystack[i_haystack + i_needle] != needle[i_needle]:
        #                     break
        #             else:
        #                 return output
        # return -1
