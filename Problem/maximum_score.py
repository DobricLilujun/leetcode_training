# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/solution/

from hashlib import new
from turtle import right


class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        # Approach 2 recursive dynamic programming
        # memo = {}
        # m = len(multipliers)
        # n = len(nums)
        # def score(op, left):
        #     if op == m:
        #         return 0
        #     if (op, left) in memo:
        #         return memo[(op,left)]
            
        #     l = nums[left] * multipliers[op] + score(op+1, left+1)
        #     r = nums[(n-1)-(op-left)] * multipliers[op] + score(op+1, left)
        #     memo[(op, left)] = max(l, r)
        #     return (memo[(op,left)])
        # return score(0,0)

        # Approach 3 simplification of recursive dynamic programming
        m = len(multipliers)
        n = len(nums)
        dp = [[0]*(m+1) for i in range(m+1)]
        for j in range(m-1, -1, -1):
            for low in range(j, -1, -1):
                first = nums[low]* multipliers[j] + dp[j+1][low+1]
                last  = nums[n-1 - (j-low)]* multipliers[j] + dp[j+1][low]
                dp[j][low] = max(first,last)
            print (dp)
        return dp[0][0]


if __name__ == '__main__':
    A = Solution()
    a = [1,2,3]
    b = [3,2,1]
    print (A.maximumScore(a,b))
