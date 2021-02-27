#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 17:12:18
# @Last Modified : 2021-02-27 17:12:18
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个只包含字符 'a'，'b' 和 'c' 的字符串 s ，你可以执行下面这个操作（5 个步骤）任意次： 
# 
#  
#  选择字符串 s 一个 非空 的前缀，这个前缀的所有字符都相同。 
#  选择字符串 s 一个 非空 的后缀，这个后缀的所有字符都相同。 
#  前缀和后缀在字符串中任意位置都不能有交集。 
#  前缀和后缀包含的所有字符都要相同。 
#  同时删除前缀和后缀。 
#  
# 
#  请你返回对字符串 s 执行上面操作任意次以后（可能 0 次），能得到的 最短长度 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ca"
# 输出：2
# 解释：你没法删除任何一个字符，所以字符串长度仍然保持不变。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cabaabac"
# 输出：0
# 解释：最优操作序列为：
# - 选择前缀 "c" 和后缀 "c" 并删除它们，得到 s = "abaaba" 。
# - 选择前缀 "a" 和后缀 "a" 并删除它们，得到 s = "baab" 。
# - 选择前缀 "b" 和后缀 "b" 并删除它们，得到 s = "aa" 。
# - 选择前缀 "a" 和后缀 "a" 并删除它们，得到 s = "" 。 
# 
#  示例 3： 
# 
#  
# 输入：s = "aabccabba"
# 输出：3
# 解释：最优操作序列为：
# - 选择前缀 "aa" 和后缀 "a" 并删除它们，得到 s = "bccabb" 。
# - 选择前缀 "b" 和后缀 "bb" 并删除它们，得到 s = "cca" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 105 
#  s 只包含字符 'a'，'b' 和 'c' 。 
#  
#  Related Topics 双指针 
#  👍 2 👎 0
  

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minimumLength(self, s: str) -> int:
        while len(s) > 1 and s[0] == s[-1]:
            s = s.strip(s[0])
        return len(s)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="ca"), 2],
    [dict(s="cabaabac"), 0],
    [dict(s="aabccabba"), 3],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().minimumLength(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
