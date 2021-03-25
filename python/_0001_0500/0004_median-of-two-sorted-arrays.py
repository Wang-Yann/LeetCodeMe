#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-07 11:58:54
# @Last Modified : 2020-04-07 11:58:54
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
#
#  请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
#  你可以假设 nums1 和 nums2 不会同时为空。
#
#
#
#  示例 1:
#
#  nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
#  示例 2:
#
#  nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
#  Related Topics 数组 二分查找 分治算法

https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-shu-b/

else { // i is perfect
        int maxLeft;
        if (i == 0) {//A分成的leftA(空集) 和 rightA(A的全部)  所以leftPart = leftA(空集) + leftB,故maxLeft = B[j-1]。
            maxLeft = B[j - 1];
        } else if (j == 0) { //B分成的leftB(空集) 和 rightB(B的全部)  所以leftPart = leftA + leftB(空集),故maxLeft = A[i-1]。
            maxLeft = A[i - 1];
        } else { //排除上述两种特殊情况，正常比较
            maxLeft = Math.max(A[i - 1], B[j - 1]);
        }
        if ((m + n) % 2 == 1) { //奇数，中位数正好是maxLeft
            return maxLeft;
        }
        //偶数
        int minRight;
        if (i == m) {//A分成的leftA(A的全部) 和 rightA(空集)  所以rightPart = rightA(空集) + rightB,故minRight = B[j]。
            minRight = B[j];
        } else if (j == n) {//B分成的leftB(B的全部) 和 rightB(空集)  所以rightPart = rightA + rightB(空集),故minRight = A[i]。
            minRight = A[i];
        } else {//排除上述两种特殊情况，正常比较
            minRight = Math.min(B[j], A[i]);
        }

        return (maxLeft + minRight) / 2.0;
}


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def findKth(k):
            index_1, index_2 = 0, 0
            while True:
                if  index_1==len1 :
                    return nums2[index_2 + k - 1]
                if index_2==len2 :
                    return nums1[index_1 + k - 1]
                if k == 1:
                    return min(nums1[index_1], nums2[index_2])
                new_index_1 = min(index_1 + k // 2 - 1, len1 - 1)
                new_index_2 = min(index_2 + k // 2 - 1, len2 - 1)
                pivot1, pivot2 = nums1[new_index_1], nums2[new_index_2]
                if pivot1 <= pivot2:
                    k -= new_index_1 - index_1 + 1
                    index_1 = new_index_1 + 1
                else:
                    k -= new_index_2 - index_2 + 1
                    index_2 = new_index_2 + 1

        len1, len2 = len(nums1), len(nums2)
        N = len1 + len2
        if N % 2 == 1:
            return findKth((N + 1) // 2)
        else:
            return (findKth(N // 2) + findKth(N // 2 + 1)) / 2


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and j > 0 and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and j < n and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0




@pytest.mark.parametrize("kwargs,expected", [
    (dict(nums1=[1, 3], nums2=[2]), 2.0),
    pytest.param(dict(nums1=[1, 2], nums2=[3, 4]), 2.5),
])
def test_solutions(kwargs, expected):
    res = Solution().findMedianSortedArrays(**kwargs)
    res1 = Solution1().findMedianSortedArrays(**kwargs)
    assert res == pytest.approx(expected, 1e-2)
    assert res1 == pytest.approx(expected, 1e-2)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
