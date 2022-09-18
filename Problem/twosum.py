## https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # lenth = len(nums)
        # for i in range(lenth-1):
        #     for j in range(i+1,lenth):
        #         if nums[i]+ nums[j] == target:
        #             return [i,j]
        hashmap = {}
        for i,v in enumerate(nums):
            dif = target - v
            if dif in hashmap:
                return [i,hashmap[dif]]
            else:
                hashmap[v] = i
        return