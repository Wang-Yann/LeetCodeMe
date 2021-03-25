#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 11:43:40
# @Last Modified : 2021-02-27 11:43:40
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。 
# 
#  它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。比方说
# ，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。 
# 
#  给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。 
# 
#  
# 
#  示例 1： 
# 
#  输入：encoded = [3,1]
# 输出：[1,2,3]
# 解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
#  
# 
#  示例 2： 
# 
#  输入：encoded = [6,5,4,6]
# 输出：[2,4,1,5,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= n < 105 
#  n 是奇数。 
#  encoded.length == n - 1 
#  
#  Related Topics 位运算 
#  👍 16 👎 0
  

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def decode(self, encoded: List[int]) -> List[int]:
        """抓住条件"""
        N = len(encoded)
        byall = 0  # 全部 n 个正整数的异或值
        for i in range(N + 2):
            byall ^= i
        all_but_first = 0  # 除开第一个数的异或值
        for i in range(1, N, 2):
            all_but_first ^= encoded[i]
        ans = [byall ^ all_but_first]  # 得到第一个数
        for i in range(N):
            ans.append(ans[i] ^ encoded[i])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(encoded=[6, 5, 4, 6]), [2, 4, 1, 5, 3]],
    [dict(encoded=[3, 1]), [1, 2, 3]],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().decode(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
