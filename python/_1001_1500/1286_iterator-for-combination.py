#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 请你设计一个迭代器类，包括以下内容： 
# 
#  
#  一个构造函数，输入参数包括：一个 有序且字符唯一 的字符串 characters（该字符串只包含小写英文字母）和一个数字 combinationLengt
# h 。 
#  函数 next() ，按 字典序 返回长度为 combinationLength 的下一个字母组合。 
#  函数 hasNext() ，只有存在长度为 combinationLength 的下一个字母组合时，才返回 True；否则，返回 False。 
#  
# 
#  
# 
#  示例： 
# 
#  CombinationIterator iterator = new CombinationIterator("abc", 2); // 创建迭代器 it
# erator
# 
# iterator.next(); // 返回 "ab"
# iterator.hasNext(); // 返回 true
# iterator.next(); // 返回 "ac"
# iterator.hasNext(); // 返回 true
# iterator.next(); // 返回 "bc"
# iterator.hasNext(); // 返回 false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= combinationLength <= characters.length <= 15 
#  每组测试数据最多包含 10^4 次函数调用。 
#  题目保证每次调用函数 next 时都存在下一个字母组合。 
#  
#  Related Topics 设计 回溯算法

"""

import itertools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.__it = itertools.combinations(characters, combinationLength)
        self.__curr = None
        self.__last = characters[-combinationLength:]

    def next(self) -> str:
        self.__curr = "".join(next(self.__it))
        return self.__curr

    def hasNext(self) -> bool:
        return self.__curr != self.__last


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# leetcode submit region end(Prohibit modification and deletion)
class CombinationIteratorBit:

    def __init__(self, characters: str, combinationLength: int):
        self.key = characters[::-1]
        self.N = len(characters)
        self.curr = 2 ** self.N - 1
        self.sz = combinationLength

    def __countOne(self, num):
        cnt = 0
        while num:
            cnt += 1
            num &= (num - 1)
        return cnt

    def next(self) -> str:
        while self.curr >= 0 and self.__countOne(self.curr) != self.sz:
            self.curr -= 1
        res = ""
        for i in range(self.N):
            if (self.curr & (1 << i)) >> i:
                res = self.key[i] + res
        self.curr -= 1
        return res

    def hasNext(self) -> bool:
        while self.curr >= 0 and self.__countOne(self.curr) != self.sz:
            self.curr -= 1
        return self.curr >= 0


@pytest.mark.parametrize("IterCls", [CombinationIteratorBit, CombinationIterator])
def test_solution(IterCls):
    # print("IterCls", IterCls)
    iterator = IterCls("abc", 2)
    assert iterator.next() == "ab"  # 返回 "ab"
    assert iterator.hasNext()  # // 返回 true
    assert iterator.next() == "ac"  # 返回 "ac"
    assert iterator.hasNext()  # // 返回 true
    assert iterator.next() == "bc"  # 返回 "bc"
    assert iterator.hasNext() == False  # // 返回 false


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
