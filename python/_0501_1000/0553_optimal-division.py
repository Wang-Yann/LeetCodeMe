
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 16:39:44
# @Last Modified : 2020-05-05 16:39:44
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def optimalDivision(self, nums: List[int]) -> str:
        """
        考虑输入形如 [a,b,c,d] 的列表，我们需要设置一些运算优先级来最大化 a/b/c/d。我们知道为了最大化 p/qp/q，分母 qq 应该最小化，所以为了最大化 a/b/c/da/b/c/d 我们首先需要最小化 b/c/d，现在我们的目标变成了最小化表达式 b/c/d。

        """
        length = len(nums)
        if length == 1:
            return str(nums[0])
        elif length == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            res = [str(nums[0]) + "/(" + str(nums[1])]
            for i in range(2, length):
                res += "/" + str(nums[i])
            res += ")"
            return "".join(res)


@pytest.mark.parametrize("args,expected", [
    ([1000, 100, 10, 2], "1000/(100/10/2)"),
])
def test_solutions(args, expected):
    assert Solution().optimalDivision(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
