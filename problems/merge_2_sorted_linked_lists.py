from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #check lists arent empty
        if not list1:
            return list2
        elif not list2:
            return list1
        #create a new list to store the merged lists
        merged = ListNode()
        pointer = merged

        while list1 and list2:
            if list1.val < list2.val:
                #append list1 to the merged list and move the pointer forward
                pointer.next = list1
                list1 = list1.next
            else:
                #append list2 to the merged list and move the pointer forward
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next

        #append any remaining elements from list1 or list2
        if list1:
            pointer.next = list1
        elif list2:
            pointer.next = list2

        return merged.next