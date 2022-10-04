#This is a python code to implement linked lists in python 
import os

class Node():
    def __init__(self, data):
        self.data = data
        self.link = None

class Llist():
    def __init__(self):
        self.head = None
        
    def isempty(self):
        if (self.head == None):
            return True
        else:
            return False
        
    def traverse(self):
        if(self.isempty() == True):
            return None
        else:
            curr = self.head
            prev = self.head
            while(curr.link != None):
                prev = curr
                curr = curr.link
            return (prev, curr)
        
    def insert_front(self, ele):
        newnode = Node(ele)
        if(self.isempty() == True):
            self.head = newnode
        else:
            newnode.link = self.head
            self.head = newnode
        print(ele, "Inserted successfully")

    def insert_rear(self, ele):
        newnode = Node(ele)
        if(self.isempty() == True):
            self.head = newnode
        else:
            temp = self.traverse()[1]
            temp.link = newnode
        print(ele, "Inserted successfully")
            
    def insert_after(self, prev_data, ele):
        newnode = Node(ele)
        if(self.isempty() == True):
            print("Specified Node doesn't exist. Insert Unsuccessful")
        else:
            if (self.head.link == None):
                if(self.head.data == prev_data):
                    self.head.link = newnode
                    print(ele, "Inserted successfully")
                else:
                    print("Specified Node doesn't exist. Insert Unsuccessful")
            else:
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
    
    def delete_front(self):
        if(self.isempty() == True):
            print("List empty")
            return -1
        else:
            x = self.head.data
            self.head = self.head.link
            return x
        
    def delete_rear(self):
        if(self.isempty() == True):
            print("List empty")
            return -1
        else:
            if(self.head.link == None):
                x = self.head.data
                self.head = None
                return x
            else:
                curr = self.traverse()[1]
                prev = self.traverse()[0]
                x = curr.data
                prev.link = None
                del curr
                return x
        
    def delete_pos(self, ele):
        if(self.isempty() == True):
            print("List empty")
            return -1
        else:
            curr = self.head
            prev = self.head
            while(curr.link != None):
                prev = curr
                curr = curr.link
                if(curr.data == ele):
                    x = curr.data
                    prev.link = curr.link
                    return x
            if(curr.link == None):
                print("Specified Node doesn't exist. Delete Unsuccessful")
                return -1
        
    def search(self, ele):
        if(self.isempty() == True):
            print("List empty")
            return 0
        else:
            temp = self.head
            while(temp != None and temp.data != ele):
                temp = temp.link
            if (temp == None):
                print("Element not found")
                return 0
            else:
                print("Element found")
                return 1

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

def clear():
    os.system("cls")
def pausenclear():
    input("Press enter to continue:")
    os.system("cls")  

l1 = Llist()
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
        

