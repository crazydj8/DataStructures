# python code to implement hash tables using dictionary
#code by Akshat Aryan
import os

class Hashtable():
    #initialising a hashtable as a dictionary of size n and keys from 0 to n - 1, and their value, an empty list
    def __init__(self, n):
        self.hashtable = dict([[i, []] for i in range(0, n)])
        self.size = n

    #inserting an element inside the hash table
    def insert(self, ele):
        index = ele % self.size
        self.hashtable[index].append(ele) #appending an element to the index size. similar to separate chaining
    
    #deleting an element from the hash table
    def delete(self, ele):
        index = ele % self.size
        if ele not in self.hashtable[index]:
            return None
        else:
            self.hashtable[index].remove(ele) #using list remove method to remove from the list at specified index
            return ele
    
    #prints the dictionary
    def display(self):
        print(self.hashtable)

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
        