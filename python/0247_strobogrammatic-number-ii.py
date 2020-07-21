#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 22:11:41
# @Last Modified : 2020-07-21 22:11:41
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。 
# 
#  找到所有长度为 n 的中心对称数。 
# 
#  示例 : 
# 
#  输入:  n = 2
# 输出: ["11","69","88","96"]
#  
#  Related Topics 递归 数学 
#  👍 26 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findStrobogrammatic(self, n: int) -> List[str]:
        lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

        def helper(k):
            if k == 0:
                return [""]
            elif k == 1:
                return ["0", "1", "8"]
            res = []
            for num_mid in helper(k - 2):
                for key, val in lookup.items():
                    #   n==k 表示最外层处理
                    #  // 例如：原始需求n=m=2, '00'不合法
                    # // 若原始需求n=m=4, 内层循环n=2,m=4,'00';最外层循环，n=m=4时，'1001'

                    if n == k and key == "0":
                        continue
                    res.append(key + num_mid + val)
            # print(res)
            return res

        return helper(n)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=2), ["11", "69", "88", "96"]],
    [dict(n=4), ['1001', '6009', '8008', '9006', '1111', '6119', '8118', '9116', '1691',
                 '6699', '8698', '9696', '1881', '6889', '8888', '9886', '1961', '6969', '8968', '9966']],

])
def test_solutions(kwargs, expected):
    assert sorted(Solution().findStrobogrammatic(**kwargs)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
