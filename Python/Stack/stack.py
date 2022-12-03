#This is a python code to implement stacks in python 
import os

class Stack():
    #Initialising the stack and top
    def __init__(self):
        self.stk = [] #in python you have the liberty to use any iterable, in our case we have used list
        self.top = None
    
    #returns 1 if stack is empty, returns 0 otherwise
    def isempty(self):
        if self.stk == []:
            return True
        else:
            return False
    
    #pushes an element onto the stack, updates value of top    
    def push(self, x):
        self.stk.append(x)
        self.top = len(self.stk) - 1
    
    #pops an element from the stack, updates value of top
    def pop(self):
        if self.isempty(): #if pop is called when stack is empty, underflow occurs
            print("Underflow")
            return -1
        else:
            self.item = self.stk.pop()
            if self.isempty():
                self.top = None
            else:
                self.top = len(self.stk) - 1
            return(self.item)

    #peek function checks and returns the 'value' of top(does not return the index position)
    def peek(self):
        if self.isempty(): #if peek is called when stack is empty, underflow occurs, returns None
            print("Underflow")
            return None
        else:
            #self.top = len(self.stk) - 1
            return self.stk[self.top]
        
    # displays the stack from top to bottom    
    def display(self):
        if self.isempty():
            print("List Empty")
        else:
            #self.top = len(self.stk) - 1
            print("Stack:")
            for i in range(self.top, -1, -1):
                print(self.stk[i])
                
#functions to clear screen for the menu driven program
def clear():
    os.system("cls")
def pausenclear():
    input("Press enter to continue:")
    os.system("cls")  
    
if __name__ == "__main__":
    #creating the stack object
    s1 = Stack()

    #Menu: (self explanatory)
    while True:
        clear()
        print("Your choices are: 1. Push 2. Pop 3. Peek 4. Display 5. Exit")
        ch = int(input("Enter your choice(1/2/3/4/5):"))
        if(ch == 1):
            clear()
            a = int(input("Enter element to push:"))
            s1.push(a)
            print(a, "Pushed successfully")
            pausenclear()
            
        elif(ch == 2):
            clear()
            itm = s1.pop()
            print("Successfully deleted:", itm)
            pausenclear()
    
        elif(ch == 3):
            clear()
            itm = s1.peek()
            print ("Element on Top =", itm)
            pausenclear()
            
        elif(ch == 4):
            clear()
            s1.display()
            pausenclear()
            
        elif(ch == 5):
            break