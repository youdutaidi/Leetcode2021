# bin/bash/python3

'''
===================================================
题目描述
4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
====================================================
实例：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
=======================================================
代码时间：2021.3.7 18:29
作者：Viviancat
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1=len(nums2)
        i=0
        while(i<len1):
            nums1.append(nums2[i])
            i+=1
        len2=len(nums1)
        nums1.sort()
        print(nums1)
        index1=len2/2
        index2=len2//2
        if(index1==index2):
            return (nums1[index2]+nums1[index2-1])/2
        else:
            return (nums1[index2])


