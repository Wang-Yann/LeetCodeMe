#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-27 18:25:45
# @Last Modified : 2020-04-27 18:25:45
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”
# 。
#
#  循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环
# 队列，我们能使用这些空间去存储新的值。
#
#  你的实现应该支持如下操作：
#
#
#  MyCircularQueue(k): 构造器，设置队列长度为 k 。
#  Front: 从队首获取元素。如果队列为空，返回 -1 。
#  Rear: 获取队尾元素。如果队列为空，返回 -1 。
#  enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
#  deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
#  isEmpty(): 检查循环队列是否为空。
#  isFull(): 检查循环队列是否已满。
#
#
#
#
#  示例：
#
#  MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
# circularQueue.enQueue(1);  // 返回 true
# circularQueue.enQueue(2);  // 返回 true
# circularQueue.enQueue(3);  // 返回 true
# circularQueue.enQueue(4);  // 返回 false，队列已满
# circularQueue.Rear();  // 返回 3
# circularQueue.isFull();  // 返回 true
# circularQueue.deQueue();  // 返回 true
# circularQueue.enQueue(4);  // 返回 true
# circularQueue.Rear();  // 返回 4
#
#
#
#  提示：
#
#
#  所有的值都在 0 至 1000 的范围内；
#  操作数将在 1 至 1000 的范围内；
#  请不要使用内置的队列库。
#
#  Related Topics 设计 队列
#  👍 121 👎 0

"""

from common_utils import ListNode as  Node


class MyCircularQueue0:
    """从并发性来看，该循环队列是线程不安全的。 """

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.__start = 0
        self.__size = 0
        self.__buffer = [0] * k
        self.__capacity = k
        # self.queueLock = Lock()

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # with self.queueLock:
        if self.isFull():
            return False
        idx = (self.__start + self.__size) % self.__capacity
        self.__buffer[idx] = value
        self.__size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.__start = (self.__start + 1) % self.__capacity
        self.__size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if not self.isEmpty():
            return self.__buffer[self.__start]
        return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if not self.isEmpty():
            idx = (self.__start + self.__size - 1) % self.__capacity
            return self.__buffer[idx]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.__size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.__size == self.__capacity


class MyCircularQueue:
    """
    与固定大小的数组相比，单链表不会为未使用的容量预分配内存，因此它的内存效率更高。
    """

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.head.val
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


if __name__ == '__main__':
    circularQueue = MyCircularQueue(3)  ## 设置长度为 3
    circularQueue.enQueue(1)  ## 返回 true
    circularQueue.enQueue(2)  ## 返回 true
    circularQueue.enQueue(3)  ## 返回 true
    circularQueue.enQueue(4)  ## 返回 false，队列已满
    circularQueue.Rear()  ## 返回 3
    circularQueue.isFull()  ## 返回 true
    circularQueue.deQueue()  ## 返回 true
    circularQueue.enQueue(4)  ## 返回 true
    circularQueue.Rear()  ## 返回
