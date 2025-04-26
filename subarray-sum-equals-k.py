nums = [-1,-1,1]
t = 1


# p1 = 0
# current_sum = float("-inf")
# count = 0

# for p2 in range(len(nums)):
#     current_sum += nums[p2]
#     while current_sum >= t and p1 <= p2:
#         if current_sum == t:
#             count += 1
#         current_sum -= nums[p1]
#         p1 += 1

# print(count)


prefix_sum = 0
tracker = {0: 1}
count = 0

for num in nums:
    prefix_sum += num
    need = prefix_sum - t
    count += tracker.get(need, 0)
    tracker[prefix_sum] = tracker.get(prefix_sum, 0) + 1

print(count)