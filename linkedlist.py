#add 2 numbers linked list in reverse order
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        current=dummy
        carry=0

        while l1 or l2 or carry:
            n1=l1.val if l1 else 0
            n2=l2.val if l2 else 0
            total=n1+n2+carry
            carry=total//10

            current.next=ListNode(total%10)
            current=current.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
        return dummy.next


"""
#SPAM- my solution reversing a part of linked list
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self,head):
        prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        length=0
        temp=head
        while(temp):
            length+=1
            temp=temp.next

        part1=head
        part2=head
        
        for i in range(1,left-1):
            part1=part1.next
        
        for i in range(1,right+1):
            part2=part2.next

        m_rev=part1.next
        rev=m_rev
        for i in range(1,right-left):
            rev=rev.next
        rev.next=None
        m_rev=self.reverse(m_rev)

        temp2=m_rev
        for i in range(1,right-left+1):
            temp2=temp2.next
        temp2.next=part2
        part1.next=m_rev
        return head

        
"""
#reversing a linked list in-between
"""

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy

        for i in range(left-1):
            prev=prev.next
        

        curr=prev.next
        for i in range(right-left):
            temp=curr.next
            curr.next=temp.next
            temp.next=prev.next
            prev.next=temp
        return dummy.next
"""
#copy ll with random pointer
"""
def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        mp={}
        curr=head
        while curr:
            mp[curr]=Node(curr.val)
            curr=curr.next
        
        for node in mp:
            mp[node].next=mp.get(node.next)
            mp[node].random=mp.get(node.random)
        
        return mp[head]
"""
#Merge k sorted linked list
"""

heap=[]

        for i,node in enumerate(lists):
            heapq.heappush(heap,(node.val,i,node))

        dummy=ListNode()
        curr=dummy

        while(heap):
            val,i,node=heapq.heappop(heap)
            curr.next=node
            curr=curr.next

            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))
        
        return dummy.next

        
"""