#include<stdio.h>
#include<stdlib.h>
struct node     //a single node of a tree containing a left and a right pointer
{
    int data;
    struct node *llink;
    struct node *rlink;
};
typedef struct node NODE; //giving "struct node" an alias "NODE" for easier implementation

struct treept
{
    NODE *root;     //for storing root pointer of the binary tree
};
typedef struct treept TREEPT;

void init(TREEPT *p)
{
    p->root=NULL;       //to initialize the root pointer of the tree to NULL
}

NODE * getnode(int ele)     //To make a node with given data and return its address
{
    NODE *temp;
    temp=(NODE *) malloc(sizeof(NODE));     //allocates memory for the node
    temp->data=ele;                         //store the data passed as the argument in the data field of the node
    temp->llink=NULL;                       //makes the left link of the node point to NULL
    temp->rlink=NULL;                       //makes the right link of the node point to NULL
    return temp;                            //returns the address of the node created
}

void insert(TREEPT *p,int ele)              //function to insert data to the binary tree
{   
    NODE *newnode;
    newnode=getnode(ele);                   //gets a node with the reqired data by calling th getnode function
    if(p->root==NULL)                       //if the tree is empty 
    {
        p->root=newnode;                    //make the new node as the root node
    }
    else
    {
        NODE *prev=NULL;                    //creating a 'prev' variable to store the address of previoiusly visited node
        NODE *cur=p->root;                  //storing the root pointer in a new variable 'cur' as current
        while(cur!=NULL)                    //iterating untill cur pointer becomes null so that we find a place to store the new node
        {   
            prev=cur;                       //assigning the prev pointer with address of current pointer
            if((cur->data)>(newnode->data))     //moving the current pointer based on the element we have to insert in the binary tree
            {
                cur=cur->llink;             //if new data is less than current pointer data
            }
            else
            {
                cur=cur->rlink;             //if new data is more than current pointer data
            }
        }                                   //we have cur=NULL and prev pointing to the leaf element after which data is to be inserted
        if((prev->data)>(newnode->data))        //inserting the newnode based on the new data being smaller of greater than the data in the prev pointer node
        {
            prev->llink=newnode;            //when new data is less than prev pointer data
        }
        else
        {
            prev->rlink=newnode;            //when new data is more than prev pointer data
        }       
    }
}

void inorder(NODE *p)                   //to print the values in the tree in in-order(left link->present data->right link)
{
    if(p!=NULL)
    {
        inorder(p->llink);              //recursivly call function to visit left link
        printf("\n %d",p->data);        //print the data in the present node
        inorder(p->rlink);              //recursivly call function to visit right link
    }
}

void preorder(NODE *p)                  //to print the values in the tree in pre-order(present data->left link->right link)
{
    if(p!=NULL)
    {
        printf("\n %d",p->data);        //print the data in the present node
        preorder(p->llink);             //recursivly call function to visit left link
        preorder(p->rlink);             //recursivly call function to visit right link
    }
}

void postorder(NODE *p)                 //to print the values in the tree in post-order(left link->right link->present data)
{
    if(p!=NULL)
    {
        postorder(p->llink);            //recursivly call function to visit left link
        postorder(p->rlink);            //recursivly call function to visit right link
        printf("\n %d",p->data);        //print the data in the present node
    }
}

//function to search for an element in the binary search tree. Returns NULL if not found, else, returns address of the node containing the data
NODE* search(NODE *root,int data)               
{
    if(root==NULL)                              //if the root is NULL, i.e. the tree has no elemets/nodes
    {
        return NULL;                            //return NULL
    }
    else if(root->data==data)                   //if root node contains the required data
    {
        return root;                            //return the address of the root itself
    }
    else                                        //traverse the tree to find the required data
    {
        if((root->data)>data)                   //if data in root node is more than required data
        {
            return(search(root->llink,data));       //recursively call search with the left linked subtree as new root
        }
        else if((root->data)<data)              //if data in root node is less than required data
        {
            return(search(root->rlink,data));       //recursively call search with the right linked subtree as new root
        }
    }
}



/*
//iterative approach for searching in binary tree
NODE* search(NODE *root,int data)               
{
    if(root==NULL)                              //if the root is NULL, i.e. the tree has no elemets/nodes
    {
        return NULL;                            //return NULL
    }
    else
    {
        NODE *cur=root;                         //taking a cur variable to traverse the tree
        while(cur!=NULL && cur->data!=data)     //traverse till the element is not found or the tree ends
        {
            if((cur->data)>data)                //if data in cur node is more than required data
            {
                cur=cur->llink;                 //move cur pointer to the left link of the tree(search in left subtree)
            }
            else if((cur->data)<data)           //if data in cur node is less than required data
            {
                cur=cur->rlink;                 //move cur pointer to the right link of the tree(search in right subtree)
            }       
        }
        return cur;
    }
}
*/


void delete(TREEPT *p,int ele)      //Function to delete an element from binary tree
{
    if(p->root==NULL)
    {
        printf("\n The tree is empty, nothing to delete! \n");
        return;
    }
    NODE *prev=NULL,*cur=p->root,*next;     //defining variable to traverse the tree
    while(cur!=NULL && cur->data!=ele)      //traverse the tree untill element is found or end of tree is reached
    {
        prev=cur;                           //keeping track of the last visited node
        if((cur->data)>ele)                 //if ele is less than current node data
        {
            cur=cur->llink;                 //traverse to the left subtree
        }
        else if((cur->data)<ele)            //if ele is more than current node data
        {
            cur=cur->rlink;                 //traverse to the right subtree
        }
    }
    if(cur==NULL)                           //if element is not found in the tree
    {   
        printf("\n The element is not  found!\n");
        return;
    }
    else if(cur->rlink==NULL || cur->llink==NULL)       //if the node having the element has only one child or no child
    {
        if(cur->rlink==NULL)                    //if right subtree is empty then left subtree is the next node
        {
            next=cur->llink;
        }
        else if(cur->llink==NULL)               //if left subtree is empty then left subtree is the next node
        {
            next=cur->rlink;
        }
        if(cur==p->root)                        //if root node contains the element to be deleted
        {
            p->root=next;                       //then change global  root to the next variable
            printf("\n The element %d is deleted successfully! \n",cur->data);
            return;                             
        }
        if(prev->llink==cur)            //if prev nodes left link contain cur node then replace it with next node, thus deleting the cur node containing the ele to be deleted
        {
            prev->llink=next;
        }
        else if(prev->rlink==cur)       //if prev nodes right link contain cur node then replace it with next node, thus deleting the cur node containing the ele to be deleted
        {
            prev->rlink=next;
        }
        printf("\n The element %d is deleted successfully! \n",cur->data);
        free(cur);
    }
    else
    {
        NODE *inprev=cur,*insucc=cur->rlink;
        while(insucc->llink!=NULL)
        {
            inprev=insucc;
            insucc=insucc->llink;
        }
        if(inprev==cur)
        {
            inprev->rlink=insucc->rlink;
        }
        else
        {
            inprev->llink=insucc->rlink;
        }
        printf("\n The element %d is deleted successfully! \n",cur->data);
        cur->data=insucc->data;
        free(insucc);
    }
    
}


void main() 
{
    TREEPT trpt;
    init(&trpt);
    int choice,data;
    NODE *x;
    do{
        printf("\n 1.Insert 2.Delete 3.Search 4.In-Order Traversal ");
        printf("\n 5.Pre-Order Traversal 6.Post-Order Traversal 7.Exit ");
        printf("\n Enter choice: ");
        scanf(" %d",&choice); 
        switch(choice)
        {
            case 1:printf("\n Enter the element to be inserted ");
                   scanf("%d",&data);
                   insert(&trpt,data);
                   break;
            case 2:printf("\n Enter the element to be deleted ");
                   scanf("%d",&data);
                   delete(&trpt,data);
                   break;
            case 3:if(trpt.root==NULL)
                    {
                        printf("\n The tree is empty, nothing to search \n");
                        break;
                    }
                    else
                    {
                        printf("\n Enter element to be searched: ");
                        scanf("%d",&data);
                        x=search(trpt.root,data);
                        if(x==NULL)
                        {
                             printf("\n The element is not  found!\n");
                        }
                        else
                        {
                            printf("\n The element %d is found\n",x->data);
                        }
                        break;
                    }
            case 4:if(trpt.root==NULL)
                    {
                        printf("\n The tree is empty, nothing to printf \n");
                        break;
                    }
                    else
                    {
                    inorder(trpt.root);
                    break;
                    }
            case 5:if(trpt.root==NULL)
                    {
                        printf("\n The tree is empty, nothing to print! \n");
                        break;
                    }
                    else
                    {
                        preorder(trpt.root);
                        break;
                    }
            case 6:if(trpt.root==NULL)
                    {
                        printf("\n The tree is empty, nothing to print! \n");
                        break;
                    }
                    else
                    {
                        postorder(trpt.root);
                        break;
                    }
            case 7:printf("\n EXITING...\n");
                    break;
            default:printf("\n Invalid choice. Please try again! \n");
                    break;
        }
    }while(choice!=7);
}