#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你和你的朋友，两个人一起玩 Nim 游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。 
# 
#  你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。 
# 
#  示例: 
# 
#  输入: 4
# 输出: false 
# 解释: 如果堆中有 4 块石头，那么你永远不会赢得比赛；
#      因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。
#  
#  Related Topics 脑筋急转弯 极小化极大

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    重点在于总是给对手留下4块石头，那么对手一定会输。

    """

    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (4, False),
    (2, True),
])
def test_solutions(args, expected):
    assert Solution().canWinNim(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
