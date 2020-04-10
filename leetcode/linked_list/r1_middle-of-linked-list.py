# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.


# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        single_speed = head
        double_speed = single_speed.next
        while (double_speed != None and double_speed.next != None):
            single_speed = single_speed.next
            double_speed = double_speed.next.next
            
        if double_speed == None:
            return single_speed 
        return single_speed.next
