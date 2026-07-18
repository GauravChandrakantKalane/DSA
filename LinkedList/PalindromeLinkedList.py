class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def insertAtTail(head,data):
    newNode = Node(data)
    if(head == None):
        head= newNode
        return head
    temp = head
    while(temp.next is not None):
        temp = temp.next
    temp.next = newNode
    return head

def removeAtTail(head):
    if(head == None):
        return None
    if(head.next == None):
        head = None
        return head
    temp = head
    while(temp.next.next is not None):
        temp = temp.next
    temp.next = None
    return head

def printList(head):
    if(head == None):
        print("None")
        return
    temp = head
    while(temp is not None):
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")

def middleOfList(head):
    slow = head
    fast = head.next
    while(fast is not None and fast.next is not None):
        fast = fast.next
        if(fast.next is not None):
            fast = fast.next
        slow = slow.next
    return slow 

def reverseList(head):
    if(head == None):
        return None
    curr = head
    prev = None
    while(curr is not None):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    return head

def isPalindrome(head):
    if(head == None or head.next == None):
        return True
    middle = middleOfList(head)
    middle.next = reverseList(middle.next)

    temp = middle.next
    head2 = head
    while(temp is not None):
        if(temp.data != head2.data):
            return False
        head2 = head2.next
        temp = temp.next
    middle.next = reverseList(middle.next)
    return True


head = None
head = insertAtTail(head,1)
head = insertAtTail(head,2)
head = insertAtTail(head,3)
head = insertAtTail(head,2)
head = insertAtTail(head,1)
printList(head)
print("IS PALINDROME => ", isPalindrome(head))
printList(head)