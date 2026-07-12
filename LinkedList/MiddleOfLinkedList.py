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
    temp = head
    while(temp is not None):
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")

def middleOfList(head):
    if(head == None):
        return None
    fast = head
    slow = head
    while(fast is not None and fast.next is not None ):
        fast = fast.next.next
        slow = slow.next
    return slow.data

head = None
head = insertAtTail(head,1)
head = insertAtTail(head,2)
head = insertAtTail(head,3)
head = insertAtTail(head,4)
head = insertAtTail(head,5)
printList(head)
print("Middle of List => ", middleOfList(head))