# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, data=0, ref=None):
        self.data = data
        self.ref = ref


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        head = dummy

        # if one of the list is empty, take the remainig nums into the output
        while l1 and l2:
            if l1.data < l2.data:
                head.ref = l1
                l1 = l1.ref
            else:
                head.ref = l2
                l2 = l2.ref
            head = head.ref

        if l1:
            # take the remaining portion and insert it at the end of the list
            head.ref = l1
        elif l2:
            head.ref = l2

        return dummy.ref


