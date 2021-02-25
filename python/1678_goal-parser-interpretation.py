#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 23:26:55
# @Last Modified : 2021-02-25 23:26:55
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 请你设计一个可以解释字符串 command 的 Goal 解析器 。command 由 "G"、"()" 和/或 "(al)" 按某种顺序组成。Goal 解
# 析器会将 "G" 解释为字符串 "G"、"()" 解释为字符串 "o" ，"(al)" 解释为字符串 "al" 。然后，按原顺序将经解释得到的字符串连接成一个字
# 符串。 
# 
#  给你字符串 command ，返回 Goal 解析器 对 command 的解释结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：command = "G()(al)"
# 输出："Goal"
# 解释：Goal 解析器解释命令的步骤如下所示：
# G -> G
# () -> o
# (al) -> al
# 最后连接得到的结果是 "Goal"
#  
# 
#  示例 2： 
# 
#  输入：command = "G()()()()(al)"
# 输出："Gooooal"
#  
# 
#  示例 3： 
# 
#  输入：command = "(al)G(al)()()G"
# 输出："alGalooG"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= command.length <= 100 
#  command 由 "G"、"()" 和/或 "(al)" 按某种顺序组成 
#  
#  Related Topics 字符串 
#  👍 13 👎 0
  

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(command="G()(al)"), "Goal"],
    [dict(command="G()()()()(al)"), "Gooooal"],
    [dict(command="(al)G(al)()()G"), "alGalooG"],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().interpret(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
