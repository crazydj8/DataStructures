#include<stdio.h>
#include<stdlib.h>
#define MAX 100               //Hardcoding the maximum size of the stack to be 100. Can be changed by the user.

typedef struct stack           //creating a struture stack for storing the stack data
{
    int top;                   //top stores the index value of the top of the stack
    int items[MAX];             //stores all the items of the stack
}STK;

void init(STK *p)               //initializing stack top to -1
{
    p->top=-1;
}

//stack is a data structure that works on Last In First Out(LIFO) principle.

void push(STK *p,int ele)      //push operation to push an element on the top of stack
{
    if(p->top==MAX-1)          //stack full(overflow) condition
    {
        printf("\n Stack full!\n");
    }
    else
    {
        (p->top)++;                //increasing the index of top of the stack if stack is not full
        p->items[p->top]=ele;      //placing element at the new stack top
    }
}

int pop(STK *p)                //pop operation to remove an element from the top of stack
{
    if(p->top==-1)
    {
        return -1;             //if stack if empty 
    }
    else
    {
       int x;
       x=p->items[p->top];      //taking element from the top of the stack
       (p->top)--;              //reducing the index of top of the stack. It does not delete the element from the array but makes it not accessible.  
       return x;                //returning the pop element
    }
}

void peep(STK p)                //peep operation to see the element at top of the stack
{
    if(p.top==-1)               //as we are using call by value, we use '.' operator to access the elements
    {
        printf("\n Stack is empty!\n");        //stack empty condition
    }
    else
    {
       printf("\n The top element is = %d\n",p.items[p.top]);
    }
}

void display(STK *p)            //display all the elements in the stack. We can also use call by value as it is not changing any data in stack
{
    if(p->top==-1)              //stack empty condition
    {
        printf("\n Stack is empty!\n");
    }
    else
    {
        int x=p->top;                    
        for(int i=x;i>=0;i--)           //displaying the most recent item first
        {
            printf("\n %d",p->items[i]);
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