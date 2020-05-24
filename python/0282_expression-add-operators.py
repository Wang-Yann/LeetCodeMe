#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加二元运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。 
# 
#  示例 1: 
# 
#  输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"] 
#  
# 
#  示例 2: 
# 
#  输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"] 
# 
#  示例 3: 
# 
#  输入: num = "105", target = 5
# 输出: ["1*0+5","10-5"] 
# 
#  示例 4: 
# 
#  输入: num = "00", target = 0
# 输出: ["0+0", "0-0", "0*0"]
#  
# 
#  示例 5: 
# 
#  输入: num = "3456237490", target = 9191
# 输出: []
#  
#  Related Topics 分治算法

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    about multiply
    for example, if you have a sequence of 12345 and you have proceeded to 1 + 2 + 3, now your eval is 6 right? If you want to add a * between 3 and 4, you would take 3 as the digit to be multiplied, so you want to take it out from the existing eval. You have 1 + 2 + 3 * 4 and the eval now is (1 + 2 + 3) - 3 + (3 * 4). Hope this could help
    """

    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(idx, tmp, tot, last):
            if idx == length:
                if tot == target:
                    res.append(tmp)
                return
            for i in range(idx, length):
                x = int(num[idx:i + 1])
                str_x = str(x)
                if idx == 0:
                    dfs(i + 1, str_x, x, x)
                else:
                    dfs(i + 1, tmp + "+" + str_x, tot + x, x)
                    dfs(i + 1, tmp + "-" + str_x, tot - x, -x)
                    dfs(i + 1, tmp + "*" + str_x, tot - last + last * x, last * x)
                if x == 0:
                    break

        res = []
        length = len(num)
        dfs(0, "", 0, 0)
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(num="123", target=6), ["1+2+3", "1*2*3"]),
    pytest.param(dict(num="232", target=8), ["2*3+2", "2+3*2"]),
    pytest.param(dict(num="105", target=5), ["1*0+5", "10-5"]),
    pytest.param(dict(num="00", target=0), ["0+0", "0-0", "0*0"]),
    pytest.param(dict(num="3456237490", target=9191), []),
])
def test_solutions(kwargs, expected):
    assert sorted(Solution().addOperators(**kwargs) )== sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
