#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 14:11:03
# @Last Modified : 2020-07-27 14:11:03
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你和朋友玩一个叫做「翻转游戏」的游戏，游戏规则：给定一个只有 + 和 - 的字符串。你和朋友轮流将 连续 的两个 "++" 反转成 "--"。 当一方无法进
# 行有效的翻转时便意味着游戏结束，则另一方获胜。 
# 
#  请你写出一个函数来判定起始玩家是否存在必胜的方案。 
# 
#  示例： 
# 
#  输入: s = "++++"
# 输出: true 
# 解析: 起始玩家可将中间的 "++" 翻转变为 "+--+" 从而得胜。
#  
# 
#  延伸： 
# 请推导你算法的时间复杂度。 
#  Related Topics 极小化极大 回溯算法 
#  👍 38 👎 0

"""

import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    @functools.lru_cache(None)
    def canWin(self, s: str) -> bool:
        N = len(s)
        for i in range(N - 1):
            if s[i] == s[i + 1] == "+":
                #对方输掉
                if not self.canWin(s[:i] + "--" + s[i + 2:]):
                    return True
        return False


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s = "++++"), True],
])
def test_solutions(kw, expected):
    assert Solution().canWin(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
