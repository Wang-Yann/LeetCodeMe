#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 22:57:22
# @Last Modified : 2020-05-04 22:57:22
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启
# 则关闭）。第 i 轮，每 i 个灯泡切换一次开关。 对于第 n 轮，你只切换最后一个灯泡的开关。 找出 n 轮后有多少个亮着的灯泡。
#
#  示例:
#
#  输入: 3
# 输出: 1
# 解释:
# 初始时, 灯泡状态 [关闭, 关闭, 关闭].
# 第一轮后, 灯泡状态 [开启, 开启, 开启].
# 第二轮后, 灯泡状态 [开启, 关闭, 开启].
# 第三轮后, 灯泡状态 [开启, 关闭, 关闭].
#
# 你应该返回 1，因为只有一个灯泡还亮着。
#
#  Related Topics 脑筋急转弯 数学
#  👍 120 👎 0

import math

import pytest


class Solution:

    def bulbSwitch(self, n: int) -> int:
        """完全平方数的因数的个数是奇数个"""
        return int(math.sqrt(n))


@pytest.mark.parametrize("args,expected", [
    (3, 1),
])
def test_solutions(args, expected):
    assert Solution().bulbSwitch(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
