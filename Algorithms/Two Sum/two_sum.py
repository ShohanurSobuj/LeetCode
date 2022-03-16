# Source : https://leetcode.com/problems/two-sum/
# Author : Md. Shohanur Islam Sobuj
# Creation Time : 2022-03-16 23:24:50

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i] 
