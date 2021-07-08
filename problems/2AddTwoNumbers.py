# https://leetcode.com/problems/add-two-numbers
import itertools


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode(val={self.val}, next={self.next})'


# V1 loop with manual creation
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_list_head = ListNode(0)
        sum_list_cur = sum_list_head
        carry = 0  # designed to hold 1 if previous iteration's sum was >= 10
        while l1 or l2 or carry:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            sum_list_cur.val = (val + carry) % 10
            carry = (val + carry) // 10
            if l1 or l2 or carry:
                next_node = ListNode(0)
                sum_list_cur.next = next_node
                sum_list_cur = next_node
        return sum_list_head


# V2 functional but iterative for creation of the linked list at the end
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def iter_ListNode(l: ListNode):
            while l:
                yield l.val
                l = l.next
        zipped_lists = itertools.zip_longest(iter_ListNode(l1), iter_ListNode(l2), fillvalue=0)
        sum_it = itertools.starmap(int.__add__, zipped_lists)
        placeholder = ListNode(0)
        current_node = placeholder
        carry = 0
        for val in sum_it:
            new_node = ListNode((val+carry) % 10)
            current_node.next = new_node
            current_node = new_node
            carry = (val+carry) // 10
        if carry:
            current_node.next = ListNode(1)

        return placeholder.next


# https://docs.python.org/3/library/itertools.html#itertools-recipes
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

# V3 more functional
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # convert ListNode to equivalent iterable of ints
        def iter_ListNode(l: ListNode):
            while l:
                yield l.val
                l = l.next
        zipped_lists = itertools.zip_longest(iter_ListNode(l1), iter_ListNode(l2), fillvalue=0)
        sum_it = itertools.starmap(int.__add__, zipped_lists)

        def handle_carry(sum):
            carry = 0
            for val in sum:
                val += carry
                carry = val >= 10
                yield val % 10
            if carry:
                yield 1
        sum_carried = handle_carry(sum_it)
        nodes, nodes2 = itertools.tee(map(ListNode, sum_carried))

        def connect_nodes(nodes):
            for n1, n2 in pairwise(nodes):
                n1.next = n2
        connect_nodes(nodes)

        # fail if empty
        return next(nodes2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(1)
    l2 = ListNode(8)
    l2.next = ListNode(8)
    print(Solution().addTwoNumbers(l1, l2))