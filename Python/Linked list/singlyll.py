#This is a python code to implement linked lists in python 
#Implementation of linked list in python gives you the advantage of storing any type of data in the data field of the node
import os

class Node():
    #node contains data and link
    def __init__(self, data):
        self.data = data
        self.link = None

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
        
    #traverses and returns the last element and its previous element of the list
    def traverse(self):
        if(self.isempty() == True):
            return None
        else:
            curr = self.head
            prev = self.head
            while(curr.link != None):
                prev = curr
                curr = curr.link
            if(prev == curr):
                return(None, curr)
            else:
                return (prev, curr)
    
    #inserts element at the front of the list, changes head
    def insert_front(self, ele):
        newnode = Node(ele) # Initialising node
        if(self.isempty() == True): #when list is empty
            self.head = newnode
        else: #when list is not empty
            newnode.link = self.head
            self.head = newnode
        print(ele, "Inserted successfully")

    #traverses and inserts the element to the end of the list
    def insert_rear(self, ele):
        newnode = Node(ele) # Initialising node
        if(self.isempty() == True): #when list is empty
            self.head = newnode
        else: #when list is not empty
            temp = self.traverse()[1]
            temp.link = newnode
        print(ele, "Inserted successfully")
    
    #inserts the element after the specified data node. If data node is not found, does nothing     
    def insert_after(self, prev_data, ele):
        newnode = Node(ele) # Initialising node
        if(self.isempty() == True): #when list is empty
            print("Specified Node doesn't exist. Insert Unsuccessful")
        else: #when list is not empty
            if (self.head.link == None): #if there is only one element in list
                if(self.head.data == prev_data):
                    self.head.link = newnode
                    print(ele, "Inserted successfully")
                else:
                    print("Specified Node doesn't exist. Insert Unsuccessful")
            else: #when there are more than 1 element in the list
                found = -1
                curr = self.head
                prev = self.head
                while(curr != None):
                    prev = curr
                    curr = curr.link
                    if(prev.data == prev_data):
                        found = 1
                        prev.link = newnode
                        newnode.link = curr
                        print(ele, "Inserted successfully")
                        break
                if(found != 1):
                    print("Specified Node doesn't exist. Insert Unsuccessful")
    
    #deletes the head element of the list
    def delete_front(self):
        if(self.isempty() == True): #when list is empty
            print("List empty")
            return -1
        else: #when list is not empty
            x = self.head.data
            self.head = self.head.link
            return x
    
    #deletes the last element of the list
    def delete_rear(self):
        if(self.isempty() == True): #when list is empty
            print("List empty")
            return -1
        else: #when list is not empty
            if(self.head.link == None): #if there is only one element in list
                x = self.head.data
                self.head = None
                return x
            else: #when there are more than 1 element in the list
                curr = self.traverse()[1]
                prev = self.traverse()[0]
                x = curr.data
                prev.link = None
                del curr
                return x
    
    #deletes the specified element from the list
    def delete_pos(self, ele):
        if(self.isempty() == True): #when list is empty
            print("List empty")
            return -1
        elif(self.head.link == None): #if there is only one element in list
            if(self.head.data == ele):
                x = self.head.data
                self.head = None
                return x
            else:
                print("Specified Node doesn't exist. Delete Unsuccessful")
                return -1
        else: #when there are more than 1 element in the list
            curr = self.head
            prev = None
            while(curr != None):
                if(curr.data == ele):
                    x = curr.data
                    if(curr != self.head):
                        prev.link = curr.link
                    else:
                        self.head = curr.link
                    return x
                prev = curr
                curr = curr.link
            if(curr == None):
                print("Specified Node doesn't exist. Delete Unsuccessful")
                return -1
    
    #returns 1 if the searched element is found. else returns 0
    def search(self, ele):
        if(self.isempty() == True): #when list is empty
            print("List empty")
            return 0
        else: #when list is not empty
            temp = self.head
            while(temp != None and temp.data != ele):
                temp = temp.link
            if (temp == None):
                print("Element not found")
                return 0
            else:
                print("Element found")
                return 1
    
    #displays the list in linear form
    def display(self):
        if(self.isempty() == True):
            print("List empty")
        else:
            print("Your linked list is:")
            temp = self.head
            while(temp.link != None):
                print(temp.data, end = "\t")
                temp = temp.link
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
                elif(ch2 == 2):
                    a = input("Enter data:")
                    l1.insert_rear(a)
                elif(ch2 == 3):
                    a = input("Enter data:")
                    b = input("Enter the data after which you want to insert:")
                    l1.insert_after(b, a)
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
                if(x != -1):
                    print(x, "Deleted successfully")
                pausenclear()
        elif(ch == 3):
            clear()
            a = input("Enter the element you want to search:")
            l1.search(a)
            pausenclear()
        elif(ch == 4):
            clear()
            l1.display()
            pausenclear()
        elif(ch == 5):
            break
            

