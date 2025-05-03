class Solution:
    def dailyTemperatures(self, temperatures):
        days = [0] * len(temperatures)
        stack = list()
        for i in range(len(temperatures)):
            temperature = temperatures[i]

            while stack and temperatures[stack[-1]] < temperature:
                popped_index = stack.pop()
                days[popped_index] = i - popped_index
            stack.append(i)
        return days


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
