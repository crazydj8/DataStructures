#include<stdio.h>
#include<stdlib.h>

//in implementation of stack using linked list, there is not limit on the size of the stack as we use dynamic memory allocation.
//similar to singly linked list program
//we will use insert front and delete front to mimic stack functions using a singly linked list


typedef struct node
{
    int data;
    struct node *link;
}NODE;                      //giving "struct node" an alias "NODE" for easier implementation

typedef struct stack
{
    NODE *head;
}STK;

void init(STK *p)           //to initialize the stack head pointer to NULL. Stack empty.
{
    p->head=NULL;
}

NODE * getnode(int ele)                         //To make a node with given stack element and return its address.
{
    NODE *NewNode;
    NewNode=(NODE *)malloc(sizeof(NODE));       //Allocates memory for the node
    NewNode->data=ele;                          //Assigns data to data variable of the node
    NewNode->link=NULL;                         //Makes the link pointer of that node as NULL
    return NewNode;                             //returns the address of that node
}

//pushing is easier using insert front in stack as we dont have to traverse the list again and again to go to end of the list
void push(STK *p,int ele)       //push operation to push an element on the top of stack
{
    NODE *temp;
    temp=getnode(ele);          //getting a node with data as element given by the user
    if(p->head==NULL)           //stack empty condition
    {
        p->head=temp;           //as stack is empty, inserting it as the first element
    }
    else                        //insert front 
    {
        temp->link=p->head;     //pointing the newnode's link to head pointer
        p->head=temp;           //changing the head pointer to new address of temp
    }
}

//popping is easier using delete front in stack as we dont have to traverse the list again and again to go to end of the list and keep track of previous pointer
int pop(STK *p)
{
    if(p->head==NULL)           //stack empty condition
    {
        return -1;
    }
    else
    {
        int x;
        NODE *temp;
        temp=p->head;           //storing first element's address in temporary variable
        x=p->head->data;        //storing element in top of the stack in the variable x
        p->head=p->head->link;  //shifting head pointer to the next node. Similar to reducing index value in array implementation of stack. However,in this the element will be removed from the memory
        free(temp);             //freeing the memory allocated to first node(element at top of the stack)
        return x;               //returning the element at top of the stack
    }
}

void peep(STK p)                //peep operation to see the element at top of the stack without changing it
{
    if(p.head==NULL)            //stack empty condition. As we are using call by value, we use '.' operator to access the address of top of the stack
    {
        printf("\n Stack is empty!\n");
    }
    else
    {
        printf("\n The top element is = %d",(p.head)->data);        //p.head is an address of structure NODE, so to access its data we use '->'
    }
}

void display(STK *p)            //display all the elements in the stack
{   
    if(p->head==NULL)           //stack empty condition
    {
        printf("\n Stack is empty!\n");
    }
    else
    {
        NODE *temp;
        temp=p->head;            
        while(temp!=NULL)         //traverses all the nodes of the linked list. If temp->next!=NULL is used then element in the last node won't be printed
        {
            printf("\n %d",temp->data);
            temp=temp->link;
        }
    }
}

void main()
{
    int choice,data;
    STK s1;
    init(&s1);
    do{
        printf("\n 1.Push 2.Pop 3.Peep 4.Display 5.Exit: ");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:printf("\n Enter element to be pushed onto the stack: ");
                   scanf("%d",&data);
                   push(&s1,data);
                   break;
            case 2:data=pop(&s1);
                   if(data==-1)
                   {
                       printf("\n Stack is empty!\n");
                   }
                   else
                   {
                       printf("\n The popped element is= %d\n",data);
                   }
                   break;
            case 3:peep(s1);
                   break;
            case 4:display(&s1);
                   break;
            case 5:printf("\n THANK YOU. EXITING..\n");
                   break;

            default:printf("\n Invalid choice. Please try again! \n");
                    break;

        }      
    }while(choice!=5);
}