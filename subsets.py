from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = list()

        def find_subset(num_index, result):
            results.append(result)
            for new_num_index in range(num_index, len(nums)):
                find_subset(new_num_index + 1, result + [nums[new_num_index]])

        find_subset(0, [])
        return results


Solution().subsets([1, 2, 3])
