'''#creating a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#Object creation
n1 = Node(7)
print(n1.data)
print(n1.next)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
#Object creation
sll=SinglyLinkedList()

'''
#Traversal in Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
       self.head = None
    def traversal(self):
        if(self.head is None):
            print("Singly Linked List is Empty")
        else:
            a = self.head
            while a is not None:
                    print(a.data, end=" ")
                    a=a.next
            print("Linked List Done")

n1 = Node(5) #n1 is the object of class Node. n1 will pass n1.data=5, n1.next=none
sll=SinglyLinkedList() #object of singlyLinkedList.ASAP init will run. self will be sll. sll.head = none. Still list is empty.
sll.head = n1 #now head is pointing to n1
n2 = Node(10) # n2.data =10, n2.next=none
n1.next = n2 #NOW n1.next=10
n3 = Node(15) # n3.data =10, n3.next=none
n2.next = n3 #NOW n2.next=15
n4 = Node(20) # n4.data =20, n4.next=none
n3.next = n4 #NOW n3.next=20 

sll.traversal() #it'll pass to the traversal method. initially sll.head is none but we assigned sll.head = n1. There  a = self.head but out self.head = sll.head. So, a = sll.head and sll.head is n1. a.data = n1.data. n1.data is 5. now a = a.next = n1.next. n1.next is n2...n4.next is none.

