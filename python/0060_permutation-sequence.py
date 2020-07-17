#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 13:58:41
# @Last Modified : 2020-05-04 13:58:41
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#
#  按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
#
#  "123"
#  "132"
#  "213"
#  "231"
#  "312"
#  "321"
#
#
#  给定 n 和 k，返回第 k 个排列。
#
#  说明：
#
#
#  给定 n 的范围是 [1, 9]。
#  给定 k 的范围是[1, n!]。
#
#
#  示例 1:
#
#  输入: n = 3, k = 3
# 输出: "213"
#
#
#  示例 2:
#
#  输入: n = 4, k = 9
# 输出: "2314"
#
#  Related Topics 数学 回溯算法
#  👍 276 👎 0

"""

import pytest


class Solution:

    def getPermutation(self, n: int, k: int) -> str:
        """https://leetcode-cn.com/problems/permutation-sequence/solution/di-k-ge-pai-lie-by-leetcode/
        算法
            生成输入数组，存储从 1 到 N 的数字。

            计算从 00 到  (N−1)! 的所有阶乘数。

            在  (0,N!−1) 区间内，k 重复减 1。

            计算 k 的阶乘，使用阶乘系数构造排列。

            返回排列字符串。

        """
        factorials, nums = [1], ["1"]
        for i in range(1, n):
            factorials.append(factorials[i - 1] * i)
            nums.append(str(i + 1))
        # fit k in the interval 0 ... (n! - 1)
        k -= 1
        output = []
        # compute factorial representation of k
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]

            output.append(nums[idx])
            nums.pop(idx)

        return "".join(output)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(n=3, k=3), "213"),
    pytest.param(dict(n=4, k=9), "2314"),
])
def test_solutions(kwargs, expected):
    assert Solution().getPermutation(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
