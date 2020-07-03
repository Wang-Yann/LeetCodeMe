#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。 
# 
#  让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。 
# 
#  由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 5
# 输出：12
# 解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。
#  
# 
#  示例 2： 
# 
#  输入：n = 100
# 输出：682289015
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 100 
#  
#  Related Topics 数学

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        primes_list = [2, 3]
        for i in range(5, n + 1, 2):
            if any(i % v == 0 for v in primes_list):
                continue
            primes_list.append(i)
        prime_cnt = sum(x <= n for x in primes_list)

        # print(prime_cnt,n-prime_cnt)
        def factorial(num):
            result = 1
            for i in range(2, num + 1):
                result = (result * i) % MOD
            return result

        return factorial(prime_cnt) * factorial(n - prime_cnt) % MOD


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (1, 1),
    (2, 1),
    (4, 4),
    (5, 12),
    (100, 682289015),
])
def test_solutions(args, expected):
    assert Solution().numPrimeArrangements(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
