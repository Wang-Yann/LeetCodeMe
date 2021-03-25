#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 16:05:50
# @Last Modified : 2020-07-27 16:05:50
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 请你写出一个能够举单词全部缩写的函数。 
# 
#  注意：输出的顺序并不重要。 
# 
#  示例： 
# 
#  输入: "word"
# 输出:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", 
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
#  
# 
#  
#  Related Topics 位运算 回溯算法 
#  👍 19 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        """clear"""

        def backtrack(pos, cur, count):
            if pos == len(word):
                if count > 0:
                    cur = cur + str(count)
                res.append(cur)
            else:
                backtrack(pos + 1, cur, count + 1)
                if count > 0:
                    cur = cur + str(count) + word[pos]
                else:
                    cur = cur + word[pos]
                backtrack(pos + 1, cur, 0)

        res = []
        backtrack(0, "", 0)
        return res


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def generateAbbreviations(self, word: str) -> List[str]:
        N = len(word)
        ans = []

        def backtrack(pos, path):
            if pos == N:
                ans.append("".join(path))
                return
            path.append(word[pos])
            backtrack(pos + 1, path)
            path.pop()
            if not path or not path[-1].isdigit():
                for i in range(1, N - pos + 1):
                    path.append(str(i))
                    backtrack(pos + i, path)
                    path.pop()

        backtrack(0, [])
        return ans


@pytest.mark.parametrize("args,expected", [
    ("word", ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d",
              "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"])
])
def test_solutions(args, expected):
    assert sorted(Solution().generateAbbreviations(args)) == sorted(expected)
    assert sorted(Solution1().generateAbbreviations(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
