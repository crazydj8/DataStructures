#This is a python code to implement queue in python 
#code by Akshat Aryan
import os

class Queue():
    #Initialising the queue, front and rear
    def __init__(self):
        self.queue = []#in python you have the liberty to use any iterable, in our case we have used list
        self.front = None
        self.rear = None
        
    #returns 1 if queue is empty, returns 0 otherwise
    def isempty(self):
        if self.queue == []:
            return True
        else:
            return False
    
    #enqueues an item to the stack, item always enters the rear of the queue     
    def enqueue(self, x):
        self.queue.append(x)
        self.front = 0
        self.rear = len(self.queue) - 1
    
    #dequeues an item from the stack, item always leaves the queue from front    
    def dequeue(self):
        if self.isempty(): #if pop is called when stack is empty, underflow occurs
            return None
        else:
            self.item = self.queue.pop(0)
            if self.isempty():
                self.front = None
                self.rear = None
            else:
                self.rear = len(self.queue) - 1
            return(self.item)
    
    #peek function checks and returns the 'value' of front(does not return the index position)
    def peek(self):
        if self.isempty(): #if peek is called when stack is empty, underflow occurs returns None
            return None
        else:
            return self.queue[self.front]
    
    def display(self):
        if self.isempty():
            print("List Empty")
        else:
            print("Queue:")
            for i in range(0, len(self.queue)):
                print(self.queue[i])

#functions to clear screen for the menu driven program
def clear():
    os.system("cls")
def pausenclear():
    input("Press enter to continue:")
    os.system("cls")  

if __name__ == "__main__":
    # Creating th queue object
    q1 = Queue()
    
    #Menu: (self explanatory)
    while True:
        print("Your choices are: 1. Enqueue 2. Dequeue 3. Peep 4. Display 5. Exit")
        ch = int(input("Enter your choice(1/2/3/4/5):"))
        if ch == 1:
            clear()
            a = int(input("Enter element to enqueue:"))
            q1.enqueue(a)
            print(a, "Enqueued successfully")
            pausenclear()

        elif ch == 2:
            clear()
            itm = q1.dequeue()
            if(itm != None):
                print("Successfully dequeued:", itm)
            else:
                print("Underflow")
            pausenclear()
        
        elif ch == 3:
            clear()
            itm = q1.peek()
            if(itm != None):
                print ("Element at front =", itm)
            else:
                print("Underflow")
            pausenclear()
            
        elif ch == 4:
            clear()
            q1.display()
            pausenclear()
            
        elif ch == 5:
            break