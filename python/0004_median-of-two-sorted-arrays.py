#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-07 11:58:54
# @Last Modified : 2020-04-07 11:58:54
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

"""https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-shu-b/

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


class Solution:
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


if __name__ == '__main__':
    sol = Solution()
    sample1 = [1, 2]
    sample2 = [3, 4]
    print(sol.findMedianSortedArrays(sample1, sample2))
