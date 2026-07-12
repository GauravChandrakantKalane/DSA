class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insertAtHead(head,data):
    newNode = Node(data)
    if(head == None):
        head = newNode
        head.next = newNode
        return head
    temp = head
    while(temp.next is not head):
        temp = temp.next
    temp.next = newNode
    newNode.next = head
    head = newNode
    return head

def insertAtTail(head,data):
    newNode = Node(data)
    if(head == None):
        head = newNode
        head.next = newNode
        return head
    temp = head
    while(temp.next is not head):
        temp = temp.next
    temp.next = newNode
    newNode.next = head
    return head

def removeAtHead(head):
    if(head == None):
        return head
    if(head.next == head):
        head = None
        return head
    temp = head
    while(temp.next is not head):
        temp = temp.next
    temp.next = temp.next.next
    head = head.next
    return head

def removeAtTail(head):
    if(head == None):
        return head
    if(head.next == head):
        head = None
        return head
    prev = None
    curr = head
    while(curr.next is not head):
        prev = curr
        curr = curr.next
    curr.next = None
    prev.next = head
    return head

def printList(head):
    if(head == None):
        print("None")
        return
    temp = head
    while(temp.next is not head):
        print(temp.data,end=" -> ")
        temp = temp.next
    print(temp.data,end=" -> ")
    temp = temp.next
    print(temp.data)






def isCircularLinkedList(head):
    if(head == None):
        return True
    if(head.next == None):
        return False
    temp = head
    while(temp.next is not head):
        if(temp.next == None):
            return False
        temp = temp.next
    return True 