#This is the program for deleting the element at the starting of the linked list
print('''saketh
12191013017''')

class Node:
    # this class is used for the creation of the node
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    # this class is used for the creation of the Linked List
    def __init__(self):
        self.head = None

    def Append(self,value):
        #Reading the values from the user
        if self.head is None:
            self.head = Node(value)
            self.head = new_Node
        else :
            new_Node = Node(value)
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_Node

            
    def RemoveFirstnode(self):
        if (self.head == None):
            return;
        else:
            if(self.head != self.new_Node):
                
        


    def PrintList(self):
        #This function is used for printing the linked list
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


li = LinkedList()
n = int(input('Enter the number of elements you want to add : '))
for i in range(n):
    li.append(input('Enter the value of the node : '))

print('Linked List before deleting the First element :')
li.PrintList()
print('After Deleting the Frist Element :')
