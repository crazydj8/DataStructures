#This is a python code to implement circular linked lists in python 
import os

class Node():
    #node contains data and link
    def __init__(self, data):
        self.data = data
        self.link = None

class Llist():
    #inititalising tail. You can only access the other elements from the head
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
        newnode = Node(ele)
        if(self.isempty() == True):
            self.tail = newnode
            self.tail.link = self.tail
        else:
            newnode.link = self.tail.link
            self.tail.link = newnode
        print(ele, "Inserted successfully")

    #traverses and inserts the element to the end of the list
    def insert_rear(self, ele):
        newnode = Node(ele)
        if(self.isempty() == True):
            self.tail = newnode
            self.tail.link = self.tail
        else:
            newnode.link = self.tail.link
            self.tail.link = newnode
            self.tail = newnode
        print(ele, "Inserted successfully")
    
    #inserts the element after the specified data node. If data node is not found, does nothing     
    def insert_after(self, prev_data, ele):
        newnode = Node(ele)
        if(self.isempty() == True):
            print("Specified Node doesn't exist. Insert Unsuccessful")
        else:
            if(self.tail.data == prev_data):
                self.insert_rear(ele)
            else:    
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
                        print(ele, "Inserted successfully")
                        break
                if(found != 1):
                    print("Specified Node doesn't exist. Insert Unsuccessful")

            
    #deletes the head element of the list
    def delete_front(self):
        if(self.isempty() == True):
            print("List empty")
            return -1
        else:
            if(self.tail.link == self.tail):
                x = self.tail.data
                self.tail = None
                return x
            else:
                x = self.tail.link.data
                self.tail.link = self.tail.link.link
                return x
                
    
    #deletes the last element of the list
    def delete_rear(self):
        if(self.isempty() == True):
            print("List empty")
            return -1
        elif(self.tail.link == self.tail):
            x = self.tail.data
            self.tail = None
            return x
        else:
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
        if(self.isempty() == True):
            print("List empty")
            return -1
        elif(self.tail.link == None):
            if(self.tail.data == ele):
                x = self.tail.data
                self.tail.data = None
                return x
            else:
                return -1
        else:
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
            print("Specified Node doesn't exist. Delete Unsuccessful")
            return -1
    
    #returns 1 if the searched element is found. else returns 0
    def search(self, ele):
        if(self.isempty() == True):
            print("List empty")
            return 0
        else:
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
        if(self.isempty() == True):
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
                a = input("Enter data you want to insert:")
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
        

