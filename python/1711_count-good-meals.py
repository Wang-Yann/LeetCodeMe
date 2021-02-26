#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-26 09:24:38
# @Last Modified : 2021-02-26 09:24:38
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。
#
#  你可以搭配 任意 两道餐品做一顿大餐。
#
#  给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大
# 餐 的数量。结果需要对 109 + 7 取余。
#
#  注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。
#
#
#
#  示例 1：
#
#
# 输入：deliciousness = [1,3,5,7,9]
# 输出：4
# 解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
# 它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。
#
#
#  示例 2：
#
#
# 输入：deliciousness = [1,1,1,3,3,3,7]
# 输出：15
# 解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。
#
#
#
#  提示：
#
#
#  1 <= deliciousness.length <= 10**5
#           TODO 嘿　插件不显示害人
#  0 <= deliciousness[i] <= 2**20
#
#  Related Topics 数组 哈希表 双指针
#  👍 22 👎 0
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10 ** 9 + 7
        lookup = {2 ** i for i in range(22)}
        counter = collections.Counter()
        ans = 0
        # 类似于 TwoSum
        for x in deliciousness:
            for sum_val in lookup:
                ans += counter[sum_val - x]
            counter[x] += 1
        return ans % MOD


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(deliciousness=[1, 3, 5, 7, 9]), 4],
    [dict(deliciousness=[1, 1, 1, 3, 3, 3, 7]), 15],
    [dict(deliciousness=[149, 107, 1, 63, 0, 1, 6867, 1325, 5611, 2581, 39, 89, 46, 18, 12, 20, 22, 234]), 12],
])
@pytest.mark.parametrize("SolutionCLS", [Solution])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().countPairs(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
