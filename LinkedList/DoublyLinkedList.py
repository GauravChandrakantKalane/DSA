class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# Insert at Head
def insertAtHead(data,head):
    newNode = Node(data)
    if(head == None):
        head = newNode
        return head
    newNode.next = head
    head = newNode
    return head

# Insert at Tail
def insertAtTail(data,head):
    newNode = Node(data)
    if(head == None):
        head = newNode
        return head
    temp = head
    while(temp.next is not None):
        temp = temp.next
    temp.next = newNode
    newNode.prev = temp
    return head

# remove Node at Head
def removeAtHead(head):
    if(head == None):
        return None
    head = head.next
    head.prev = None
    return head

# remove Node at Tail
def removeAtTail(head):
    if(head == None):
        return None
    temp = None
    curr = head
    while(curr.next is not None):
        temp = temp.next
        curr = curr.next
    temp.next = None
    curr.prev = None
    return head


# Insert at Position
def insertAtPosition(position,data,head):
    newNode = Node(data)
    if(position == 1):
        return insertAtHead(data,head)
    
    curr = head
    temp = None
    count = 1
    while(count < position):
        temp = curr
        curr = curr.next
        
        count += 1
    print("COUNT => ", count)
    
    curr.next = newNode
    newNode.prev = curr
    newNode.next = temp
    temp.prev = newNode
    return head

# Remove at Position
def removeAtPosition(position,head):
    if(position == 1):
        return removeAtHead(data,head)
    
    curr = head
    count = 1
    while(count < position):
        curr = curr.next
        count += 1
    
    temp = curr.next
    curr.next = curr.next.next
    temp.prev = None
    temp.next = None
    curr.next.prev = curr
    return head

# Length of Linked List
def lengthOfList(head):
    if(head == None):
        return None
    temp = None
    count = 0
    while(temp is not None):
        temp = temp.next
        count += 1
    return count

# Print Linked List
def printList(head):
    temp = head
    while(temp is not None):
        print(" <- ",temp.data, end=" -> ")
        temp = temp.next
    print("None")

head = None
head = insertAtTail(1,head)
head = insertAtHead(2,head)
head = insertAtTail(3,head)
head = insertAtPosition(1,4,head)
head = insertAtPosition(3,5,head)
# head = removeAtPosition(3,head)



printList(head)
    
    
