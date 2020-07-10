#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 18:54:40
# @Last Modified : 2020-07-10 18:54:40
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 path，其中 path[i] 的值可以是 'N'、'S'、'E' 或者 'W'，分别表示向北、向南、向东、向西移动一个单位。 
# 
#  机器人从二维平面上的原点 (0, 0) 处开始出发，按 path 所指示的路径行走。 
# 
#  如果路径在任何位置上出现相交的情况，也就是走到之前已经走过的位置，请返回 True ；否则，返回 False 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：path = "NES"
# 输出：false 
# 解释：该路径没有在任何位置相交。 
# 
#  示例 2： 
# 
#  
# 
#  输入：path = "NESWW"
# 输出：true
# 解释：该路径经过原点两次。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= path.length <= 10^4 
#  path 仅由 {'N', 'S', 'E', 'W} 中的字符组成 
#  
#  Related Topics 字符串 
#  👍 5 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """AC"""
        pos = (0, 0)
        seen = {pos}
        directions = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0),
        }
        for char in path:
            x, y = directions[char]
            new_pos = pos[0] + x, pos[1] + y
            if new_pos in seen:
                return True
            pos = new_pos
            seen.add(pos)
        return False


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(path="NES"), False],
    [dict(path="NESWW"), True],
])
def test_solutions(kw, expected):
    assert Solution().isPathCrossing(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
