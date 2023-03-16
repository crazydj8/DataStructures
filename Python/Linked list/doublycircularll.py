#This is a python code to implement circular linked lists in python 
#Code by Akshat Aryan
import os

class Node():
    #node contains data and link
    def __init__(self, data):
        self.data = data
        self.llink = None
        self.rlink = None

class Llist():
    #inititalising head. You can only access the other elements from the head
    def __init__(self):
        self.head = None
    
    #returns true is list is empty, else returns False
    def isempty(self):
        if (self.head == None):
            return True
        else:
            return False
    
    #inserts element at the front of the list, changes head
    def insert_front(self, ele):
        newnode = Node(ele) # Initialising node
        if(self.isempty()): #when list is empty
            self.head = newnode
            self.head.llink = self.head
            self.head.rlink = self.head
        else: #when list is not empty
            newnode.llink = self.head.llink
            newnode.rlink = self.head
            self.head.llink.rlink = newnode
            self.head.llink = newnode
            self.head = newnode

    #traverses and inserts the element to the end of the list
    def insert_rear(self, ele):
        newnode = Node(ele) # Initialising node
        if(self.isempty()): #when list is empty
            self.head = newnode
            self.head.llink = self.head
            self.head.rlink = self.head
        else: #when list is not empty
            newnode.llink = self.head.llink
            newnode.rlink = self.head
            self.head.llink.rlink = newnode
            self.head.llink = newnode
    
    #inserts the element after the specified data node. If data node is not found, does nothing     
    def insert_after(self, prev_data, ele):
        newnode = Node(ele) # Initialising node
        if(self.isempty()): #when list is empty
            return 0
        else: #when list is not empty
            if(self.head.rlink == self.head or self.head.data == prev_data): #if there is only one element in the list or if the selected node is head itself
                newnode.llink = self.head
                newnode.rlink = self.head.rlink
                self.head.rlink.llink = newnode
                self.head.rlink = newnode
                return 1
            else: #when there are more than 1 element in the list
                found = -1
                curr = self.head.rlink
                while(curr != self.head):
                    if(curr.data == prev_data):
                        found = 1
                        newnode.rlink = curr.rlink
                        newnode.llink = curr
                        curr.rlink.llink = newnode
                        curr.rlink = newnode
                        return 1
                    curr = curr.rlink
                if(found != 1):
                    return -1

    #deletes the head element of the list
    def delete_front(self):
        if(self.isempty()): #when list is empty
            return None
        else: #when list is not empty
            if(self.head.rlink == self.head): #if there is only one element in list
                x = self.head.data
                self.head = None
                return x
            else: #when there are more than 1 element in the list
                x = self.head.data
                self.head.llink.rlink = self.head.rlink
                self.head.rlink.llink = self.head.llink
                self.head = self.head.rlink
                return x
                
    #deletes the last element of the list
    def delete_rear(self):
        if(self.isempty()): #when list is empty
            return None
        elif(self.head.rlink == self.head): #if there is only one element in list
            x = self.head.data
            self.head = None
            return x
        else: #when there are more than 1 element in the list
            x = self.head.llink.data
            self.head.llink = self.head.llink.llink
            self.head.llink.rlink = self.head
            return x
        
    #deletes the specified element from the list
    def delete_pos(self, ele):
        if(self.isempty()): #when list is empty
            return None
        elif(self.head.data == ele): #if there is only one element in list
            x = self.delete_front()
            return x
        else: #when there are more than 1 element in the list
            curr = self.head.rlink
            while(curr != self.head):
                if(curr.data == ele):
                    x = curr.data
                    curr.llink.rlink = curr.rlink
                    curr.rlink.llink = curr.llink
                    del(curr)
                    return x
                curr = curr.rlink
            return None
    
    #returns 1 if the searched element is found. else returns 0
    def search(self, ele):
        if(self.isempty()): #when list is empty
            return 0
        else: #when list is not empty
            temp = self.head.rlink
            while(temp != self.head and temp.data != ele):
                temp = temp.rlink
            if(temp == self.head and temp.data != ele):
                return -1
            else:
                return 1
            
    #displays the list in linear form
    def display(self):
        if(self.isempty()):
            print("List empty")
        else:
            print("Your linked list is:")
            temp = self.head
            while(temp != self.head.llink):
                print(temp.data, end = "\t")
                temp = temp.rlink
            print(temp.data)
            
#functions to clear screen for the menu driven program
def clear():
    os.system("cls")
def pausenclear():
    input("Press enter to continue:")
    os.system("cls")  

if __name__ == "__main__":
    #creating the linked list object
    l1 = Llist()

    #Menu: (self explanatory)
    while True:
        clear()
        print("Your choices are: 1. Insert 2. Delete 3. Search 4. Display 5. Exit")
        ch = int(input("Enter your choice(1/2/3/4/5):"))
        if(ch == 1):
            while True:
                clear()
                print("Your choices are: 1. Insert Front 2. Insert Rear 3. Insert after 4. Back")
                ch2 = int(input("Enter your choice(1/2/3/4/5):"))
                if(ch2 == 1):
                    a = input("Enter data:")
                    l1.insert_front(a)
                    print(a, "Inserted successfully")
                elif(ch2 == 2):
                    a = input("Enter data:")
                    l1.insert_rear(a)
                    print(a, "Inserted successfully")
                elif(ch2 == 3):
                    a = input("Enter data you want to insert:")
                    b = input("Enter the data after which you want to insert:")
                    x = l1.insert_after(b, a)
                    if(x == 0):
                        print("list empty")
                    elif(x == -1):
                        print("Specified node does not exist.")
                    else:
                        print(a, "Inserted successfully")
                elif(ch2 == 4):
                    pausenclear()
                    break
                pausenclear()
        elif(ch == 2):
            while True:
                clear()
                print("Your choices are: 1. Delete Front 2. Delete Rear 3. Delete specified 4. Back")
                ch2 = int(input("Enter your choice(1/2/3/4/5):"))
                if(ch2 == 1):
                    x = l1.delete_front()
                elif(ch2 == 2):
                    clear()
                    x = l1.delete_rear()
                elif(ch2 == 3):
                    clear()
                    b = input("Enter the data you want to delete:")
                    x = l1.delete_pos(b)
                elif(ch2 == 4):
                    pausenclear()
                    break
                if(x != None):
                    print(x, "Deleted successfully")
                else:
                    print("Delete unsuccessful")
                pausenclear()
        elif(ch == 3):
            clear()
            a = input("Enter the element you want to search:")
            x = l1.search(a)
            if(x == 0):
                print("list empty")
            elif(x == -1):
                print("Element not found")
            else:
                print("Element found")
            pausenclear()
        elif(ch == 4):
            clear()
            l1.display()
            pausenclear()
        elif(ch == 5):
            break
            

