#This is a python code to implement doubly linked lists in python 
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
        
    #traverses and returns the last element
    def traverse(self):
        if(self.isempty() == True):
            return None
        else:
            curr = self.head
            while(curr.rlink != None):
                curr = curr.rlink
            else:
                return curr
    
    #inserts element at the front of the list, changes head
    def insert_front(self, ele):
        newnode = Node(ele)
        if(self.isempty() == True):
            self.head = newnode
        else:
            newnode.rlink = self.head
            self.head.llink = newnode
            self.head = newnode
        print(ele, "Inserted successfully")

    #traverses and inserts the element to the end of the list
    def insert_rear(self, ele):
        newnode = Node(ele)
        if(self.isempty() == True):
            self.head = newnode
        else:
            temp = self.traverse()
            temp.rlink = newnode
            newnode.llink = temp
        print(ele, "Inserted successfully")
    
    #inserts the element after the specified data node. If data node is not found, does nothing     
    def insert_after(self, prev_data, ele):
        newnode = Node(ele)
        if(self.isempty() == True):
            print("Specified Node doesn't exist. Insert Unsuccessful")
        else:
            if (self.head.rlink == None):
                if(self.head.data == prev_data):
                    self.head.rlink = newnode
                    newnode.llink = self.head
                    print(ele, "Inserted successfully")
                else:
                    print("Specified Node doesn't exist. Insert Unsuccessful")
            else:
                found = -1
                curr = self.head
                while(curr != None):
                    if(curr.data == prev_data):
                        found = 1
                        newnode.rlink = curr.rlink
                        curr.rlink = newnode
                        newnode.llink = curr
                        newnode.rlink.llink = newnode
                        print(ele, "Inserted successfully")
                        break
                    curr = curr.rlink
                if(found != 1):
                    print("Specified Node doesn't exist. Insert Unsuccessful")
    
    #deletes the head element of the list
    def delete_front(self):
        if(self.isempty() == True):
            print("List empty")
            return -1
        else:
            x = self.head.data
            self.head = self.head.rlink
            self.head.llink = None
            return x
    
    #deletes the last element of the list
    def delete_rear(self):
        if(self.isempty() == True):
            print("List empty")
            return -1
        else:
            if(self.head.rlink == None):
                x = self.head.data
                self.head = None
                return x
            else:
                curr = self.traverse()
                x = curr.data
                curr.llink.rlink = None
                del curr
                return x
    
    #deletes the specified element from the list
    def delete_pos(self, ele):
        if(self.isempty() == True):
            print("List empty")
            return -1
        else:
            curr = self.head
            while(curr.rlink != None):
                if(curr.data == ele):
                    x = curr.data
                    curr.llink.rlink = curr.rlink
                    return x
                curr = curr.rlink
            if(curr.rlink == None):
                print("Specified Node doesn't exist. Delete Unsuccessful")
                return -1
    
    #returns 1 if the searched element is found. else returns 0
    def search(self, ele):
        if(self.isempty() == True):
            print("List empty")
            return 0
        else:
            temp = self.head
            while(temp != None and temp.data != ele):
                temp = temp.rlink
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
            while(temp.rlink != None):
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
            

