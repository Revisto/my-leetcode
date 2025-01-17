class Solution:
    def threeSum(self, nums):
        answers = set()
        for num1_index in range(len(nums)):
            for num2_index in range(len(nums)):
                if num1_index == num2_index:
                    continue
                num1 = nums[num1_index]
                num2 = nums[num2_index]
                if (-(num1 + num2)) in set(nums[num2_index + 1 :]):
                    answers.add(tuple(sorted([num1, num2, -(num1 + num2)])))
        return list(answers)
