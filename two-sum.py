class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        for num1 in nums_set:
            ideal_num2 = target - num1
            if ideal_num2 == num1 and nums.count(num1) == 1:
                continue
            if ideal_num2 in nums_set:
                num1_index = nums.index(num1)
                return sorted([num1_index, nums[num1_index + 1:].index(ideal_num2) + num1_index + 1])