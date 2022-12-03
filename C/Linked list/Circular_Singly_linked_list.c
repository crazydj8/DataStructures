#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *next;
};
typedef struct node NODE; //giving "struct node" an alias "NODE" for easier implementation

//We keep track of the last node in circular singly linked list as it provides us with the memory address of the last node along 
//with the address of first node(stored in the next pointer)

struct list{
    NODE *tail; //for storing address of tail pointer of the linked list
};
typedef struct list LIST;


//To initialize the linked list tail pointer
void init(LIST *p) 
{
    p->tail=NULL;
}

//To make a node with given data and return its address.
NODE * getnode(int data)
{
    NODE *temp;
    temp=(NODE *)malloc(sizeof(NODE)); //Allocates memory for the node
    temp->data=data;                   //Assigns data to data variable of the node
    temp->next=NULL;                   //Makes the next pointer of that node as NULL
    return temp;                       //returns the address of that node
}

//To insert the element at the begining of the linked list
void insert_front(LIST *p,int data)
{
    NODE *newNode=getnode(data);
    if(p->tail==NULL) //if list is empty, insert as first node(as for only one node, first and last node are the same)
    {
        p->tail=newNode;
        newNode->next=p->tail; //connecting the next pointer of the node to itself as it is a circular linked list
    }
    else
    {
        newNode->next=p->tail->next;  //making the node as first node
        p->tail->next=newNode;   //pointing the last node back to the first node
    }
}

//To insert the element at the end of the linked list
void insert_rear(LIST *p,int data)
{
    NODE *newNode=getnode(data);
    if(p->tail==NULL)
    {
        p->tail=newNode;    //if list is empty, insert as first node(as for only one node, first and last node are the same)
        newNode->next=p->tail;    //connecting the next pointer of the node to itself as it is a circular linked list
    }
    else
    {
        newNode->next=p->tail->next;  //to make it as the last node, storing the address of the first node in the next address
        p->tail->next=newNode;
        p->tail=newNode;  //shifting the tail pointer to the newNode which is now the last node
    }
}

//To insert the element at a specific position in the linked list
void insert_at_position(LIST *p,int data,int pos)
{
    int count=1;
    if(pos==0)
    {
        insert_front(p,data);            //if position is 0 then insert as first node
    }
    else
    {
        NODE *newNode=getnode(data);
        NODE *cur=p->tail->next->next,*prev=p->tail->next;  //initializin the current pointer from the second node and prev from the first node
        while(cur!=p->tail->next && count!=pos)   //finding the node address where newnode is going to be added
        {
            prev=cur;
            cur=cur->next;
            count++;
        }
        if(cur==p->tail->next)                    //if the position is more than the size of the list, then add the element as last node
        {
            insert_rear(p,data);
        }
        else                             //inserting the newnode after prev pointer
        {
            newNode->next=cur;
            prev->next=newNode;
        }
    }
}

//To delete a node from the begining of the linked list
void delete_front(LIST *p)
{
    if(p->tail==NULL)       //List empty condition
    {
        printf("\n The list is empty!\n");
    }
    else if(p->tail->next==p->tail)  //If there is only one node, then the next pointer of the node will point to itself
    {
        NODE *temp=p->tail;
        p->tail=NULL;        //There wont be any node left so we point the tail pointer to NULL explicitly to avoid void pointers
        printf("\n The deleted node data is %d \n",temp->data);
        free(temp);
    }
    else
    {
        NODE *temp=p->tail->next;  //storing the address of the first node in a temporary variable
        p->tail->next=p->tail->next->next;    
        printf("\n The deleted node data is %d \n",temp->data);
        free(temp);   //freeing the memory of the first node
    }
}

//To delete a node from the end of the linked list
void delete_rear(LIST *p)
{
    
    if(p->tail==NULL)   //List empty condition
    {
        printf("\n The list is empty!\n");
    }
    else if(p->tail->next==p->tail)      //If there is only one node, then the next pointer of the node will point to itself
    {
        NODE *temp=p->tail; 
        p->tail=NULL;                    //There wont be any node left so we point the tail pointer to NULL explicitly to avoid void pointers
        printf("\n The deleted node data is %d \n",temp->data);
        free(temp);
    }
    else
    {
        NODE *cur=p->tail->next,*prev=NULL;
        while(cur!=p->tail)         //To find out the address of the second last node
        {
            prev=cur;
            cur=cur->next;
        }
        prev->next=cur->next;
        p->tail=prev;              //Shifting the tail pointer to the second last node which now becomes the last node
        printf("\n The deleted node data is %d \n",cur->data);
        free(cur);
    }
}

//To delete a node with a particulat data from the linked list
void delete_node(LIST *p,int data)
{
    if(p->tail==NULL)    //List empty condition
    {
        printf("\n The list is empty!\n ");
    }
    else
    {
        NODE *cur=p->tail->next,*prev=NULL;        //Address of first node is stored in cur and prev is initialized to NULL
        if(cur->data!=data)         //Checking if data is present in the first node itself
        {
            prev=cur;
            cur=cur->next;
        }
        while(cur!=p->tail->next && cur->data!=data)  //Traverse to the node with the given data
        {
            prev=cur;
            cur=cur->next;
        }
        if(prev==NULL) //If the data is found in the first node itself
        {
            p->tail->next=p->tail->next->next;
            printf("\n Successfully deleted node with data %d \n ",cur->data);
            free(cur);
        }
        else if(prev!=NULL && cur==p->tail->next)  //If the data is not present in the linked list(as prev!= NULL that means while loop has already iterated over the whole linked list)
        {
            printf("\n The data %d is not found in any node. Please try again! \n",data);
        }
        else              //Data is found somewhere in the middle of the linked list
        {
            prev->next=cur->next;
            printf("\n Successfully deleted node with data %d \n",cur->data);
            free(cur); //freeing the node containing the data
        }

    }
}

//To search the position of an element in the linked list
int search(LIST *p,int ele)
{
    int count=0; //keeps track of the position of the node
    if(p->tail==NULL) 
    {
        return -1;
    }
    else
    {
        NODE *temp=p->tail->next;
        if(temp->data!=ele)        //Checking if data is present in the first node itself
        {
            temp=temp->next;
            count++;
        }
        while(temp!=p->tail->next && temp->data!=ele )  //traverse the list untill element is found or the list ends.
        {
            temp=temp->next;
            count++;
        }
        if(temp==p->tail->next && count>0) //if the element is not found in the list(count>0 indicates that the list has been searched)
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
    if(p->tail==NULL)
    {
        printf("\n The list is empty!\n ");
        return;
    }
    NODE *temp,*cur=p->tail->next;
    while(cur!=p->tail) //till the list has only the last node left
    {
        temp=cur; //temp pointer to point to a node
        cur=cur->next; //shift the cur pointer to next node
        free(temp); //free the node whose address is stored in temp
    }
    free(cur);  //freeing the last node
    p->tail=NULL;    //Storing NULL in tail pointer to avoid void/dangling pointers
    printf("\n The list has been destroyed! \n");
}

//To print the elements of the linked list
void display(LIST *p)
{
    if(p->tail==NULL)    //List empty condition
    {
        printf("\n List is Empty\n");
    }
    else
    {
        NODE *temp=p->tail->next;     //To start the iteration from the first node
        printf("\n %d",temp->data);   //Printing the data of the first node
        temp=temp->next; 
        while(temp!=p->tail->next) //traverses all the nodes of the linked list. 
        {
            printf("\n %d",temp->data); //prints the data of the nodes
            temp=temp->next;
        }
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
            case 6:printf("\n Enter the element to be deleted ");
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
            case 10:break;
            default:printf("\n Invalid choice. Please try again! \n");
                    break;
        }
    }while(choice!=10);
}