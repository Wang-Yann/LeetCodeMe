#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 18:02:48
# @Last Modified : 2020-07-10 18:02:48
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 salary ，数组里每个数都是 唯一 的，其中 salary[i] 是第 i 个员工的工资。 
# 
#  请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。 
# 
#  
# 
#  示例 1： 
# 
#  输入：salary = [4000,3000,1000,2000]
# 输出：2500.00000
# 解释：最低工资和最高工资分别是 1000 和 4000 。
# 去掉最低工资和最高工资以后的平均工资是 (2000+3000)/2= 2500
#  
# 
#  示例 2： 
# 
#  输入：salary = [1000,2000,3000]
# 输出：2000.00000
# 解释：最低工资和最高工资分别是 1000 和 3000 。
# 去掉最低工资和最高工资以后的平均工资是 (2000)/1= 2000
#  
# 
#  示例 3： 
# 
#  输入：salary = [6000,5000,4000,3000,2000,1000]
# 输出：3500.00000
#  
# 
#  示例 4： 
# 
#  输入：salary = [8000,9000,2000,3000,6000,1000]
# 输出：4750.00000
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= salary.length <= 100 
#  10^3 <= salary[i] <= 10^6 
#  salary[i] 是唯一的。 
#  与真实值误差在 10^-5 以内的结果都将视为正确答案。 
#  
#  Related Topics 排序 数组 
#  👍 2 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(salary=[4000, 3000, 1000, 2000]), 2500.00000],
    [dict(salary=[1000, 2000, 3000]), 2000.00000],
    [dict(salary=[6000, 5000, 4000, 3000, 2000, 1000]), 3500.00000],
    [dict(salary=[8000, 9000, 2000, 3000, 6000, 1000]), 4750.00000],
])
def test_solutions(kw, expected):
    assert Solution().average(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
