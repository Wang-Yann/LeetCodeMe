#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方
# 法，生成跳水板所有可能的长度。 
#  返回的长度需要从小到大排列。 
#  示例： 
#  输入：
# shorter = 1
# longer = 2
# k = 3
# 输出： {3,4,5,6}
#  
#  提示： 
#  
#  0 < shorter <= longer 
#  0 <= k <= 100000 
#  
#  Related Topics 递归 记忆化

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        ans = set()
        for i in range(k + 1):
            j = k - i
            ans.add(shorter * i + longer * j)
        return sorted(ans)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(shorter=1, longer=2, k=3), [3, 4, 5, 6]],
    [dict(shorter=1, longer=1, k=0), []],
])
def test_solutions(kw, expected):
    assert Solution().divingBoard(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
