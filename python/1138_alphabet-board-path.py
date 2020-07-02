#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。 
# 
#  在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。 
# 
#  
# 
#  我们可以按下面的指令规则行动： 
# 
#  
#  如果方格存在，'U' 意味着将我们的位置上移一行； 
#  如果方格存在，'D' 意味着将我们的位置下移一行； 
#  如果方格存在，'L' 意味着将我们的位置左移一列； 
#  如果方格存在，'R' 意味着将我们的位置右移一列； 
#  '!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。 
#  
# 
#  （注意，字母板上只存在有字母的位置。） 
# 
#  返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。 
# 
#  
# 
#  示例 1： 
# 
#  输入：target = "leet"
# 输出："DDR!UURRR!!DDD!"
#  
# 
#  示例 2： 
# 
#  输入：target = "code"
# 输出："RR!DDRR!UUL!R!"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= target.length <= 100 
#  target 仅含有小写英文字母。 
#  
#  Related Topics 哈希表 字符串

"""
import string

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def alphabetBoardPath(self, target: str) -> str:
        """
        Notice that moving down and moving right,
        may move into a square that doesn't exist.
        To avoid this, we put L U before R D.
        """
        m = {c:[i // 5, i % 5] for i, c in enumerate(string.ascii_lowercase)}
        x0, y0 = 0, 0
        res = []
        for c in target:
            x, y = m[c]
            if y < y0:
                res.append('L' * (y0 - y))
            if x < x0:
                res.append('U' * (x0 - x))
            if x > x0:
                res.append('D' * (x - x0))
            if y > y0:
                res.append('R' * (y - y0))
            res.append('!')
            x0, y0 = x, y
        return "".join(res)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def alphabetBoardPath(self, target: str) -> str:
        pos = {}
        for i, char in enumerate(string.ascii_lowercase):
            pos[char] = (i % 5, i // 5)
        cur = "a"
        ans = ""
        for char in target:
            i, j = pos[char][0] - pos[cur][0], pos[char][1] - pos[cur][1]
            if char != "z":
                ans += ("U" if j < 0 else "D") * abs(j)
                ans += ("L" if i < 0 else "R") * abs(i)
            else:
                # 如果目标字母中含有'z'，我们应该先横向走，再纵向走，其余 情况都可以先纵向走，再横向走
                ans += ("L" if i < 0 else "R") * abs(i)
                ans += ("U" if j < 0 else "D") * abs(j)
            ans += "!"
            cur = char
        return ans


@pytest.mark.parametrize("args,expected", [
    ("leet", ["DDR!UURRR!!DDD!"]),
    pytest.param("code", ["RR!DDRR!UUL!R!", 'RR!DDRR!LUU!R!']),
    pytest.param("zdz", ["DDDDD!UUUUURRR!DDDDLLLD!", "DDDDD!UUUUURRR!LLLDDDDD!"]),
])
def test_solutions(args, expected):
    assert Solution().alphabetBoardPath(args) in expected
    assert Solution1().alphabetBoardPath(args) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
