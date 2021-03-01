#! usr/bin/python3
'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

'''

class Solution(object):
    def twoSum(self,nums, target):
        lens=len(nums)
        for i in range(lens):
            if (target - nums[i]) in nums:
                if nums.index(target-nums[i])==i and nums.count(nums[i])==1:
                    continue
                else:
                    j=nums.index(target-nums[i])
                    if j >=0:
                        break
        if j>=0:
            return [i,j]
        else:
            return []
'''
python基础题目，基础解法，后续有时间可以补上其他解法，目前是为了练习python编成

'''
