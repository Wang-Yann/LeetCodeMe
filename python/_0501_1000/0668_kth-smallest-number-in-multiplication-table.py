#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 23:30:14
# @Last Modified : 2020-05-01 23:30:14
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？
#
#  给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。
#
#  例 1：
#
#
# 输入: m = 3, n = 3, k = 5
# 输出: 3
# 解释:
# 乘法表:
# 1	2	3
# 2	4	6
# 3	6	9
#
# 第5小的数字是 3 (1, 2, 2, 3, 3).
#
#
#  例 2：
#
#
# 输入: m = 2, n = 3, k = 6
# 输出: 6
# 解释:
# 乘法表:
# 1	2	3
# 2	4	6
#
# 第6小的数字是 6 (1, 2, 2, 3, 4, 6).
#
#
#  注意：
#
#
#  m 和 n 的范围在 [1, 30000] 之间。
#  k 的范围在 [1, m * n] 之间。
#
#  Related Topics 二分查找
#  👍 91 👎 0

import pytest


class Solution:

    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def count(num, m, n):
            # ：获得在m*n的乘法表中，找出有多少个值 <= num。返回满足条件的值的数量
            # num这个值在当前第i行，有多少个值不比它大（<=num的个数
            # for(int i = 1; i<=m; ++i)//行从第一行开始
            # count += min(num/i, n);//此表达式的含义：num这个值在当前第i行，有多少个值不比它大（<=num的个数）
            return sum(min(num // i, n) for i in range(1, m + 1))

        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) >> 1
            # print("count" ,count(mid, m, n)    )
            # 得到在乘法表中 值 <= mid 的数量
            if count(mid, m, n) >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l


@pytest.mark.parametrize("kwargs,expected", [
    (dict(m=3, n=3, k=7), 6),
    pytest.param(dict(m=2, n=3, k=6), 6),
])
def test_solutions(kwargs, expected):
    assert Solution().findKthNumber(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
