# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def get_lowest_node(l1, l2):
    """Get lowest node out of 2 ListNode's, and return 
        Returns (
            (ListNode) lowest value node of the 2 ListNode's,
            (bool) if lowest node was l1
        )
    """
    if not l1:
        lowest_node = l2
    elif not l2:
        lowest_node = l1
    elif l1.val < l2.val:
        lowest_node = l1
    else:
        lowest_node = l2
    # Forgive not using NamedTuple!
    return (
        lowest_node,
        True if lowest_node == l1 else False
    )


class SolutionA:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head_node = None
        last_node = None
        while l1 or l2:
            lowest_node, l1_was_lowest = get_lowest_node(l1, l2)

            if not head_node:
                head_node = lowest_node
                last_node = lowest_node
            else:
                last_node.next = lowest_node
                last_node = lowest_node

            if l1_was_lowest:
                l1 = l1.next
            else:
                l2 = l2.next

        return head_node

class SolutionB:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            # Ensure l1 is less
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(
                l1.next,
                l2
            )
        return l1 or l2
