#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-15 17:38:44
# @Last Modified : 2020-07-15 17:38:44
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 小A 和 小B 在玩猜数字。小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回 小
# A 猜对了几次？ 
# 
#  
# 
#  输入的guess数组为 小A 每次的猜测，answer数组为 小B 每次的选择。guess和answer的长度都等于3。 
# 
#  
# 
#  示例 1： 
# 
#  输入：guess = [1,2,3], answer = [1,2,3]
# 输出：3
# 解释：小A 每次都猜对了。 
# 
#  
# 
#  示例 2： 
# 
#  输入：guess = [2,2,3], answer = [3,2,1]
# 输出：1
# 解释：小A 只猜对了第二次。 
# 
#  
# 
#  限制： 
# 
#  
#  guess的长度 = 3 
#  answer的长度 = 3 
#  guess的元素取值为 {1, 2, 3} 之一。 
#  answer的元素取值为 {1, 2, 3} 之一。 
#  
#  👍 104 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(x == y for x, y in zip(guess, answer))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(guess=[1, 2, 3], answer=[1, 2, 3]), 3],
    [dict(guess=[2, 2, 3], answer=[3, 2, 1]), 1],
])
def test_solutions(kw, expected):
    assert Solution().game(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
