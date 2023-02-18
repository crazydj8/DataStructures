#include<stdio.h>
#include<stdlib.h>
#define maxnodes 100        //Hardcoding the maximum size of the queue to be 100. Can be changed by the user.

typedef struct queue         //creating a struture stack for storing the stack data
{
    int front;              //stores the position of the front of the queue
    int rear;               //stores the position of the rear of the queue
    int items[maxnodes];    //actual queue where elements are stored
}QUEUE;

void init(QUEUE *q1)        //initializing the front and top variables of the queue to 0
{
    q1->front=-1;
    q1->rear=-1;
}

void enqueue(QUEUE *p,int ele)      //enqueue function to add data to the queue
{
    if(p->rear==maxnodes-1)         //checks if queue is full 
    {
        printf("\n Queue Full! \n");
    }
    else                            //adding data to the queue
    {
        if(p->front==-1)            //if the queue is empty then add the data to the first position and make front and rear both equal to 0
        {
            (p->front)=0;
            (p->rear)=0;
            p->items[p->rear]=ele;
        }
        else                        //if queue is not empty then add data to the next position and only increment the rear pointer(as queue is FIFO)
        {
            (p->rear)++;            //first incrementing the rear pointer then adding the elment there. Can also be written as p->items[++(p->rear)]=ele;
            p->items[p->rear]=ele;
            //p->items[++(p->rear)]=ele;       //using pre-increment
        }
    }
}


int peek(QUEUE *p)              //to see which is the next element in the queue
{
    int x;
    if(p->front==-1)            //if the queue is empty
    {
        return -99999;
    }
    else                        //if the queue is not empty
    {
        x=p->items[p->front];   //taking the data at front position of the queue 
        return x;               //returning the data
    }
}

void display(QUEUE *p)                  //to print the data in the queue in order
{
    if(p->front==-1)                    //if queue is empty
    {
        printf("\n Queue is empty!\n");
    }
    else                                //if queue is not empty
    {
        int x;
        x=p->front;                     //taking the first position index in variable x
        for(int i=x;i<=p->rear;i++)     //running the loop from front of the queue till the rear of the queue
        {
            printf("\n %d",p->items[i]);
        }
    }
    printf("\n");
}

int dequeue(QUEUE *p)                   //dequeue function to remove data to the queue
{
    if(p->front==-1)                    //if queue is empty
    {
        return -99999;
    }
    else
    {
        int x;
        if(p->front==p->rear)          //if only one element is in the queue
        {
            x=p->items[p->front];     
            p->front=-1;               //resets the front and rear pointer variable. The queue is reset
            p->rear=-1;
        }
        else                            //if more than one element in the queue
        {
            x=p->items[p->front];
            (p->front)++;              //increases the front pointer value. The data is not removed from the array, only the first pointer value is incremented
        }
        return x;
    }
}

void main()
{
    int x,choice,data;
    QUEUE q1;
    init(&q1);
    do
    {
        printf("\n Enter 1.Enqueue 2.Dequeue 3.Peek 4.Display 5.Exit : ");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1: printf("\n Enter element to be enqueued: ");
                    scanf("%d",&data);
                    enqueue(&q1,data);
                    break;
            case 2: x=dequeue(&q1);
                    if(x==-99999)
                    {
                        printf("\n Queue is empty!\n");
                    }
                    else
                    {
                        printf("\n The dequeued element is: %d\n",x);
                    }
                    break;
            case 3: x=peek(&q1);
                    if(x==-99999)
                    {
                        printf("\n Queue is empty!\n");
                    }
                    else
                    {
                        printf("\n The nextcelement in queue is: %d\n",x);
                    }
                    break;
            case 4: display(&q1);
                    break;
            case 5: printf("\n THANK YOU. EXITING.. \n");
                    break;
            default:printf("\n Invalid choice. Please try again! \n");
                    break;
        }
    } while(choice!=5);
}