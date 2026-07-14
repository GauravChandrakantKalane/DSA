class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
def insertAtHead(head,data):
    newNode = Node(data)
    if(head == None):
        head = newNode
        return head
    newNode.next = head
    head.prev = newNode
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
    newNode.prev = temp
    return head
    
def removeAtHead(head):
    if(head == None):
        return head
    if(head.next == None):
        head = None
        return head
    head = head.next
    head.prev = None
    return head
    
def removeAtTail(head):
    if(head == None):
        return head
    if(head.next == None):
        head = None
        return head
    temp = None
    curr = head
    while(curr.next is not None):
        temp = curr
        curr = curr.next
    curr.prev = None
    temp.next = None
    return head
    
def printList(head):
    if(head == None):
        print("None")
    temp = head
    while(temp is not None):
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
    

# Function to remove duplicate in sorted linked list   
def removeDuplicateInSortedList(head):
    if(head == None):
        return head
    if(head.next == None):
        return head
    curr = head
    while(curr.next is not None):
        if(curr.data == curr.next.data):
            temp = curr.next
            curr.next = curr.next.next
            temp.prev = None
            temp.next = None
            if(curr.next is not None):
                curr.next.prev = curr
        else:
            curr = curr.next
    return head

head = None
# head = insertAtHead(head,1)
# head = insertAtTail(head,1)
# head = insertAtTail(head,1)
# head = insertAtTail(head,3)
# head = insertAtTail(head,3)
# head = insertAtTail(head,3)
# head = insertAtTail(head,4)
printList(head)
head = removeDuplicateInSortedList(head)
printList(head)
