#This is a python code to implement circular linked lists in python 
#Code by Akshat Aryan
import os

class Node():
    #node contains data and link
    def __init__(self, data):
        self.data = data
        self.link = None

class Llist():
    #inititalising tail. You can only access the other elements from the tail
    def __init__(self):
        self.tail = None
    
    #returns true is list is empty, else returns False
    def isempty(self):
        if (self.tail == None):
            return True
        else:
            return False
    
    #inserts element at the front of the list, changes head
    def insert_front(self, ele):
        newnode = Node(ele) # Initialising node
        if(self.isempty()): #when list is empty
            self.tail = newnode
            self.tail.link = self.tail
        else: #when list is not empty
            newnode.link = self.tail.link
            self.tail.link = newnode

    #traverses and inserts the element to the end of the list
    def insert_rear(self, ele):
        newnode = Node(ele) # Initialising node
        if(self.isempty()): #when list is empty
            self.tail = newnode
            self.tail.link = self.tail
        else: #when list is not empty
            newnode.link = self.tail.link
            self.tail.link = newnode
            self.tail = newnode
    
    #inserts the element after the specified data node. If data node is not found, does nothing     
    def insert_after(self, prev_data, ele):
        newnode = Node(ele) # Initialising node
        if(self.isempty()): #when list is empty
            return 0
        else: #when list is not empty
            if(self.tail.data == prev_data): #if searched element is tail itself
                self.insert_rear(ele)
            else: #when there are more than 1 element in the list
                found = -1
                curr = self.tail.link
                prev = self.tail
                while(curr != self.tail):
                    prev = curr
                    curr = curr.link
                    if(prev.data == prev_data):
                        found = 1
                        newnode.link = prev.link
                        prev.link = newnode
                        return 1
                if(found != 1):
                    return -1

            
    #deletes the head element of the list
    def delete_front(self):
        if(self.isempty()): #when list is empty
            return None
        else: #when list is not empty
            if(self.tail.link == self.tail): #if there is only one element in list
                x = self.tail.data
                self.tail = None
                return x
            else: #when there are more than 1 element in the list
                x = self.tail.link.data
                self.tail.link = self.tail.link.link
                return x
                
    
    #deletes the last element of the list
    def delete_rear(self):
        if(self.isempty()): #when list is empty
            return None
        elif(self.tail.link == self.tail): #if there is only one element in list
            x = self.tail.data
            self.tail = None
            return x
        else: #when there are more than 1 element in the list
            curr = self.tail.link
            while(curr.link != self.tail):
                curr = curr.link
            curr.link = self.tail.link
            x = self.tail.data
            del(self.tail)
            self.tail = curr
            return x
                
    #deletes the specified element from the list
    def delete_pos(self, ele):
        if(self.isempty()): #when list is empty
            return None
        elif(self.tail.link == self.tail): #if there is only one element in list
            if(self.tail.data == ele):
                x = self.tail.data
                self.tail.data = None
                return x
            else:
                return -1
        else: #when there are more than 1 element in the list
            curr = self.tail.link
            prev = self.tail
            while(curr != self.tail):
                if(curr.data == ele):
                    x = curr.data
                    prev.link = curr.link
                    if(curr == self.tail):
                        self.tail = prev
                    return x
                prev = curr
                curr = curr.link
            return None
    
    #returns 1 if the searched element is found. else returns 0
    def search(self, ele):
        if(self.isempty()): #when list is empty
            print("List empty")
            return 0
        else: #when list is not empty
            temp = self.tail.link
            while(temp != self.tail and temp.data != ele):
                temp = temp.link
            if(temp == self.tail and temp.data != ele):
                print("Element not found")
                return 0
            else:
                print("Element found")
                return 1
            
    #displays the list in linear form
    def display(self):
        if(self.isempty()):
            print("List empty")
        else:
            print("Your linked list is:")
            temp = self.tail.link
            while(temp != self.tail):
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
                    print("Delete Unsuccessful")
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
            

