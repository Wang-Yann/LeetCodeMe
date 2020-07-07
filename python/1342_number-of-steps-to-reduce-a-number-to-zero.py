#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：num = 14
# 输出：6
# 解释：
# 步骤 1) 14 是偶数，除以 2 得到 7 。
# 步骤 2） 7 是奇数，减 1 得到 6 。
# 步骤 3） 6 是偶数，除以 2 得到 3 。
# 步骤 4） 3 是奇数，减 1 得到 2 。
# 步骤 5） 2 是偶数，除以 2 得到 1 。
# 步骤 6） 1 是奇数，减 1 得到 0 。
#  
# 
#  示例 2： 
# 
#  输入：num = 8
# 输出：4
# 解释：
# 步骤 1） 8 是偶数，除以 2 得到 4 。
# 步骤 2） 4 是偶数，除以 2 得到 2 。
# 步骤 3） 2 是偶数，除以 2 得到 1 。
# 步骤 4） 1 是奇数，减 1 得到 0 。
#  
# 
#  示例 3： 
# 
#  输入：num = 123
# 输出：12
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= num <= 10^6 
#  
#  Related Topics 位运算

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num:
            if not num & 0b1:
                num >>= 1
            else:
                num -= 1
            cnt += 1
        return cnt


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(num=14), 6],
    [dict(num=123), 12],
])
def test_solutions(kw, expected):
    assert Solution().numberOfSteps(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
