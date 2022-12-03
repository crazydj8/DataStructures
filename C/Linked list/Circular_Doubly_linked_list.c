#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *llink;    //llink stands for left link
    struct node *rlink;    //rlink stands for right link
};
typedef struct node NODE; //giving "struct node" an alias "NODE" for easier implementation

struct list{
    NODE *head; //for storing head pointer for the doubly linked list
};
typedef struct list LIST;


//To initialize the linked list head pointer
void init(LIST *p) 
{
    p->head=NULL;
}

//To make a node with given data and return its address.
NODE * getnode(int data)
{
    NODE *temp;
    temp=(NODE *)malloc(sizeof(NODE)); //Allocates memory for the node
    temp->data=data;                   //Assigns data to data variable of the node
    temp->llink=NULL;                  //Makes the left link pointer of that node as NULL
    temp->rlink=NULL;                  //Makes the right link pointer of that node as NULL
    return temp;                       //Returns the address of that node
}

//To insert the element at the begining of the linked list
void insert_front(LIST *p,int data)
{
    NODE *newNode=getnode(data);
    if(p->head==NULL) //if list is empty, insert as first node
    {
        p->head=newNode;
        p->head->rlink=p->head;     //The right link of the node will point to itself as it is circular doubly linked list
        p->head->llink=p->head;     //The left link of the node will point to itself as it is circular doubly linked list
    }
    else
    {
        NODE *first=p->head,*last=p->head->llink;     //storing the address of first node in 'first' and address of last node in 'last'
        newNode->rlink=first;
        first->llink=newNode;
        newNode->llink=last;
        last->rlink=newNode;
        p->head=newNode;                             //Changing the head pointer to the new first node i.e. newNode
    }
}

//To insert the element at the end of the linked list
void insert_rear(LIST *p,int data)
{
    NODE *newNode=getnode(data);
    if(p->head==NULL)
    {
        p->head=newNode;             //if list is empty, insert as first node
        p->head->rlink=p->head;      //The right link of the node will point to itself as it is circular doubly linked list
        p->head->llink=p->head;      //The left link of the node will point to itself as it is circular doubly linked list
    }
    else
    {
        NODE *first=p->head,*last=p->head->llink;
        newNode->rlink=first;              //Same as newNode->rlink=p->head;
        newNode->llink=last;               //Same as newNode->llink=p->head->llink;
        last->rlink=newNode;               //Same as p->head->llink->rlink=newNode;
        first->llink=newNode;              //Same as p->head->llink=newNode;
    }
}

//To insert the element at a specific position in the linked list
void insert_at_position(LIST *p,int data,int pos)
{
    int count=1;
    if(pos==0 || p->head==NULL)
    {
        insert_front(p,data);            //if position is 0 or the list has no elements then insert as first node
    }
    else
    {
        NODE *newNode=getnode(data);
        NODE *cur=p->head->rlink;
        while(cur!=p->head && count!=pos)   //finding the node address where newnode is going to be added
        {
            cur=cur->rlink;
            count++;
        }
        if(cur==p->head)                    //if the position is more than the size of the list(identified by cur==p->head as it comes back to first node), then add the element as last node
        {
            insert_rear(p,data);
        }
        else                             //inserting the newnode at the specific position;
        {
            NODE *prev;            //Logic to insert a node in the middle
            prev=cur->llink;       //Take a prev pointer pointing to the node after which newNode is to be inserted
            newNode->rlink=cur;    //Point newNode's rlink to the cur pointer
            newNode->llink=prev;   //point newNodes's llink to prev pointer
            prev->rlink=newNode;   //Change prev pointers rlink to point to newNode
            cur->llink=newNode;    //Change cur pointers llink to point to newNode
        }
    }
}

//To delete a node from the begining of the linked list
void delete_front(LIST *p)
{
    if(p->head==NULL)     //List empty condition
    {
        printf("\n The list is empty!\n");
    }
    else if(p->head->rlink==p->head)    //There is only one node in the list
    {
        NODE *temp=p->head;
        p->head=NULL;            //To avoid dangling pointers, we assign the head value as NULL
        printf("\n The deleted node data is %d \n",temp->data);
        free(temp);
    }
    else
    {
        NODE *temp=p->head;             //storing the address of the first node in a temporary variable.
        p->head=p->head->rlink;         //Shifting the head variable
        p->head->llink=temp->llink;     //Storing the address of last node in the left link of the new first node
        temp->llink->rlink=p->head;     //Storing the address of new first node in the right link of the last node
        printf("\n The deleted node data is %d \n",temp->data);
        free(temp);
    }
}

//To delete a node from the end of the linked list
void delete_rear(LIST *p)
{
    NODE *cur=p->head;
    if(p->head==NULL)  //List empty condition
    {
        printf("\n The list is empty!\n");
    }
    else if(p->head->rlink==p->head)          //There is only one node in the list
    {
        NODE *temp=p->head;
        p->head=NULL;             //To avoid dangling pointers, we assign the head value as NULL
        printf("\n The deleted node data is %d \n",temp->data);
        free(temp);
    }
    else
    {
        NODE *last=p->head->llink;     //storing the address of the last node in a temporary variable 'last'
        last->llink->rlink=p->head;    //Storing the address of first node in the right link of the second last node 
        p->head->llink=last->llink;    //Storing the address of second last node in the left link of the first node. Breaking all the connections to the last node
        printf("\n The deleted node data is %d \n",last->data);
        free(last);                    //Freeing the last node making the second last node as the last node
    }
}

//To delete a node with a particulat data from the linked list
void delete_node(LIST *p,int data)
{
    if(p->head==NULL)   //List empty condition
    {
        printf("\n The list is empty!\n ");
    }
    else
    {
        NODE *cur=p->head;
        if(cur->data!=data)    //Checking if the first node has the data required to be deleted
        {
            cur=cur->rlink;    
        }
        else
        {
            delete_front(p);    //If data is present in the first node itself
            return;
        }
        while(cur!=p->head && cur->data!=data)   //Traversing till either data is found or the list ends
        {
            cur=cur->rlink;
        }
        if(cur==p->head)     //If data is not found then cur will point to the first node again after iterating through the loop
        {
            printf("\n The data %d is not found in any node. Please try again! \n",data);
        }
        else if(cur==p->head->llink)    //If data is found in the last node
        {
            delete_rear(p);        //Reusing the functions
            return;
        }
        else      //If data is found in the middle of the list
        {
            cur->llink->rlink=cur->rlink;   //Making the prev nodes right link point to node next to the node being deleted
            cur->rlink->llink=cur->llink;   //Making the node's (which is next to the node being deleted) left link point to the previous node
            printf("\n Successfully deleted node with data %d \n",cur->data);
            free(cur); //freeing the node containing the data
        }
    }
}

//To search the position of an element in the linked list
int search(LIST *p,int ele)
{
    int count=1; //keeps track of the position of the node
    if(p->head==NULL)   //List empty condition
    {
        return -1;
    }
    else
    {
        NODE *temp=p->head;
        if(temp->data==ele)    //If data is found in the first node itself
        {
            return 0;          //Returning index value 0
        }
        else                   //If data is not present in first node then shifting to the second node
        {
            temp=temp->rlink;
        }
        while(temp!=p->head && temp->data!=ele )  //traverse the list untill element is found or the list ends.
        {
            temp=temp->rlink;
            count++;
        }
        if(temp==p->head) //if the element is not found in the list
        {
            return -1;
        }
        else
        {
            return count; //if element is found then returns its position
        }
    }
}

//To destory the list and free up memory
void destroy(LIST *p)
{
    if(p->head==NULL)               //List empty condition
    {
        printf("\n The list is empty!\n ");
        return;
    }
    NODE *cur=p->head,*last=p->head->llink,*temp;
    while(cur!=last)                 //till the list becomes empty except the last node
    {
        temp=cur;                    //temp pointer to point to a node
        cur=cur->rlink;              //shift the cur pointer to the next node
        free(temp);                  //free the node whose address is stored in temp
    }
    free(cur);                       //to free the last node
    p->head=NULL;                    //to avoid dangling/NULL pointers 
    printf("\n The list has been destroyed! \n");
}

//To print the elements of the linked list
void display(LIST *p)
{
    if(p->head==NULL)
    {
        printf("\n The list is empty!\n");
    }
    else
    {
        NODE *temp=p->head;
        while(temp!=p->head->llink) //traverses all the nodes of the linked list untill the last node is reached
        {
            printf("\n %d",temp->data); //prints the data of the nodes
            temp=temp->rlink;
        }
        printf("\n %d",temp->data);  //prints the last node data
        printf("\n");
    }
}

//Menu based operation
int main()
{
    int choice,data,pos,x;
    LIST l1;
    init(&l1);
    do{
        printf("\n 1.Insert Front 2.Insert Rear 3.Insert at specific position ");
        printf("\n 4.Delete Front 5.Delete Rear 6.Delete a specific element ");
        printf("\n 7.Search an element 8.Display List 9.Destroy List 10.EXIT");
        printf("\n Enter choice: ");
        scanf(" %d",&choice); 
        switch(choice)
        {
            case 1:printf("\n Enter the element to be inserted at front: ");
                   scanf("%d",&data);
                   insert_front(&l1,data);
                   break;
            case 2:printf("\n Enter the element to be inserted at rear: ");
                   scanf("%d",&data);
                   insert_rear(&l1,data);
                   break;
            case 3:printf("\n Enter the element to be inserted: ");
                   scanf("%d",&data);
                   printf("\n Enter the position where the element is to be inserted: ");
                   scanf("%d",&pos);
                   insert_at_position(&l1,data,pos);
                   break;
            case 4:delete_front(&l1);
                   break;
            case 5:delete_rear(&l1);
                   break;
            case 6:printf("\n Enter the element to be deleted: ");
                   scanf("%d",&data);
                   delete_node(&l1,data);
                   break;
            case 7:printf("\n Enter element to be searched: ");
                   scanf("%d",&data);
                   x=search(&l1,data);
                   if(x==-1)
                   {
                       printf("\n The element is not  found!\n");
                   }
                   else
                   {
                       printf("\n The element is found at %d position in the list\n",x);
                   }
                   break;
            case 8:display(&l1);
                   break;
            case 9:destroy(&l1);
                   break;
            case 10:printf("\n THANK YOU. EXITING..\n");
                    break;
            default:printf("\n Invalid choice. Please try again! \n");
                    break;
        }
    }while(choice!=10);
}