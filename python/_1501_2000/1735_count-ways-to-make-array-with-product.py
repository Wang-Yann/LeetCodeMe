#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 08:21:28
# @Last Modified : 2021-02-23 08:21:28
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个二维整数数组 queries ，其中 queries[i] = [ni, ki] 。第 i 个查询 queries[i] 要求构造长度为 ni 、每
# 个元素都是正整数的数组，且满足所有元素的乘积为 ki ，请你找出有多少种可行的方案。由于答案可能会很大，方案数需要对 109 + 7 取余 。 
# 
#  请你返回一个整数数组 answer，满足 answer.length == queries.length ，其中 answer[i]是第 i 个查询的结果
# 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：queries = [[2,6],[5,1],[73,660]]
# 输出：[4,1,50734910]
# 解释：每个查询之间彼此独立。
# [2,6]：总共有 4 种方案得到长度为 2 且乘积为 6 的数组：[1,6]，[2,3]，[3,2]，[6,1]。
# [5,1]：总共有 1 种方案得到长度为 5 且乘积为 1 的数组：[1,1,1,1,1]。
# [73,660]：总共有 1050734917 种方案得到长度为 73 且乘积为 660 的数组。1050734917 对 109 + 7 取余得到 507
# 34910 。
#  
# 
#  示例 2 ： 
# 
#  
# 输入：queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# 输出：[1,2,3,10,5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= queries.length <= 104 
#  1 <= ni, ki <= 104 
#  
#  Related Topics 数学 
#  👍 12 👎 0

"""

from typing import List

import pytest

# leetcode submit region begin(Prohibit modification and deletion)
try:
    from math import comb
except ImportError as e:
    from scipy.special import comb

primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)
MOD = 1000000007


class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        """
        把k个球放进n个不同的篮子里（不可以留空），有多少种放法
        答案很简单，就是C_{n+k-1}^{n-1}

        组合隔板法理解可以
        重复组合公式
        H(n,r) = C(n+r-1,r)

        两个 2 放进 4 个坑里，有多少种放法

        """

        def helper(n: int, k: int) -> int:
            res = 1
            for p in primes:
                r = 0
                while k % p == 0:
                    r += 1
                    k //= p
                res *= comb(n - 1 + r, r)
            if k != 1:
                # 如果最后 k > 1，那么说明 k 无法进一步被分解
                # 此时 k 是一个比较大的质数，比如 2377
                # 只要把 k 放在 n 个格子的任意一个位置，所以有 n 种放法
                res *= n
            return res % MOD

        return [helper(n, k) for n, k in queries]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(queries=[[2, 6], [5, 1], [73, 660]]), [4, 1, 50734910]],
    [dict(queries=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]), [1, 2, 3, 10, 5]],
])
def test_solutions(kw, expected):
    assert Solution().waysToFillArray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
