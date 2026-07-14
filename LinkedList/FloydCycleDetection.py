class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def insertAtHead(head,data):
    newNode = Node(data)
    if(head == None):
        head = newNode
        return head
    newNode.next = head
    head = newNode
    return head

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

def removeAtHead(head):
    if(head == None):
        return None
    head = head.next
    return head

def removeAtTail(head):
    if(head == None):
        return None
    if(head.next == None):
        head = None
        return head
    prev = None
    temp = head
    while(temp.next is not None):
        prev = temp
        temp = temp.next
    prev.next = None
    return head

def printList(head):
    if(head == None):
        print("None")
    temp = head
    while(temp is not None):
        print(temp.data,end=" -> ")
        temp = temp.next
    print('None')

def createCyclic(head):
    temp = head
    while(temp.next is not None):
        temp = temp.next
    temp.next = head.next.next

# Find if there is Loop
def isCyclicLoop(head):
    if(head == None):
        return None
    slow = head
    fast = head
    while(fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next
        if(fast == slow):
            return slow
    return None

# Get the intersection point
def intersectionPoint(head):
    if(head == None):
        return None
    meeting = isCyclicLoop(head)
    if(meeting is None):
        return None
    slow = meeting
    fast = head
    while(fast != slow):
        fast = fast.next
        slow = slow.next
    return slow
    
# remove the loop

def removeLoop(head):
    if(head == None):
        return None
    
    intersectPoint = intersectionPoint(head)
    if(intersectPoint is None):
        return None
    temp = intersectPoint
    while(temp.next != intersectPoint):
        temp = temp.next
    temp.next = None

    

head = None
head = insertAtHead(head,1)
head = insertAtTail(head,2)
head = insertAtTail(head,3)
head = insertAtTail(head,4)
head = insertAtTail(head,5)
printList(head)
# print("IS LOOP PRESENT => ",isCyclicLoop(head) )

createCyclic(head)
# printList(head)
# print("IS LOOP PRESENT => ",isCyclicLoop(head) )

removeLoop(head)

printList(head)

     