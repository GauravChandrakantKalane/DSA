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
        return newNode
    temp = head
    while(temp.next is not head):
        temp = temp.next
    temp.next = newNode
    newNode.next = head
    return head

def removeAtHead(head):
    if(head == None):
        return head
    temp = head
    while(temp.next is not head):
        temp = temp.next
    head = head.next
    temp.next = head
    return head

def removeAtTail(head):
    if(head == None):
        return head
    
    curr = head
    prev = None
    while(curr.next is not head):
        prev = curr
        curr = curr.next
    
    curr.next = None
    prev = head
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
head = None
head = insertAtHead(head,1)
head = insertAtTail(head,2)
head = insertAtHead(head,3)
head = insertAtTail(head,4)
printList(head)

