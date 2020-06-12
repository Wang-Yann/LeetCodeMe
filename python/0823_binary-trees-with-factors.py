#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给出一个含有不重复整数元素的数组，每个整数均大于 1。 
# 
#  我们用这些整数来构建二叉树，每个整数可以使用任意次数。 
# 
#  其中：每个非叶结点的值应等于它的两个子结点的值的乘积。 
# 
#  满足条件的二叉树一共有多少个？返回的结果应模除 10 ** 9 + 7。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: A = [2, 4]
# 输出: 3
# 解释: 我们可以得到这些二叉树: [2], [4], [4, 2, 2] 
# 
#  示例 2: 
# 
#  
# 输入: A = [2, 4, 5, 10]
# 输出: 7
# 解释: 我们可以得到这些二叉树: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]. 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= A.length <= 1000. 
#  2 <= A[i] <= 10 ^ 9. 
#  
# 

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        """
        令 dp[i] 表示已 A[i] 为树根的树的种类数
        """
        MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        dp = [1] * N
        index = {x:i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in range(i):
                if x % A[j] == 0:
                    right = x / A[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD
        return sum(dp) % MOD


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([2, 4], 3),
    pytest.param([2, 4, 5, 10], 7),
])
def test_solutions(args, expected):
    assert Solution().numFactoredBinaryTrees(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
