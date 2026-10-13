# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        # Copy the next node's value into this node
        node.val = node.next.val
        # Skip the next node
        node.next = node.next.next
