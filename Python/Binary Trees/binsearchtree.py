#This is a python code to implement binary searh trees in python 

import os

class Node():
    #node contains data and links
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinTree():
    #initialising root of the tree. All other elements can be accessed only through root of the tree
    def __init__(self):
        self.root = None

    #returns true if the tree is empty, else returns false
    def isempty(self):
        if(self.root == None):
            return True
        else:
            return False
        
    #inserts the element into the binary search tree
    def insert(self, ele):
        newnode = Node(ele) #Initialising a new node to be inserted
        if(self.isempty()):
            self.root = newnode #when list empty new node becomes root
        else:
            curr = self.root
            while(curr != None): #when list is not empty, traverse branches to find the correct position
                prev = curr;
                if(newnode.data == curr.data):
                    print(ele, "Already exists in tree")
                    return
                if(newnode.data > curr.data):
                    curr = curr.right
                else:
                    curr = curr.left
            if(newnode.data > prev.data):
                prev.right = newnode
            else:
                prev.left = newnode

    def delete(self, key):
        curr = self.root
        while(curr != None and curr.data != key): #finding the node containing key
            prev = curr
            if(key < curr.data):
                curr = curr.left
            else:
                curr = curr.right
        
        if(curr == None): #tree traversed, node not found
            print("Element not found")
            return -1
        
        if (curr.right == None or curr.left == None): #if the node to be deleted has only one child
            #next is assigned to its only child
            if(curr.right == None):
                next = curr.left
            else:
                next = curr.right
            if(curr == self.root): #if node to be deleted was root node with one child
                self.root = next
                del curr
                return
            #depending on which child it was, to its parent, it is replaced
            if(prev.right == curr): 
                prev.right = next
            elif(prev.left == curr):
                prev.left = next
            del curr
            return
            
        else: # if the node to be deleted has both children, it is to be replaced by the inordered successsor
            inprev = curr
            insucc = curr.right
            while(insucc.left != None): #finding the inordered successor
                inprev = insucc
                insucc = insucc.left
            if(inprev != curr): # if inordered successor is not a child of the node to be deleted
                inprev.left = insucc.right
            else:
                inprev.right = insucc.right
            curr.data = insucc.data
            del insucc
            return

    #finds min and max element in the tree, returns -1 if tree empty
    def minmax(self):
        if(self.isempty()):
            return (-1)
        else:
            temp = self.root
            while(temp.right != None):
                temp = temp.right
            min = temp.data
            temp = self.root
            while(temp.left != None):
                temp = temp.left
            max = temp.data
        return(min, max)
    
    #recursive function to search for an element in the tree
    def search(self, node, ele):
        if(node == None):
            return -1
        else:
            if(node.data == ele):
                return 0;
            elif(ele > node.data):
                self.search(node.right, ele)
            elif(ele < node.data):
                self.search(node.left, ele)
    
    #recursive function to display the tree preorder            
    def disp_preorder(self, root):
        temp = root
        if(temp != None):
            print(temp.data)
            self.disp_preorder(temp.left)
            self.disp_preorder(temp.right)
        else:
            return

    #recursive function to display the tree inorder
    def disp_inorder(self, root):
        temp = root
        if(temp != None):
            self.disp_inorder(temp.left)
            print(temp.data)
            self.disp_inorder(temp.right)
        else:
            return
    
    #recursive function to display the tree postorder        
    def disp_postorder(self, root):
        temp = root
        if(temp != None):
            self.disp_postorder(temp.left)
            self.disp_postorder(temp.right)
            print(temp.data)
        else:
            return
        
#functions to clear screen for the menu driven program
def clear():
    os.system("cls")
def pausenclear():
    input("Press enter to continue:")
    os.system("cls")  

if __name__ == "__main__":
    #creating the tree object
    t1 = BinTree()
    #Menu: (self explanatory)
    while True:
        clear()
        print("Your choices are: 1. Insert 2. Delete 3. Search 4. Find Min/Max 5. Display Preorder 6. Display Inorder 7.Display Postorder 8. Exit")
        ch = int(input("Enter your choice(1/2/3/4/5/6/7/8):"))
        if(ch == 1):
            clear()
            a = input("Enter you element:")
            t1.insert(a)
            pausenclear()
        elif(ch == 2):
            clear()
            b = input("Enter the data you want to delete:")
            x = t1.delete(b)
            if(x != -1):
                print("Successfully deleted", b)
            pausenclear()
        elif(ch == 3):
            clear()
            a = input("Enter the element you want to search:")
            x = t1.search(t1.root, a)
            if(x == 0):
                print(a, "Found")
            else:
                print(a, "Not Found")
            pausenclear()
        elif(ch == 4):
            clear()
            if(t1.minmax() != -1):
                (a, b) = t1.minmax()
                print("Min =", a, "Max =", b) 
            else:
                print("Tree empty:")
            pausenclear()
        elif(ch == 5):
            clear()
            print("Preorder display:")
            t1.disp_preorder(t1.root)
            pausenclear()
        elif(ch == 6):
            clear()
            print("Inorder display:")
            t1.disp_inorder(t1.root)
            pausenclear()
        elif(ch == 7):
            clear()
            print("Postorder display:")
            t1.disp_postorder(t1.root)
            pausenclear()
        elif(ch == 8):
            break
        