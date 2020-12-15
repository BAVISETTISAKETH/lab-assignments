# this is the program for Linked List

# We create Two classes - node class and linked list class

class NodeClass:

    # This class is used to intialize the node objects
    def __init__(self, info):
        self.info  = info  # Assigning the value to the node 
        self.next =  None  # To intialize the next obect as null


class LinkedList:

    #This  class is used for the creation of the linked list
    #In this class we intialize the head
    def __init__(self):
        self.head = None


    def PrintList(self):
        # This function is used to print the linked list 
        p = self.head

        while(p):
            print(p.info)
            p = p.next

# the executin the code starts here

list1 = LinkedList()
list1.head = NodeClass("Napolean")
n2 = NodeClass("332 - I am Nobody")
n3 = NodeClass(55)
n4 = NodeClass("This is another Element")
#Linking the Nodes
list1.head.next = n2
n2.next = n3
n3.next = n4

list1.PrintList()
