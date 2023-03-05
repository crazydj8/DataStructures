# python code to implement linear probing hashing technique
import os
import numpy as np

#an array of these nodes will be used as the hash table
class Node():
    #a node will contain an id(can also contain more fields, and a flag that indicates if its used or not
    def __init__(self):
        self.id = None
        self.used = -1
        
class Hashtable():
    #initialising the hashtable as an array of nodes, size variable containing the size and a count variable indicating no of elements in the table
    def __init__(self, n):
        self.hashtable = np.array([Node() for i in range(0, n)])
        self.size = n
        self.count = 0
    
    #a function that returns true if the hash table is empty and false otherwise
    def isempty(self):
        if(self.count == 0):
            return True
        else:
            return False
    #function that returns true if the hash table is full and false otherwise 
    def isfull(self):
        if(self.count == self.size):
            return True
        else:
            return False
    
    #function to insert elemen into the hash table using linear probing as a solution for collision. returns -1 if table is full
    def insert(self, id):
        if(self.isfull()):
            return -1
        index = id % self.size
        while(self.hashtable[index].used != -1):
            index = (index + 1) % self.size #linear probing: adding to index cyclically by 1
        self.hashtable[index].id = id
        self.hashtable[index].used = 1
        self.count += 1
    
    #function to delete an element from the hash table. uses count variable for checking if entire table has been traversed
    def delete(self, key):
        if(self.isempty()):
            return None
        index = key % self.size
        i = 0
        while(self.hashtable[index].id != key and i < self.count): #keep increasing index until the element is found or i reaches count which means entire table has been traversed
            index = (index + 1) % self.size
            if(self.hashtable[index].used == 1):
                i += 1
        if(self.hashtable[index].id == key and self.hashtable[index].used == 1):
            self.hashtable[index].used = -1
            self.count -= 1
            return key
    
    #function to search if an element is present in the table(returns 1) or not(returns -1). returns 0 if table empty
    def search(self, key):
        if(self.isempty()):
            return 0
        index = key % self.size
        i = 0
        while(self.hashtable[index].id != key and i < self.count):
            index = (index + 1) % self.size
            if(self.hashtable[index].used == 1):
                i += 1
        if(self.hashtable[index].id == key and self.hashtable[index].used == 1):
            return 1
        else:
            return -1
    
    #function to display all the indexes of the hash table
    def display(self):
        if(self.isempty()):
            print("Hash table empty")
            return -1
        for i in range(0, self.size):
            print(str(i) + ":", end = " ")
            if(self.hashtable[i].used == 1):
                print(self.hashtable[i].id)
            else:
                print()

#functions to clear screen for the menu driven program
def clear():
    os.system("cls")
def pausenclear():
    input("Press enter to continue:")
    os.system("cls")  

if __name__ == "__main__":
    #creating the graph object
    ht = Hashtable(10)
    #Menu: (self explanatory)
    while True:
        clear()
        print("Your choices are: 1. Insert 2. Delete 3. Search 4. Display 5. Exit")
        ch = int(input("Enter your choice(1/2/3/4/5):"))
        if(ch == 1):
            clear()
            a = int(input("Enter the element you want to insert:"))
            x = ht.insert(a)
            if(x == -1):
                print("Insert unsuccessful, table full")
            pausenclear()
        elif(ch == 2):
            clear()
            a = int(input("Enter the element you want to delete:"))
            x = ht.delete(a)
            if(x != None):
                print(x, "Deleted successfully")
            else:
                print("Delete unsuccessful, element not present")
            pausenclear()
        elif(ch == 3):
            clear()
            a = int(input("Enter the element you want to search for:"))
            x = ht.search(a)
            if(x == 0):
                print("Element not found, table empty")
            elif(x == -1):
                print("Element not found.")
            else:
                print("Element found")
            pausenclear()
        elif(ch == 4):
            clear()
            ht.display()
            pausenclear()
        elif(ch == 5):
            clear()
            break