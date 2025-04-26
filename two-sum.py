class Solution:
    def twoSum(self, nums, target: int):
        nums_count = dict()
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
        
        for num in nums_count:
            desired_num = target - num
            desired_num_count = nums_count.get(desired_num, 0)
            if (desired_num == num and desired_num_count >= 2):
                first_index = nums.index(num)
                second_infex = nums[first_index + 1:].index(desired_num) + first_index + 1
                return [first_index, second_infex]
                
            if (desired_num != num and desired_num_count >= 1):
                first_index = nums.index(num)
                second_infex = nums.index(desired_num)
                return [first_index, second_infex]
print(Solution().twoSum([3,3], 6))