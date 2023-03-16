# python code to implement separate chaining hashing technique
# code by Akshat Aryan
import os
import numpy as np
'''you can only import modules if they are present in Python root lib folder, or if they are in current directory of the current program

the following code snippet allows us to import module from anywhere using its file path'''
import importlib
import sys
spec = importlib.util.spec_from_file_location("Llist", "../Linked list/singlyll.py") #here I have used relative path, alternatively, we can also give absolute path
ll = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = ll
spec.loader.exec_module(ll)

'''you can also uncomment the below code snippet if the singlyll.py is present in the same directory'''
# import singlyll as ll

class Hashtable():
    #initialising a hash table with the given size n, the indexes will be from 0 to n-1
    def __init__(self, n):
        self.size = n
        self.table = np.array([ll.Llist() for i in range(0, self.size)]) #using np to create an array of liked lists, linked lists imported from singly ll by me
        
    #function to insert elements into the hash table
    def insert(self, ele):
        index = ele % self.size #the index assigned to ele is ele % self.size
        self.table[index].insert_rear(ele) #inserting ele at the rear of the linked list present at the index

    #function to delete the elements from the hash table
    def delete(self, ele):
        index = ele % self.size #finding the index of the ele to delete
        x = self.table[index].delete_pos(ele) #using the delete_pos function of singlyll.py to delete the specified element from the linked list present at the index position
        return x #returns None when element not found or returns the element if found and deleted
    
    #function to display the hash table
    def display(self):
        for i in range(0, self.size):
            print(i, "=   ", end = " ") #printing the value of index
            temp =self.table[i].head
            while(temp != None):
                print(temp.data, end = "\t") #instead of using singlyll's display function, this loop simply iterates the linked list and displays the values with tab spaces to separate them
                temp = temp.link
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
        print("Your choices are: 1. Insert 2. Delete 3. Display 4. Exit")
        ch = int(input("Enter your choice(1/2/3/4):"))
        if(ch == 1):
            clear()
            x = int(input("Enter the element you want to insert:"))
            ht.insert(x)
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
            ht.display()
            pausenclear()
        elif(ch == 4):
            clear()
            break
        