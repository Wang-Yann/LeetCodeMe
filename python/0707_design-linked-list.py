#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 19:52:09
# @Last Modified : 2020-04-19 19:52:09
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针
# /引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
#
#  在链表类中实现这些功能：
#
#
#  get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
#  addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
#  addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
#  addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val 的节点。如果 index 等于链表的长度，则该节点将附加
# 到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
#  deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
#
#
#
#
#  示例：
#
#  MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
# linkedList.get(1);            //返回2
# linkedList.deleteAtIndex(1);  //现在链表是1-> 3
# linkedList.get(1);            //返回3
#
#
#
#
#  提示：
#
#
#  所有val值都在 [1, 1000] 之内。
#  操作次数将在 [1, 1000] 之内。
#  请不要使用内置的 LinkedList 库。
#
#  Related Topics 设计 链表
#  👍 151 👎 0

"""
import pytest

from common_utils import ListNode, DoubleListNode


class MyLinkedList:

    def __init__(self):
        self.size = 0
        # sentinel nodes as pseudo-head and pseudo-tail
        self.head, self.tail = DoubleListNode(0), DoubleListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __repr__(self):
        return "MyLinkedList({}  |  length: {} )".format(self.head, self.size)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1

        # choose the fastest way: to move from the head
        # or to move from the tail
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        pred, succ = self.head, self.head.next

        self.size += 1
        to_add = DoubleListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        succ, pred = self.tail, self.tail.prev

        self.size += 1
        to_add = DoubleListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length,
        # the node will not be inserted.
        if index > self.size:
            return

        # [so weird] If index is negative,
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0

        # find predecessor and successor of the node to be added
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        # insertion itself
        self.size += 1
        to_add = DoubleListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return

        # find predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev

        # delete pred.next
        self.size -= 1
        pred.next = succ
        succ.prev = pred


class MyLinkedListSingle:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__dummy_head = ListNode(-1)
        self.__size = 0

    def __repr__(self):
        return "MyLinkedListSingle({}  |  length: {} )".format(self.__dummy_head.next, self.__size)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if not 0 <= index <= self.__size - 1:
            return -1

        cur = self.__dummy_head
        for i in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.__size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if not 0 <= index <= self.__size:
            return
        pre = self.__dummy_head
        node = ListNode(val)
        for _ in range(index):
            pre = pre.next
        node.next = pre.next
        pre.next = node
        self.__size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if not 0 <= index <= self.__size - 1:
            return

        pre = self.__dummy_head
        for _ in range(index):
            pre = pre.next
        pre.next = pre.next.next
        self.__size -= 1


@pytest.mark.parametrize("ops_list, args_list", [
    (["MyLinkedList", "addAtHead", "get", "addAtHead", "addAtHead",
      "deleteAtIndex", "addAtHead", "get", "get", "get", "addAtHead",
      "deleteAtIndex"],
     [[], [4], [1], [1], [5], [3], [7], [3], [3], [3], [1], [4]]),
    (
        ["MyLinkedList", "addAtHead", "addAtHead", "addAtHead", "addAtIndex", "deleteAtIndex",
         "addAtHead", "addAtTail", "get", "addAtHead", "addAtIndex", "addAtHead"],
        [[], [7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]]
    ),
    (["MyLinkedList", "addAtHead", "addAtTail", "deleteAtIndex", "addAtTail", "addAtIndex", "addAtIndex",
      "deleteAtIndex",
      "deleteAtIndex", "addAtTail", "addAtIndex", "addAtTail"],
     [[], [7], [0], [1], [5], [1, 1], [2, 6], [2], [1], [7], [1, 7], [6]])
])
@pytest.mark.parametrize("LinkedListCLS", [
    MyLinkedList, MyLinkedListSingle
])
def test_solutions(LinkedListCLS, ops_list, args_list):
    print("-" * 30)
    print(LinkedListCLS.__name__, list(zip(ops_list, args_list)))
    lk = LinkedListCLS()
    for i in range(1, len(ops_list)):
        method, args = ops_list[i], args_list[i]
        print(method, args, lk, getattr(lk, method)(*args))
    print("-" * 30)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
