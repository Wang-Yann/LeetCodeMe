#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。 
# 
#  注意：本题中，每个活字字模只能使用一次。 
# 
#  
# 
#  示例 1： 
# 
#  输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
#  
# 
#  示例 2： 
# 
#  输入："AAABBC"
# 输出：188
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= tiles.length <= 7 
#  tiles 由大写英文字母组成 
#  
#  Related Topics 回溯算法

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = collections.Counter(tiles)

        def backtrack(counter):
            total = 0
            for k, v in counter.items():
                if not v:
                    continue
                counter[k] -= 1
                total += backtrack(counter) + 1
                counter[k] += 1
            return total

        return backtrack(count)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("AAB", 8),
    ("AAABBC", 188),
])
def test_solutions(args, expected):
    assert Solution().numTilePossibilities(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
