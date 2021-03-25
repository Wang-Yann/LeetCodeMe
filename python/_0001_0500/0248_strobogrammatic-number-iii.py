#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 22:49:56
# @Last Modified : 2020-07-21 22:49:56
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。 
# 
#  写一个函数来计算范围在 [low, high] 之间中心对称数的个数。 
# 
#  示例: 
# 
#  输入: low = "50", high = "100"
# 输出: 3 
# 解释: 69，88 和 96 是三个在该范围内的中心对称数 
# 
#  注意: 
# 由于范围可能很大，所以 low 和 high 都用字符串表示。 
#  Related Topics 递归 数学 
#  👍 20 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        """GOOD"""
        def find(path, size):
            if len(path) >= size:
                if len(path) != size or (size != 1 and path[0] == "0"):
                    return
                if (size == len(low) and path < low) or (size == len(high) and path > high):
                    return
                self.res += 1
            find("0" + path + "0", size)
            find("1" + path + "1", size)
            find("6" + path + "9", size)
            find("8" + path + "8", size)
            find("9" + path + "6", size)

        self.res = 0
        for i in range(len(low), len(high) + 1):
            find("", i)
            find("0", i)
            find("1", i)
            find("8", i)
        return self.res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(low="50", high="100"), 3],

])
def test_solutions(kwargs, expected):
    assert Solution().strobogrammaticInRange(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
