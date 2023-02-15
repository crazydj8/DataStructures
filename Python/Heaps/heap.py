#this is a python code to implement heaps 
import os
import numpy as np

class Heap():
    def __init__(self, n):         #this is an array implementation of heap
        self.max_val = n           #setting the max value of index postion heap can take
        self.heap_arr = np.zeros(n + 1, int) # creating an array with all zeroes, heap index starts from 1 so we inititalize array with n + 1
        self.count = 0             #count variable keeps track of the number of elements in the heap
    
    def isempty(self):            #returns true if heap empty else returns false
        return True if(self.count == 0) else False
    
    def shift_up(self):            #algorithm used to insert elements into the heap in descending order, the largest value will be the root
        i = self.count             #assigning position of the last element to i
        j = i // 2                 #assigning postition of the parent of element at i to j
        while(i > 1 and self.heap_arr[i] >= self.heap_arr[j]): #till we reach the root and the child value is greater than parent
            temp = self.heap_arr[j]#swap(these 3 lines)
            self.heap_arr[j] = self.heap_arr[i]
            self.heap_arr[i] = temp
            i = j                  #i is now assigned the value of j(i now has the position the parent of the previous i)
            j = i // 2             #j is now assigned the value of the parent of new i
    
    def insert(self, ele):         #inserts the specified element into the heap
        if(self.count == self.max_val):     #heap full
            return -1
        else:
            self.count += 1            #increments count by 1
            self.heap_arr[self.count] = ele #places the newly inserted element into the last position
            self.shift_up()            #shift_up is called to heapify
            return 0
    
    def shift_down(self):
        k = 1                      #position starting node
        v = self.heap_arr[k]       #value of starting node
        heap = False               #a flag for checking if heap statisfies or not
        while(not(heap) and 2 * k <= self.count):
            j = 2 * k              #position of left child of node at k
            if(j < self.count):    #if child exists
                if(self.heap_arr[j + 1] > self.heap_arr[j]): #comparing if the right child is greater than left child of node at k
                    j += 1         #if right child greater, j updates to position of right child
            if(v > self.heap_arr[j]): #comparing if value of the parent node 'k' is greater than the largest of its two children
                heap = True        #if value of parent is greater, heap is satisfied
            else:
                self.heap_arr[k] = self.heap_arr[j] #if not, value of parent is overwritten with the value of child
                k = j               #k value is now set to the position of the larger child
        self.heap_arr[k] = v        #position of the larger child is now updated with the value of parent which was smaller
        
    def delete(self):               #deletes element with highest value(like in a priority queue)
        if(self.isempty()):
            return -1
        else:
            x = self.heap_arr[1]
            self.heap_arr[1] = self.heap_arr[self.count] #the root(containing the largest element) is switched with the last element of the heap 
            self.count -= 1         #count value is now decremented
            self.shift_down()       #shift_down is now called to heapify with the decremented count value
            return x
    
    def display(self):              #displays the heap array contents in index order, with spaces
        if(self.count == 0):
            print("Heap Empty")
        else:
            for i in range(1, self.count + 1):
                if(i != self.count):
                    print(self.heap_arr[i], end = " ")
                else:
                    print(self.heap_arr[i])
#functions to clear screen for the menu driven program
def clear():
    os.system("cls")
def pausenclear():
    input("Press enter to continue:")
    os.system("cls")  

if __name__ == "__main__":
    #creating the heap object of defined array size
    h1 = Heap(3) 
    #Menu: (self explanatory)
    while True:
        clear()
        print("Your choices are: 1. Insert 2. Delete 3. Display 4. Exit")
        ch = int(input("Enter your choice(1/2/3/4):"))
        if(ch == 1):
            clear()
            a = input("Enter you element:")
            x = h1.insert(a)
            if(x == -1):
                print("Heap Full")
            pausenclear()
        elif(ch == 2):
            clear()
            x = h1.delete()
            if(x != -1):
                print("Successfully deleted", x)
            else:
                print("Heap Empty")
            pausenclear()
        elif(ch == 3):
            clear()
            h1.display()
            pausenclear()
        elif(ch == 4):
            break