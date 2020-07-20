#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 00:28:13
# @Last Modified : 2020-04-24 00:28:13
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2
# ] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
#
#  示例 1：
#
#  输入：[3,4,5,1,2]
# 输出：1
#
#
#  示例 2：
#
#  输入：[2,2,2,0,1]
# 输出：0
#
#
#  注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sor
# ted-array-ii/
#  Related Topics 二分查找
#  👍 76 👎 0




from typing import List


class Solution:

    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return
        l, r = 0, len(numbers) - 1
        while l < r:
            mid = l + (r - l) // 2
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                r-=1
        return numbers[l]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [3, 4, 5, 1, 2], [2, 2, 2, 0, 1],[3,1,1],[2,2,3]

    ]
    res = [sol.minArray(args) for args in samples]
    print(res)
