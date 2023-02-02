# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = self.
        if h is None:
            return
        else:
            while h is not None:
                prev_val = 0
                if h.val == prev_val:
                    # delete
                    h = h.next
                else:
                    prev_val = h.val
                h = h.next