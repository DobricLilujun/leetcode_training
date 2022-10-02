# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        adding = 0
        rest = 0
        resultNode = None
        while (l1 != None) or (l2 != None):
            a = l1.val if (l1!=None) else 0
            b = l2.val if (l2!=None) else 0
            if a+b+adding >=10:
                addnode = ListNode(val = a+b+adding-10)
                adding = 1
            else:
                addnode = ListNode(val = a+b+adding)
                adding = 0
            if resultNode == None:
                resultNode = addnode
                initial = resultNode
            else:
                resultNode.next = addnode
                resultNode = resultNode.next
            l1 = l1.next if (l1!=None) else None
            l2 = l2.next if (l2!=None) else None
        if adding ==1:
            addnode = ListNode(val = 1)
            resultNode.next = addnode
        return initial