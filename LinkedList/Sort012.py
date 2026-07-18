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
    temp = head
    while(temp is not None):
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")

# Approach One
# def sort012(head):
#     if(head == None or head.next == None):
#         return head
#     zeroCount = 0
#     oneCount = 0
#     twoCount = 0
#     temp = head
#     while(temp is not None):
#         if(temp.data == 0):
#             zeroCount += 1
#         elif(temp.data == 1):
#             oneCount += 1
#         else:
#             twoCount += 1
#         temp = temp.next

#     temp = head
#     while(temp is not None):
#         if(zeroCount != 0):
#             temp.data = 0
#             zeroCount -= 1
#         elif(oneCount != 0):
#             temp.data = 1
#             oneCount -= 1
#         elif(twoCount != 0):
#             temp.data = 2
#             twoCount -= 1
#         temp = temp.next
#     return head

# Apprach 2
def sort012(head):
    zeroHead = Node(-1)
    oneHead = Node(-1)
    twoHead = Node(-1)
    temp = head
    while(temp is not None):
        if(temp.data == 0):
            zeroHead = insertAtTail(zeroHead,temp.data)
        elif(temp.data == 1):
            oneHead = insertAtTail(oneHead,temp.data)
        else:
            twoHead = insertAtTail(twoHead,temp.data)
        temp = temp.next
    if(oneHead.next is not None):
        zeroTail = zeroHead
        while(zeroTail.next is not None):
            zeroTail = zeroTail.next
        zeroTail.next = oneHead.next
    else:
        zeroTail = zeroHead
        while(zeroTail.next is not None):
            zeroTail = zeroTail.next
        zeroTail.next = twoHead.next
    oneTail = oneHead
    while(oneTail.next is not None):
        oneTail = oneTail.next
    oneTail.next = twoHead.next
    oneHead.next = None
    twoHead.next = None
    head = zeroHead.next
    return head
        



head = None
head = insertAtTail(head,1)
head = insertAtTail(head,2)
head = insertAtTail(head,1)
head = insertAtTail(head,0)
head = insertAtTail(head,1)
printList(head)
head = sort012(head)
printList(head)


