# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def insert(self, num):
        new_node = ListNode(num)        
        new_node.next = self.head
        self.head = new_node

    # def traversal(self):
    #     h = self.head

    #     if h is None:
    #         print(f"Linked List is empty")
        
    #     else:
    #         while h is not None:
    #             print(f"{h.val}->", end="")
    #             h = h.next


    def deleteDuplicates(self):
        h = self.head
        if h is None:
            return f"List empty"
        else:
            prev_val = 0
            while h is not None:
                if h.val == prev_val:
                    print(f"{h.val} is a Duplicate")
                else:
                    print(f"{h.val}->")
                    # delete h.val
                prev_val = h.val
                h = h.next


list1 = [1,2,3,4,4,6,22]
soln = Solution()

soln.insert(1)
soln.insert(2)
soln.insert(3)
soln.insert(4)
soln.insert(4)
soln.insert(6)
soln.insert(22)


soln.deleteDuplicates()

# soln.traversal()