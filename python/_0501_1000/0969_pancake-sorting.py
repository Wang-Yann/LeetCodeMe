#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 15:47:45
# @Last Modified : 2020-05-03 15:47:45
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定数组 A，我们可以对其进行煎饼翻转：我们选择一些正整数 k <= A.length，然后反转 A 的前 k 个元素的顺序。我们要执行零次或多次煎饼翻转（
# 按顺序一次接一次地进行）以完成对数组 A 的排序。
#
#  返回能使 A 排序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * A.length 范围内的有效答案都将被判断为正确。
#
#
#
#  示例 1：
#
#  输入：[3,2,4,1]
# 输出：[4,2,4,3]
# 解释：
# 我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
# 初始状态 A = [3, 2, 4, 1]
# 第一次翻转后 (k=4): A = [1, 4, 2, 3]
# 第二次翻转后 (k=2): A = [4, 1, 2, 3]
# 第三次翻转后 (k=4): A = [3, 2, 1, 4]
# 第四次翻转后 (k=3): A = [1, 2, 3, 4]，此时已完成排序。
#
#
#  示例 2：
#
#  输入：[1,2,3]
# 输出：[]
# 解释：
# 输入已经排序，因此不需要翻转任何内容。
# 请注意，其他可能的答案，如[3，3]，也将被接受。
#
#
#
#
#  提示：
#
#
#  1 <= A.length <= 100
#  A[i] 是 [1, 2, ..., A.length] 的排列
#
#  Related Topics 排序 数组
#  👍 59 👎 0

"""
import copy
from typing import List

import pytest


class Solution:

    def pancakeSort(self, A: List[int]) -> List[int]:
        """
        TODO
        20200503 官方解答错误,题目有问题
        """
        ans = []

        N = len(A)
        B = sorted(range(1, N + 1), key=lambda i: -A[i - 1])
        for i in B:
            for f in ans:
                if i <= f:
                    i = f + 1 - i
            ans.extend([i, N])
            N -= 1

        return ans


class Solution0:

    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        for x in range(len(A), 0, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
            # print(A,res)
        return res


class Solution1(object):
    def pancakeSort(self, A):
        def reverse(l, begin, end):
            for i in range((end - begin) // 2):
                l[begin + i], l[end - 1 - i] = l[end - 1 - i], l[begin + i]

        result = []
        for n in range(len(A), 0, -1):
            i = A.index(n)
            reverse(A, 0, i + 1)
            result.append(i + 1)
            reverse(A, 0, n)
            result.append(n)
        return result


@pytest.mark.parametrize("args,expected", [
    ([3, 2, 4, 1], [3, 4, 2, 3, 1, 2, 1, 1]),
    ([1, 2, 3], [3, 3, 2, 2, 1, 1]),
])
def test_solutions(args, expected):
    assert Solution().pancakeSort(copy.deepcopy(args)) == expected
    assert Solution0().pancakeSort(copy.deepcopy(args)) == expected
    assert Solution1().pancakeSort(copy.deepcopy(args)) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
