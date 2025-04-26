# class Solution:
#     def rob(self, nums):
#         memo = {}
#         def rob_one_house(houses, amount):
#             max_amount = amount
#             tuple_houses = tuple(houses)
#             if len(houses) == 1:
#                 return amount + houses[0]
#             if len(houses) == 0:
#                 return amount
#             if tuple_houses in memo:
#                 return memo[tuple_houses]
#             for house_index in range(len(houses)):
#                 houses_without_adjacents = houses.copy()
#                 if house_index != (len(houses) - 1):
#                     houses_without_adjacents.pop(house_index + 1)
#                 houses_without_adjacents.pop(house_index)
#                 if house_index != 0:
#                     houses_without_adjacents.pop(house_index - 1)
#                 max_amount = max(rob_one_house(houses_without_adjacents, amount + houses[house_index]), max_amount)
#             memo[tuple_houses] = max_amount
#             return max_amount
#         return rob_one_house(nums, 0)

class Solution:
    def rob(self, nums):
        memo = dict()
        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            robbed_amount = nums[i] + dp(i + 2)
            skipped_amount = dp(i + 1)
            
            max_amount = max(robbed_amount, skipped_amount)
            memo[i] = max_amount
            
            return max_amount
        return dp(0)


print(Solution().rob([2,7,9,3,1]))