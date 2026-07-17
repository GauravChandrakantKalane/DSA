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
        print(temp.data, end =" -> ")
        temp = temp.next
    print("None")

def reverseList(head):
    if(head == None):
        return head
    if(head.next == None):
        return head
    curr = head
    prev = None
    while(curr is not None):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    return head

def addList(head1,head2, ans):
    temp1 = head1
    temp2 = head2
    carry = 0
    while(temp1 is not None and temp2 is not None):
        sum = temp1.data + temp2.data + carry
        if(sum >= 10):
            digit = sum % 10
            carry = sum // 10
            newNode = Node(digit)
            ans = insertAtTail(ans,digit)
        else:
            carry = 0
            newNode = Node(sum)
            ans = insertAtTail(ans,sum)
        temp1 = temp1.next
        temp2 = temp2.next
    while(temp1 is not None):
        sum = temp1.data + carry
        if(sum >= 10):
            digit = sum % 10
            carry = sum // 10
            newNode = Node(digit)
            ans = insertAtTail(ans,digit)
        else:
            carry = 0
            newNode = Node(sum)
            ans = insertAtTail(ans,sum)
        temp1 = temp1.next
    while(temp2 is not None):
        sum = temp2.data + carry
        if(sum >= 10):
            digit = sum % 10
            carry = sum // 10
            newNode = Node(digit)
            ans = insertAtTail(ans,digit)
        else:
            carry = 0
            newNode = Node(sum)
            ans = insertAtTail(ans,sum)
        temp2 = temp2.next
    while(carry != 0):
        digit = carry % 10
        carry = carry // 10
        newNode = Node(digit)
        ans = insertAtTail(ans,digit)
    return ans


def addTwoList(head1,head2,ans):
    head1 = reverseList(head1)
    head2 = reverseList(head2)
    ans = addList(head1,head2,ans)

    ans = reverseList(ans)
    temp = ans
    while(temp.data != 0):
        temp = temp.next
    ans = temp
    return ans


head1 = None
head2 = None
head1 = insertAtTail(head1,4)
head1 = insertAtTail(head1,5)
# head1 = insertAtTail(head1,4)
printList(head1)
head2 = insertAtTail(head2,3)
head2 = insertAtTail(head2,4)
head2 = insertAtTail(head2,5)
printList(head2)
sumHead = None
sumHead = addTwoList(head1,head2,sumHead)
printList(sumHead)