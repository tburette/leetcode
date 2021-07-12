import unittest
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode:val={self.val},next= {self.next!r}"

    def __str__(self):
        ret_val = "ListNode<"
        current_node = self
        while current_node:
            ret_val += f"{current_node.val}, "
            current_node = current_node.next
        ret_val = ret_val[:-2]  # remove last ", "
        ret_val += ">"
        return ret_val

    def __eq__(self, other):
        if other is None:
            # self is not None but other is
            # assumes None is the equivalent of a ListNode with no elements
            return False
        if not isinstance(other, type(self)):
            return NotImplemented
        if self.val != other.val:
            return False
        return self.next == other.next


# recursive implementation
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def mergeTwoListsRec(current: ListNode, l1: ListNode, l2: ListNode):
            if not l1 and not l2:
                # Nothing to add anymore
                return current

            # TODO: I don't think you need to go node by node when only one list is left
            if not l1:
                # l1 empty, take value from l2
                list_to_add_from = l2
                non_modified_list = l1
            elif not l2:
                # l2 empty, take value from l1
                list_to_add_from = l1
                non_modified_list = l2
            elif l1.val <= l2.val:
                # both lists non-empty, take value from l1 (smaller)
                list_to_add_from = l1
                non_modified_list = l2
            else:
                # both lists non-empty, take value from l2 (smaller)
                list_to_add_from = l2
                non_modified_list = l1

            current.next = list_to_add_from
            mergeTwoListsRec(
                current.next,
                list_to_add_from.next,
                non_modified_list)
            return current

        # the ListNode passed is a dummy.
        # It will not be returned itself but its .next will.
        concatenated_list = mergeTwoListsRec(ListNode(), l1, l2)
        return concatenated_list.next


# iterative implementation
class Solution:
    @staticmethod
    def pop_smaller_value(lists):
        """returns smaller head value and removes it from lists (in-place).

        :raise: ValueError : Both lists are empty (None)
        """
        if not lists[0] and not lists[1]:
            raise ValueError(f"Cannot pop from empty lists: {lists}")

        if not lists[0]:
            # pop value from second list
            remove_from_first = False
        elif not lists[1]:
            # pop value from first list
            remove_from_first = True
        elif lists[0].val > lists[1].val:
            # pop value from second list
            remove_from_first = False
        else:
            assert lists[0].val <= lists[1].val
            # pop value from first list
            remove_from_first = True

        if remove_from_first:
            node_to_return = lists[0]
            lists[0] = node_to_return.next
            node_to_return.next = None  # TODO needed?
        else:
            node_to_return = lists[1]
            lists[1] = node_to_return.next
            node_to_return.next = None  # TODO needed?

        return node_to_return

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head_node = ListNode()
        current_node = dummy_head_node
        lists = [l1, l2]  # [0] is (current state of) l1, [1] is (current) l2
        while lists != [None, None]:
            smaller_node = Solution.pop_smaller_value(lists)
            current_node.next = smaller_node
            current_node = smaller_node
        return dummy_head_node.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def list_to_ListNode(self, list_: List) -> ListNode:
        dummy_head = ListNode()  # head node is a dummy, will return the next
        current = dummy_head
        for val in list_:
            next_node = ListNode(val)
            current.next = next_node
            current = next_node
        return dummy_head.next

    def assertEqualMergeTwoLists(self, expected: List, l1: List,
                                 l2: List) -> None:
        """Convenience method to test mergeTwoLists.

        The arguments are converted into proper ListNodes
        """
        self.assertEqual(self.list_to_ListNode(expected),
                         self.s.mergeTwoLists(self.list_to_ListNode(l1),
                                              self.list_to_ListNode(l2)))

    def test_examples(self):
        self.assertEqualMergeTwoLists([1, 1, 2, 3, 4, 4], [1, 2, 4], [1, 3, 4])
        self.assertEqualMergeTwoLists([], [], [])
        self.assertEqualMergeTwoLists([0], [], [0])

    def test_empty(self):
        self.assertEqualMergeTwoLists([0], [0], [])
        self.assertEqualMergeTwoLists([0], [], [0])
