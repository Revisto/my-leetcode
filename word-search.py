from typing import List
from collections import deque, defaultdict


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        total_rows, total_cols = len(board), len(board[0])

        def search(row_index, col_index, char_index):
            if char_index == len(word):
                return True

            if (
                row_index < 0
                or row_index >= total_rows
                or col_index < 0
                or col_index >= total_cols
                or board[row_index][col_index] != word[char_index]
            ):
                return False

            saved_char = word[char_index]
            board[row_index][col_index] = "#"

            result = (
                search(row_index + 1, col_index, char_index + 1)
                or search(row_index - 1, col_index, char_index + 1)
                or search(row_index, col_index + 1, char_index + 1)
                or search(row_index, col_index - 1, char_index + 1)
            )
            board[row_index][col_index] = saved_char
            return result

        for row_index in range(total_rows):
            for col_index in range(total_cols):
                if board[row_index][col_index] == word[0]:
                    if search(row_index, col_index, 0):
                        return True
        return False


print(
    Solution().exist(
        board=[
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "B", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
        ],
        word="AB",
    )
)
