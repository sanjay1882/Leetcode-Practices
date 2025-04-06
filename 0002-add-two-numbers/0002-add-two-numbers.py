# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        String1=""
        while l1:
            String1+=str(l1.val)
            l1=l1.next
        String2=""
        while l2:
            String2+=str(l2.val)
            l2=l2.next
        if not String1:
            String1="0"
        if not String2:
            String1="0"
        Sum=str(int(String1)+int(String2))

        dummy=curr=ListNode(0)
        for i in reversed(Sum):
            curr.next=ListNode(int(i))
            curr=curr.next
        return dummy.next

        
        

