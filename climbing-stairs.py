class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(n):
            if n in memo:
                return memo[n]

            if n == 1:
                return 1
            if n == 2:
                return 2
            
            answer = climb(n - 1) + climb(n - 2)
            memo[n] = answer
            
            return answer

        return climb(n)

print(Solution().climbStairs(3))