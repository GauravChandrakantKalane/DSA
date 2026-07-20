
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
        print("None")
    temp = head
    while(temp is not None):
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")

def findMid(head):
    if(head == None):
        return head
    slow = head
    fast = head.next
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow

def solve(first,second):
    curr1 = first
    next1 = first.next
    curr2 = second
    while(next1 is not None and curr2 is not None):
        if(curr2.data >= curr1.data and curr2.data <= next1.data):
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

def merge(first,second):
    if(first == None):
        return second
    if(second == None):
        return first
    if(first.data <= second.data):
        return solve(first,second)
    else:
        return solve(second,first)

def mergeSort(head):
    if(head == None or head.next == None):
        return head
    
    mid = findMid(head)
    left = head
    right = mid.next
    mid.next = None
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left,right)


head = None
head = insertAtTail(head,4)
head = insertAtTail(head,1)
head = insertAtTail(head,6)
head = insertAtTail(head,2)
head = insertAtTail(head,9)
head = insertAtTail(head,7)
printList(head)
head = mergeSort(head)
printList(head)