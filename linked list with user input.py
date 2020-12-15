# Creating the linked List with user Inputs
print('''saketh
121910313017''')

class Node:
    #This class is used for the creation of the node 
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    #This class is used for the creation of the Linked List 
    def __init__(self):
        self.head = None
        
    def append(self,value):
        #This function is used for the user input feed 
        if self.head is None:
            new_node  = Node(value) #Only for the head value 
            self.head=new_node
            
        else:
            new_node = Node(value) #For the other values of the linked list 
            temp = self.head
            while temp.next!=None:
                 temp=temp.next
            temp.next = new_node
            
    def printList(self):
        #For Printing the linked list 
        t = self.head
        while(t):
            print(t.data)
            t = temp.next


a=LinkedList()
n=int(input("enter the number of nodes u want to add to the linkedlist: "))

for i in range(n):
    a.append(input('Enter the node data: '))
    
a.printList()  
