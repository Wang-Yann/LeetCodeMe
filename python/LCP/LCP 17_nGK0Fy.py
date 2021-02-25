#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 21:21:57
# @Last Modified : 2021-02-25 21:21:57
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 小扣在秋日市集发现了一款速算机器人。店家对机器人说出两个数字（记作 `x` 和 `y`），请小扣说出计算指令：
# - `"A"` 运算：使 `x = 2 * x + y`；
# - `"B"` 运算：使 `y = 2 * y + x`。
# 
# 在本次游戏中，店家说出的数字为 `x = 1` 和 `y = 0`，小扣说出的计算指令记作仅由大写字母 `A`、`B` 组成的字符串 `s`，字符串中字符的
# 顺序表示计算顺序，请返回最终 `x` 与 `y` 的和为多少。
# 
# **示例 1：**
# >输入：`s = "AB"`
# > 
# >输出：`4`
# > 
# >解释：
# >经过一次 A 运算后，x = 2, y = 0。
# >再经过一次 B 运算，x = 2, y = 2。
# >最终 x 与 y 之和为 4。
# 
# **提示：**
# - `0 <= s.length <= 10`
# - `s` 由 `'A'` 和 `'B'` 组成
# 
# 
#  👍 18 👎 0
  

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def calculate(self, s: str) -> int:
        x, y = 1, 0
        for char in s:
            if char == "A":
                x = 2 * x + y
            elif char == "B":
                y = 2 * y + x
        return x + y


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="AB"), 4],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().calculate(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
