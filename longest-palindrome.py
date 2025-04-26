# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         letter_count = dict()
#         longest_palindrome = 0
#         the_odd_one = False
#         for letter in s:
#             letter_count[letter] = letter_count.get(letter, 0) + 1
        
#         for letter in letter_count:
#             if letter_count[letter] % 2 == 1 and the_odd_one is False:
#                 longest_palindrome += letter_count[letter]
#                 the_odd_one = True
#             elif letter_count[letter] % 2 == 1:
#                 longest_palindrome += letter_count[letter] - 1
#             else:
#                 longest_palindrome += letter_count[letter]
        
#         return longest_palindrome


class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest_palindrome = 0
        history = set()
        for letter in s:
            if letter in history:
                history.remove(letter)
                longest_palindrome += 2
            else:
                history.add(letter)
        if history != set():
            longest_palindrome += 1
        return longest_palindrome