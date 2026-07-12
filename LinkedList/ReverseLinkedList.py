class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insertAtTail(head,data):
    newNode = Node(data)
    if(head == None):
        head = newNode
        return head
    temp = head
    while(temp.next is not None):
        temp = temp.next
    temp.next = newNode
    return head

def printList(head):
    if(head == None):
        print(" -> None")
    temp = head
    while(temp is not None):
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")

def lengthOfList(head):
    count = 0
    temp = head
    while(temp is not None):
        count += 1
        temp = temp.next
    return count

def reverseList(head):
    curr = head
    prev = None
    while(curr is not None):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    return head

head = None
head = insertAtTail(head,1)
head = insertAtTail(head,2)
head = insertAtTail(head,3)
# head = insertAtTail(head,4)
# head = insertAtTail(head,5)
printList(head)
head = reverseList(head)
printList(head)
