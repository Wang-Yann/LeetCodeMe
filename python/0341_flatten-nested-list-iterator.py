#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 10:13:40
# @Last Modified : 2020-04-26 10:13:40
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return True

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return 0

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return []


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
        except Exception as e:
            return False


if __name__ == '__main__':
    nestedList = []
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)
