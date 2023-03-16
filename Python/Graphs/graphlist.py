#Python code to implement graph in python using linked lists
#code By Akshat Aryan
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

class Graph():
    #we define agraph using an array containing linked lists correspoing to each node
    def __init__(self):
        self.nodelist = None
        self.created = 0
    
    #a function called to insert the destination node in the end of the linked list of the source node 
    def insertnode(self, source, dest):
        self.nodelist[source].insert_rear(dest)
    
    #create fuction creates a graph of n nodes and asks us to define the links using a simple loop
    def create(self):
        n = int(input("Enter the number of nodes:"))
        self.nodelist = np.array([ll.Llist() for i in range(0, n)]) #creating an array of n linked lists
        self.created = 1
        print("Graph initialised, your nodes are numbered from 0 to", n - 1)
        while(True):
            (i, j) = tuple(map(lambda x: int(x), input("Enter the two nodes you want to link(Enter -1 -1 to stop):").split()))
            if(i == -1 and j == -1): #-1 -1 are the sentinel to let the program know when to stop
                break
            else:
                if(j >= n or i >= n):
                    print("Node cannot take value >=", n)
                elif(i == j):
                    print("Cannot link a node to self")
                else:
                    self.insertnode(i, j)
                    #calling insertnode function to create a link

    #delete function deletes the existing graph
    def delete(self):
        self.nodelist = None #self.nodelist now points to null
        self.created = 0 #self.created = 0 indicated no graph is formed right now

    #a function that displays each linked list in the nodelist array
    def display(self):
        for i in range(0, len(self.nodelist)):
            print(str(i) + ":", end = " ")
            self.nodelist[i].display()
    
    #a recursive function to perform dfs traversal on the graph by specifying source node
    #fun fact: DFS traversal uses stack(here in the form of recursion)
    def dfs(self, source):
        global visited #a visited array is an array of the length of the nodes, if value = 0, node has not been visited, if value = 1, node has been visited
        visited[source] = 1
        print(source, end = "\t")
        curr = self.nodelist[source].head #initialising curr to the head of the linked list of source inside nodelist array
        while(curr != None):
            adj = curr.data
            if(visited[adj] == 0): #checking if the node inside the linked list of source has been visited or not
                self.dfs(adj)
            curr = curr.link
    
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
            curr = self.nodelist[source].head #initialising curr to the head of the linked list of source 
            while(curr != None):
                adj = curr.data
                if(visited[adj] == 0): #checking if the node inside the linked list of source has been visited or not
                    queue.append(adj)
                    visited[adj] = 1
                    print(adj, end = '\t')
                curr = curr.link

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
        print("Your choices are: 1. Create Graph 2. Delete Graph 3. Display Node List 4. DFS Traversal 5. BFS Traversal 6. Exit")
        ch = int(input("Enter your choice(1/2/3/4/5/6):"))
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
                g1.delete()
                print("Graph successfully deleted")
            else:
                print("Create a graph first!")
            pausenclear()
        elif(ch == 3):
            clear()
            if(g1.created == 1):
                g1.display()
            else:
                print("Create a graph first!")
            pausenclear()
        elif(ch == 4):
            clear()
            if(g1.created == 1):
                while(True):
                    x = int(input("Enter the source node:"))
                    if(x >= len(g1.nodelist)):
                        print("Please enter a value from 0 to", len(g1.nodelist) - 1, "only")
                    else:
                        break
                visited = np.zeros(len(g1.nodelist), int)
                print("DFS Taversal:")
                g1.dfs(x)
                for i in range(0, len(visited)):
                    if(visited[i] == 0):
                        g1.dfs(i)
                print()
            else:
                print("Create a graph first!")
            pausenclear()
        elif(ch == 5):
            clear()
            if(g1.created == 1):
                while(True):
                    x = int(input("Enter the source node:"))
                    if(x >= len(g1.nodelist)):
                        print("Please enter a value from 0 to", len(g1.nodelist) - 1, "only")
                    else:
                        break
                visited = np.zeros(len(g1.nodelist), int)
                print("BFS Taversal:")
                g1.bfs(x)
                for i in range(0, len(visited)):
                    if(visited[i] == 0):
                        g1.bfs(i)
                print()
            else:
                print("Create a graph first!")
            pausenclear()
        elif(ch == 6):
            break
        
        
