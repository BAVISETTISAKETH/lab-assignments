#This is the program for inserting the element at the beginning of the linked list
print('''Venkatesh Bisoyi
121910313056''')

#The Code Starts from here 
class Node:
    #Node Class is used to create a node
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    # This class is used to create Linked List  
    def __init__(self):
        self.head = None
        
    def append(self,value):
        # Taking in the User input 
        if self.head is None:
            new_node  = Node(value)
            self.head=new_node
        else:
            new_node = Node(value)
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node    

    def AtTheBeginning(self,value):
        # Adding the element at the Beginning of the linked list 
        if self.head is None:
            new_node  = Node(value)
            self.head=new_node
        else:
            new_node = Node(value)
            new_node.next=self.head
            self.head=new_node
        
    def printList(self):
        # printing the linked list 
        t = self.head
        while(t):
            print(t.data)
            t = t.next

a=LinkedList()
n = int(input("enter the number of nodes u want to add to the linkedlist: "))
for i in range(n):
    a.append(input('Enter the node data : '))
print('The linked List before inserting the element at the beginning')
a.printList()

# Enter the element you want to add at the beginning
b=input("Enter the value to add at the beggining: ")
a.AtTheBeginning(b)
a.printList()    
