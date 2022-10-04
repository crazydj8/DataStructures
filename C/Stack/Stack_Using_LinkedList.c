#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
    int data;
    struct node *link;
}NODE;

typedef struct head
{
    NODE *head;
}HEAD;

void init(HEAD *p)
{
    p->head=NULL;
}

NODE * getnode(int ele)
{
    NODE *newnode;
    newnode=(NODE *)malloc(sizeof(NODE));
    newnode->data=ele;
    newnode->link=NULL;
    return newnode;
}

void push(HEAD *p,int ele)
{
    NODE *temp;
    temp=getnode(ele);
    if(p->head==NULL)
    {
        p->head=temp;
    }
    else
    {
        temp->link=p->head;
        p->head=temp;
    }
}

void display(HEAD *p)
{
    if(p->head==NULL)
    {
        printf("\n Stack is empty");
    }
    else
    {
        NODE *temp;
        temp=p->head;
        while(temp!=NULL)
        {
            printf("\n %d",temp->data);
            temp=temp->link;
        }
    }
}

int pop(HEAD *p)
{
    if(p->head==NULL)
    {
        return -11111;
    }
    else
    {
        NODE *temp;
        temp=p->head;
        int x;
        x=p->head->data;
        p->head=p->head->link;
        free(temp);
        return x;
    }
}

void peep(HEAD p)
{
    if(p.head==NULL)
    {
        printf("\n Stack is Empty");
    }
    else
    {
        printf("\n The top element is = %d",(p.head)->data);
    }
}

void main()
{
    HEAD h1;
    int x;
    init(&h1);
    push(&h1,10);
    push(&h1,20);
    push(&h1,30);
    display(&h1);
    x=pop(&h1);
    if(x==-11111)
    {
        printf("\n Stack is empty");
    }
    else
    {
        printf("\n The deleted element is= %d",x);
    }

    display(&h1);
    peep(h1);
}