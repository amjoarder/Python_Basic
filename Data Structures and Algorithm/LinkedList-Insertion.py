#https://www.youtube.com/watch?v=MLqHDsBOC4c&ab_channel=GreatLearning
#Watch this if you have any doubt.
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
    

    def insertBeginning(self,data):
        print()
        nb = Node(data) #creating new object of Node class. we put 2 as data
        nb.next = self.head #this is the logic to connect the new node. self.head is n1 actually.
        self.head = nb #it is sll.head = nb and it changes head position.


    def insertionEnd(self,data):
        print()
        ne = Node(data) #to insert the node at last. we have to traverse the total linked list. so we create a temporary variable.
        a = self.head #a =sll.head will pass actually. then sll.head = nb. 
        while a.next is not None:
            a=a.next #a.next = nb.next. then a = nb.next
        a.next = ne


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


#inserting new node at beginning starts here.

sll.insertBeginning(2) #inserting 2 in the beginning
sll.traversal() #this will show new list after inserting the new value.

#insertion at the end code starts here.
#print("\nInsertion at the end")
sll.insertionEnd(25)
sll.traversal()

