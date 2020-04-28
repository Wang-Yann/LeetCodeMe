#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-27 18:25:45
# @Last Modified : 2020-04-27 18:25:45
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


class MyCircularDueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.__start = 0
        self.__size = 0
        self.__buffer = [0] * k
        self.__capacity = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        idx = (self.__start + self.__capacity - 1) % self.__capacity
        self.__buffer[idx] = value
        self.__start=idx
        self.__size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        idx = (self.__start + self.__size) % self.__capacity
        self.__buffer[idx] = value
        self.__size+=1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.__start = (self.__start + 1) % self.__capacity
        self.__size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.__size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
           return self.__buffer[self.__start]
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            idx = (self.__start + self.__size-1) % self.__capacity
            return self.__buffer[idx]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.__size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.__size == self.__capacity


if __name__ == '__main__':
    circularDeque = MyCircularDueue(3)  ## 设置长度为 3
    circularDeque.insertLast(1)  # 返回 true
    circularDeque.insertLast(2)  # 返回 true
    circularDeque.insertFront(3)   # 返回 true
    circularDeque.insertFront(4)   # 已经满了，返回 false
    print(circularDeque.getRear() )      # 返回 2
    circularDeque.isFull()       # 返回 true
    circularDeque.deleteLast()    # 返回 true
    print(circularDeque.insertFront(4))  # 返回 true
    print(circularDeque.getFront())  # 返回 4
