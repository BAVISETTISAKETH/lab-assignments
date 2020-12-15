# Inserting the element at the end of the Linked list
print('''Venkatesh Bisoyi
121910313056''')

class Node:
    # this is for the creation of the node 
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    #this class is used for the creation of linked list 
    def __init__(self):
        self.head = None
        
    def append(self,value):
        #This function is used for reading the user inputs 
        if self.head is None:
            new_node  = Node(value) # The Value of head 
            self.head=new_node
        else:
            new_node = Node(value)
            temp = self.head
            while temp.next!=None:
                 temp=temp.next
            temp.next = new_node
            
    def printList(self):
        # this is for printing the list 
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

li=LinkedList()
N=int(input("enter the number of nodes u want to add to the linkedlist: "))
for i in range(N):
    li.append(input('Enter the node data : '))
a=input("Enter the value u want to insert at the end : ")
li.append(a) # Directly appending the value at the end of the linked list 
li.printList()  
