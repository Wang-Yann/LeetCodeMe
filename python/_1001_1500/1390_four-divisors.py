#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums，请你返回该数组中恰有四个因数的这些整数的各因数之和。 
# 
#  如果数组中不存在满足题意的整数，则返回 0 。 
# 
#  
# 
#  示例： 
# 
#  输入：nums = [21,4,7]
# 输出：32
# 解释：
# 21 有 4 个因数：1, 3, 7, 21
# 4 有 3 个因数：1, 2, 4
# 7 有 2 个因数：1, 7
# 答案仅为 21 的所有因数的和。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^4 
#  1 <= nums[i] <= 10^5 
#  
#  Related Topics 数学

"""

import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            divisor = set()
            for i in range(1, math.floor(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisor.add(num // i)
                    divisor.add(i)
                if len(divisor) > 4:
                    break
            if len(divisor) == 4:
                res += sum(divisor)
        return res


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # C 是数组 nums 元素的上限，C3 是 C 的立方根
        C, C3 = 100000, 46

        isprime = [True] * (C + 1)
        primes = list()

        # 埃拉托斯特尼筛法
        for i in range(2, C + 1):
            if isprime[i]:
                primes.append(i)
            for j in range(i + i, C + 1, i):
                isprime[j] = False

        # 欧拉筛法
        """
        for i in range(2, C + 1):
            if isprime[i]:
                primes.append(i)
            for prime in primes:
                if i * prime > C:
                    break
                isprime[i * prime] = False
                # 换言之，i 之前被 pri[j] 筛过了
                # 由于 pri 里面质数是从小到大的，所以 i 乘上其他的质数的结果一定也是
                # pri[j] 的倍数 它们都被筛过了，就不需要再筛了，所以这里直接 break
                # 掉就好了
                if i % prime == 0:
                    break
        """

        # 通过质数表构造出所有的四因数
        # 根据「算数基本定理」（又叫「唯一分解定理」
        factor4 = dict()
        for prime in primes:
            if prime <= C3:
                factor4[prime ** 3] = 1 + prime + prime ** 2 + prime ** 3
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                if primes[i] * primes[j] <= C:
                    factor4[primes[i] * primes[j]] = 1 + primes[i] + primes[j] + primes[i] * primes[j]
                else:
                    break
        # print(factor4)
        ans = 0
        for num in nums:
            if num in factor4:
                ans += factor4[num]
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[21, 4, 7]), 32],
])
def test_solutions(kw, expected):
    assert Solution().sumFourDivisors(**kw) == expected
    assert Solution1().sumFourDivisors(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
