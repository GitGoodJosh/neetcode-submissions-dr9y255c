# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, cl1: Optional[ListNode], cl2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        while cl1 !=None and cl2 !=None:
            print(current.val)
            if cl1.val <= cl2.val:
                current.next = cl1
                cl1 = cl1.next
                
            elif cl2.val <= cl1.val: 
                current.next = cl2
                cl2 = cl2.next

            current = current.next

        if cl1 == None:
            current.next = cl2
        elif cl2 ==None:
            current.next = cl1
        return head.next


        