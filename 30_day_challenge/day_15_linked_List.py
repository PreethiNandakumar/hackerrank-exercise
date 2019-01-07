class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        if head is None:
            head = Node(data)
            self.head_next = head
        else:
            node = Node(data)
            self.head_next.next = node
            self.head_next = node
        return head
    #Complete this method

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
    # print("HEAD:{}".format(head))
mylist.display(head);