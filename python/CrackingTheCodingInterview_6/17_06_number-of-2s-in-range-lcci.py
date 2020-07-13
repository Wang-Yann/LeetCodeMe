#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 22:13:58
# @Last Modified : 2020-07-13 22:13:58
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。 
# 
#  示例: 
# 
#  输入: 25
# 输出: 9
# 解释: (2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次) 
# 
#  提示： 
# 
#  
#  n <= 10^9 
#  
#  Related Topics 数学 动态规划 
#  👍 18 👎 0


"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numberOf2sInRange(self, n: int) -> int:
        """
        https://leetcode-cn.com/problems/number-of-2s-in-range-lcci/solution/xiao-xue-sheng-du-neng-kan-dong-de-zhao-gui-lu-fa-/
        """
        s = str(n)
        count = 0
        for i in range(len(s)):
            current = int(s[i])
            high = int(s[:i] or "0")
            low = int(s[i + 1:] or "0")
            if current > 2:
                count += (high + 1) * (10 ** len(s[i + 1:]))
            elif current < 2:
                count += high * (10 ** len(s[i + 1:]))
            else:
                count += high * (10 ** len(s[i + 1:])) + low + 1
        return count


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (25, 9),
])
def test_solutions(args, expected):
    assert Solution().numberOf2sInRange(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
