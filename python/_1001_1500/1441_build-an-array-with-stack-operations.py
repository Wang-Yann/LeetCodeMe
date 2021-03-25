#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-09 21:56:25
# @Last Modified : 2020-07-09 21:56:25
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""

# 给你一个目标数组 target 和一个整数 n。每次迭代，需要从 list = {1,2,3..., n} 中依序读取一个数字。 
# 
#  请使用下述操作来构建目标数组 target ： 
# 
#  
#  Push：从 list 中读取一个新元素， 并将其推入数组中。 
#  Pop：删除数组中的最后一个元素。 
#  如果目标数组构建完成，就停止读取更多元素。 
#  
# 
#  题目数据保证目标数组严格递增，并且只包含 1 到 n 之间的数字。 
# 
#  请返回构建目标数组所用的操作序列。 
# 
#  题目数据保证答案是唯一的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：target = [1,3], n = 3
# 输出：["Push","Push","Pop","Push"]
# 解释： 
# 读取 1 并自动推入数组 -> [1]
# 读取 2 并自动推入数组，然后删除它 -> [1]
# 读取 3 并自动推入数组 -> [1,3]
#  
# 
#  示例 2： 
# 
#  输入：target = [1,2,3], n = 3
# 输出：["Push","Push","Push"]
#  
# 
#  示例 3： 
# 
#  输入：target = [1,2], n = 4
# 输出：["Push","Push"]
# 解释：只需要读取前 2 个数字就可以停止。
#  
# 
#  示例 4： 
# 
#  输入：target = [2,3,4], n = 4
# 输出：["Push","Pop","Push","Push","Push"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= target.length <= 100 
#  1 <= target[i] <= 100 
#  1 <= n <= 100 
#  target 是严格递增的 
#  
#  Related Topics 栈 
#  👍 4 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def buildArray(self, target: List[int], n: int) -> List[str]:
        """AC"""
        stack = []
        ans = []
        N = len(target)
        i = 0
        for v in range(1, n + 1):
            if i == N:
                break
            stack.append(v)
            ans.append("Push")
            if v != target[i]:
                ans.append("Pop")
            else:
                i += 1

        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(target=[1, 3], n=3), ["Push", "Push", "Pop", "Push"]],
    [dict(target=[1, 2, 3], n=3), ["Push", "Push", "Push"]],
    [dict(target=[1, 2], n=4), ["Push", "Push"]],
    [dict(target=[2, 3, 4], n=4), ["Push", "Pop", "Push", "Push", "Push"]],

])
def test_solutions(kwargs, expected):
    assert Solution().buildArray(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
