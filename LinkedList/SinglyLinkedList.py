class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Add Node to Head of Linked List
def insertAtHead(data,head):
    newNode = Node(data)
    if(head == None):
        head = newNode
        return head
    newNode.next = head
    head = newNode
    return head

# Add Node to Tail of Linked List
def insertAtTail(data,head):
    newNode = Node(data)
    if(head == None):
        head = newNode
        return head
    temp = head
    while(temp.next is not None):
        temp = temp.next
    
    temp.next = newNode
    return head

# Remove Node at Head of Linked List
def removeAtHead(head):
    if(head == None):
        return None
    head = head.next
    return head

# Remove Node at Tail of Linked List
def removeAtTail(head):
    if(head == None):
        return None
    if(head.next is None):
        head = None
        return head
    temp = head
    while(temp.next.next is not None):
        temp = temp.next
    temp.next = None
    return head

# Add Node at given Position in Linked List
def insertAtPosition(position,data,head):
    newNode = Node(data)
    print("POSITION ", position)
    if(position == 1):
        return insertAtHead(data,head)
        
    
    count = 1
    temp = head
    while(count < position):
        temp = temp.next
    newNode.next = temp.next
    temp.next = newNode
    return head

def removeAtPosition(position,head):
    if(position == 1):
        return removeAtHead(head)
    
    curr = head
    count = 1
    while(count < position):
        curr = curr.next
    
    temp = curr.next
    curr.next = curr.next.next
    temp.next = None
    return head

def lengthOfList(head):
    count = 0
    temp = head
    while (temp is not None):
        temp = temp.next
        count += 1
    return count
    
def printList(head):
    if(head == None):
        print("None")
        return
    temp = head
    
    while(temp is not None):
        print(temp.data , end=" -> ")
        temp = temp.next
    print("None")

head = None
print("LENGTH OF LIST => ", lengthOfList(head))
head = insertAtHead(1,head)
print("LENGTH OF LIST => ", lengthOfList(head))

head = insertAtTail(2,head)
head = insertAtPosition(1,3,head)
print("LENGTH OF LIST => ", lengthOfList(head))

printList(head)
head = removeAtPosition(1,head)
print("LENGTH OF LIST => ", lengthOfList(head))

# head = removeAtHead(head)
printList(head)
print("LENGTH OF LIST => ", lengthOfList(head))
