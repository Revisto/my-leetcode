from typing import List
from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbors = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                neighbors[pattern].append(word)

        visited = set()
        queue = deque([beginWord])

        steps = 1
        visited.add(beginWord)

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return steps

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for new_word in neighbors[pattern]:
                        if new_word not in visited:
                            visited.add(new_word)
                            queue.append(new_word)
            steps += 1
        return 0
