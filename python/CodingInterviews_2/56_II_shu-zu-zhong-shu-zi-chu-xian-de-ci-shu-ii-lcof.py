#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [3,4,3,3]
# 输出：4
#  
# 
#  示例 2： 
# 
#  输入：nums = [9,1,7,9,7,9,7]
# 输出：1 
# 
#  
# 
#  限制： 
# 
#  
#  1 <= nums.length <= 10000 
#  1 <= nums[i] < 2^31 
#  
# 
#  
# 

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        """
        1 <= nums[i] < 2^31
        为什么Python最后需要对返回值进行判断？
如果不这么做的话测试用例是[-2,-2,1,1,-3,1,-3,-3,-4,-2] 的时候，就会输出 4294967292。 其原因在于Python是动态类型语言，在这种情况下其会将符号位置的1看成了值，而不是当作符号“负数”。 这是不对的。 正确答案应该是 - 4，-4的二进制码是 1111...100，就变成 2^32-4=4294967292，解决办法就是 减去 2 ** 32 。

之所以这样不会有问题的原因还在于题目限定的数组范围不会超过 2 ** 32

        """
        res = 0
        for i in range(32):
            cnt = 0
            bit = 1 << i  # 记录当前要操作的 bit
            for num in nums:
                if num & bit:
                    cnt += 1
            if cnt % 3 != 0:
                # 不等于0说明唯一出现的数字在这个 bit 上是1
                res |= bit
        return res


# leetcode submit region end(Prohibit modification and deletion)

class Solution3:

    def singleNumber(self, nums: List[int]) -> int:
        """
        https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/solution/mian-shi-ti-56-ii-shu-zu-zhong-shu-zi-chu-xian-d-4/
        """
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones


@pytest.mark.parametrize("args,expected", [
    ([3, 4, 3, 3], 4),
    # ([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2], -4),
    pytest.param([9, 1, 7, 9, 7, 9, 7], 1),
])
def test_solutions(args, expected):
    assert Solution().singleNumber(args) == expected
    assert Solution3().singleNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
