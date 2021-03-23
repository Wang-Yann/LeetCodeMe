#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 10:13:40
# @Last Modified : 2020-04-26 10:13:40
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
#
#  列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
#
#
#
#  示例 1:
#
#  输入: [[1,1],2,[1,1]]
# 输出: [1,1,2,1,1]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
#
#  示例 2:
#
#  输入: [1,[4,[6]]]
# 输出: [1,4,6]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
#
#  Related Topics 栈 设计
#  👍 127 👎 0
import pytest

from common_utils import NestedInteger


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.generator = self._build_generator(nestedList)
        self.v = None

    def _build_generator(self, data):
        for ele in data:
            if ele.isInteger():
                yield ele.getInteger()
            else:
                yield from self._build_generator(ele.getList())

    def next(self) -> int:
        return self.v

    def hasNext(self) -> bool:
        try:
            self.v = next(self.generator)
            return True
        except StopIteration as e:
            return False


def test_solution():
    nestedList = []
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    assert v == []


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
