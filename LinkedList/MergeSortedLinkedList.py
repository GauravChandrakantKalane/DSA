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

def removeAtTail(head):
    if(head == None):
        return head
    if(head.next == None):
        head = None
        return head
    temp = head
    while(temp.next.next is not None):
        temp = temp.next
    temp.next = newNode
    return head

def printList(head):
    if(head == None):
        print("None")
    temp = head
    while(temp is not None):
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")

def solve(first,second):
    curr1 = first
    next1 = curr1.next
    curr2 = second
    while(curr2 is not None and next1 is not None):
        if(curr1.data <= curr2.data and curr2.data <= next1.data):
            next2 = curr2.next
            curr2.next = next1
            curr1.next = curr2
            curr1 = curr2
            curr2 = next2
            next1 = curr1.next
        else:
            curr1 = next1
            next1 = next1.next
    
    if(curr2 is not None):
        curr1.next = curr2
    return first

def mergeList(head1,head2):
    if(head1 is None):
        return head2
    if(head2 is None):
        return head1
    if(head1.data <= head2.data):
        return solve(head1,head2)
    else:
        return solve(head2,head1)


head1 = None
head2 = None
head1 = insertAtTail(head1,1)
head1 = insertAtTail(head1,2)
head1 = insertAtTail(head1,6)
head2 = insertAtTail(head2,3)
head2 = insertAtTail(head2,7)
head2 = insertAtTail(head2,9)
printList(head1)
printList(head2)
head = mergeList(head1,head2)
printList(head)
