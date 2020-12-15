# This is the program for inserting the element in between
print('''Venkatesh Bisoyi
121910313056''')

class Node:
    #This is class for creation of nodes
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    #this is the class for the intialization of linked list 
    def __init__(self):
        self.head = None
        
    def append(self,value):
        #Rading the user input 
        if self.head is None:
            new_node  = Node(value)
            self.head=new_node
        else:
            new_node = Node(value)
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node    

    def add_in_btw(self,value,position_value):
        #Reading the index value and inserting the element at the desired index 
        new_node=Node(value)
        temp=self.head
        while temp:
            if temp.data==position_value:
                break
            temp=temp.next
        nxt=temp.next
        temp.next=new_node
        new_node.next=nxt
        
        
    def printList(self):
        #This is used for printing the linked List 
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


li=LinkedList()
n=int(input("enter the number of nodes u want to add to the linkedlist: "))
for i in range(n):
    li.append(input('Enter the node data: '))

a=input("Enter the value to insert: ")
b=input("Enter after which element you want to add this new value: ")

li.add_in_btw(a,b)
li.printList()
