#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-08 21:49:54
# @Last Modified : 2020-08-08 21:49:54
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s 和一个 长度相同 的整数数组 indices 。 
# 
#  请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。 
# 
#  返回重新排列后的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# 输出："leetcode"
# 解释：如图所示，"codeleet" 重新排列后变为 "leetcode" 。
#  
# 
#  示例 2： 
# 
#  输入：s = "abc", indices = [0,1,2]
# 输出："abc"
# 解释：重新排列后，每个字符都还留在原来的位置上。
#  
# 
#  示例 3： 
# 
#  输入：s = "aiohn", indices = [3,1,4,2,0]
# 输出："nihao"
#  
# 
#  示例 4： 
# 
#  输入：s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
# 输出："arigatou"
#  
# 
#  示例 5： 
# 
#  输入：s = "art", indices = [1,0,2]
# 输出："rat"
#  
# 
#  
# 
#  提示： 
# 
#  
#  s.length == indices.length == n 
#  1 <= n <= 100 
#  s 仅包含小写英文字母。 
#  0 <= indices[i] < n 
#  indices 的所有的值都是唯一的（也就是说，indices 是整数 0 到 n - 1 形成的一组排列）。 
#  
#  Related Topics 排序 
#  👍 5 👎 0
	 

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def restoreString(self, s: str, indices: List[int]) -> str:
        chars = [""] * len(s)
        for i, char in zip(indices, s):
            chars[i] = char
        return "".join(chars)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]), "leetcode"],
    [dict(s="abc", indices=[0, 1, 2]), "abc"],
    [dict(s="aiohn", indices=[3, 1, 4, 2, 0]), "nihao"],
    [dict(s="aaiougrt", indices=[4, 0, 2, 6, 7, 3, 1, 5]), "arigatou"],
    [dict(s="art", indices=[1, 0, 2]), "rat"],

])
def test_solutions(kwargs, expected):
    assert Solution().restoreString(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
