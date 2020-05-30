#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。 
# 
#  示例: 
# 
#  
# nums = [1, 2, 3]
# target = 4
# 
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 
# 请注意，顺序不同的序列被视作不同的组合。
# 
# 因此输出为 7。
#  
# 
#  进阶： 
# 如果给定的数组中含有负数会怎么样？ 
# 问题会产生什么变化？ 
# 我们需要在题目中添加什么限制来允许负数的出现？ 
# 
#  致谢： 
# 特别感谢 @pbrother 添加此问题并创建所有测试用例。 
#  Related Topics 动态规划

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    https://leetcode-cn.com/problems/combination-sum-iv/solution/xi-wang-yong-yi-chong-gui-lu-gao-ding-bei-bao-wen-/
    """

    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        动态规划基础应用。简化成爬楼梯，题目例子[1,2,3], target = 4, 想象成一共4 级楼梯，每次只能爬 1、2、3 级，一共有多少种爬法。
        DP思路：
            1.状态
            - 最后一步从 (target - num) 开始走，target = 4, num 为 1，2，3
            - 子问题：target - 1， target - 2， 。。。， target = 0
            2.转移方程
            - f[i] = f[i - 1] + f[i - 2] + f[i - 3]
            3.初始条件和边界条件
            - f[0] = 1
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    continue
                dp[i] += dp[i - num]
        return dp[target]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        nums=[1, 2, 3],
        target=4
    ), 7),
])
def test_solutions(kwargs, expected):
    assert Solution().combinationSum4(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
