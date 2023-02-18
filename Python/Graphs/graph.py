#Python code to implement graphs 
import os
import numpy as np

class Graph():
    #we define a graph using an adjacency matrix of dimensions nxn
    def __init__(self):
        self.adjmat = None
        self.created = 0 #flag to indicate that a graph has been created

    #create fuction creates a graph of nxn nodes and asks us to define the links using a simple loop
    def create(self):
        n = int(input("Enter the number of nodes:"))
        self.adjmat = np.zeros(n ** 2, int).reshape(n, n) #np.zeros function directly creates an array of zeros of specified length. np.reshape then reshapes the array in the specified dimensions, here in our case: nxn 
        self.created = 1
        print("Graph initialised, your nodes are numbered from 0 to", n - 1)
        while(True):
            (i, j) = tuple(map(lambda x: int(x), input("Enter the two nodes you want to link(Enter -1 -1 to stop):").split()))
            if(i == -1 and j == -1): #-1 -1 are the sentinel to let the program know when to stop
                break
            else:
                if(i == j):
                    print("Cannot link a node to self")
                else:
                    self.adjmat[i][j] = 1 #1 value in the adjmat[i][j] signifies that a link exists from i to j

    #delete function deletes the existing graph
    def delete(self):
        self.adjmat = None #points self.adjmat to None now
        self.created = 0 #self.created = 0 means that the graph does not exist
        
    #a function to edit current links
    def edit(self, flag):
        if(flag == 1): # to add links
            while(True):
                (i, j) = tuple(map(lambda x: int(x), input("Enter the two nodes you want to link(Enter -1 -1 to stop):").split()))
                if(i == -1 and j == -1): #sentinel to stop
                    break
                else:
                    if(i == j):
                        print("Cannot link a node to self")
                    else:
                        if(self.adjmat[i][j] == 1):
                            print("Link already exists")
                        else:
                            self.adjmat[i][j] = 1
        else: #to remove links
            while(True):
                (i, j) = tuple(map(lambda x: int(x), input("Enter the two nodes you want to remove link from(Enter -1 -1 to stop):").split()))
                if(i == -1 and j == -1): #sentinel to stop
                    break
                else:
                    if(self.adjmat[i][j] == 0):
                        print("No link exists")
                    else:
                        self.adjmat[i][j] = 0
    
    #a function to return the values of in frequency and out frequency of each node in the form of two dictionaries
    def innout(self):
        d1 = {}
        d2 = {}
        inn = self.adjmat.sum(axis= 0) #a numpy array method to create an array of sum of all columns when axis = 0
        out = self.adjmat.sum(axis= 1) #a numpy array method to create an array of sum of all columns when axis = 1
        for i in range(0, len(self.adjmat)): #assigning the values(sums) to the keys(nodes)
            d1[i] = inn[i]
            d2[i] = out[i]
        return d1, d2

    #a function that displays the adjacency matrix corresponding to the current graph object
    def display(self):
        print(self.adjmat)
        '''Or you can use the code snippet below, but it will be inconsistent for digits > 1'''
        # for i in range(0, len(self.adjmat) + 1):
        #     if(i == 0):
        #         print(" ", end = " ")
        #     else:
        #         print(i - 1, end = " ")
        # print()
        # for i in range(0, len(self.adjmat)):
        #     print(i, end = " ")
        #     for j in range(0, len(self.adjmat)):
        #         print(self.adjmat[i][j], end = " ")
        #     print()

    #a recursive function to perform dfs traversal on the graph by specifying source node
    #fun fact: DFS traversal uses stack(here in the form of recursion)
    def dfs(self, source):
        global visited #a visited array is an array of the length of the nodes, if value = 0, node has not been visited, if value = 1, node has been visited
        visited[source] = 1
        print(source, end = "\t")
        for i in range(0, len(self.adjmat)):
            if(self.adjmat[source][i] == 1 and visited[i] == 0): #checking if a link exists from source to i and i has not been visited
                self.dfs(i)
                
    #an iterative function to perform bfs traversal on the graph by specifying source node
    #fun fact: BFS Traversal uses queue        
    def bfs(self, source):
        global visited
        queue = [] #initialising a simple queue here using list, can also be done by creating a queue object by importing queue.py from the same repo
        f = 0 #front pointer
        visited[source] = 1
        print(source, end = "\t")
        queue.append(source)
        while(f <= len(queue) - 1): #checking if front pointer is greater than the rear
            source = queue[f]
            f += 1
            for i in range(0, len(self.adjmat)):
                if(self.adjmat[source][i] == 1 and visited[i] == 0): #if link exists from source to i and i is not visited, then i is added to the queue and its value is printed
                    queue.append(i)
                    visited[i] = 1
                    print(i, end = "\t") 

#functions to clear screen for the menu driven program
def clear():
    os.system("cls")
def pausenclear():
    input("Press enter to continue:")
    os.system("cls")  

if __name__ == "__main__":
    #creating the graph object
    g1 = Graph()
    #Menu: (self explanatory)
    while True:
        clear()
        print("Your choices are: 1. Create Graph 2. Edit Graph 3. Delete Graph 4. Display Adjacency Matrix 5. In and Our Frequencies 6. DFS Traversal 7. BFS Traversal 8. Exit")
        ch = int(input("Enter your choice(1/2/3/4/5/6/7/8):"))
        if(ch == 1):
            clear()
            if(g1.created == 1):
                conf = input("Your previous graph will be overwritten. Are you sure you want to proceed?(y/n)")
                if(conf == 'n'):
                    continue
            g1.create()
            pausenclear()
        elif(ch == 2):
            clear()
            if(g1.created == 1):
                while True:
                    clear()
                    print("Your choices are: 1. Add links 2. Remove Links 3. Go Back")
                    ch2 = int(input("Enter your choice(1/2/3):"))
                    if(ch2 == 1):
                        clear()
                        g1.edit(1)
                        pausenclear()
                    elif(ch2 == 2):
                        clear()
                        g1.edit(0)
                        pausenclear()
                    elif(ch2 == 3):
                        break
            else:
                print("Create a graph first!")
            pausenclear()
        elif(ch == 3):
            clear()
            if(g1.created == 1):
                g1.delete()
                print("Graph successfully deleted")
            else:
                print("Create a graph first!")
            pausenclear()
        elif(ch == 4):
            clear()
            if(g1.created == 1):
                g1.display()
            else:
                print("Create a graph first!")
            pausenclear()
        elif(ch == 5):
            clear()
            if(g1.created == 1):
                (inn, out) = g1.innout()
                print("In Frequency{node:freq}:\n", inn)
                print("Out Frequency{node:freq}:\n", out)
            else:
                print("Create a graph first!")
            pausenclear()
        elif(ch == 6):
            clear()
            if(g1.created == 1):
                while(True):
                    x = int(input("Enter the source node:"))
                    if(x >= len(g1.adjmat)):
                        print("Please enter a value from 0 to", len(g1.adjmat) - 1, "only")
                    else:
                        break
                visited = np.zeros(len(g1.adjmat), int)
                print("DFS Taversal:")
                g1.dfs(x)
                print()
            else:
                print("Create a graph first!")
            pausenclear()
        elif(ch == 7):
            clear()
            if(g1.created == 1):
                while(True):
                    x = int(input("Enter the source node:"))
                    if(x >= len(g1.adjmat)):
                        print("Please enter a value from 0 to", len(g1.adjmat) - 1, "only")
                    else:
                        break
                visited = np.zeros(len(g1.adjmat), int)
                print("BFS Taversal:")
                g1.bfs(x)
                print()
            else:
                print("Create a graph first!")
            pausenclear()
        elif(ch == 8):
            break
        