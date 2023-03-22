#include<stdio.h>

#define treesize 7
int a[treesize];

void insert_tree(int ele)
{
    int p=0;
    if(a[p]==-1)
    {
        a[p]=ele;
    }
    else
    {
        while(a[p]!=-1 && p<treesize)
        {
            if(a[p]>ele)
            {
                p=p*2+1;
            }
            else
            {
                p=p*2+2;
            }
        }
        if(p>=treesize)
        {
            printf("Incease the size of tree");
        }
        else
        {
            a[p]=ele;
        }
    }
}

void display()
{
    for(int i=0;i<treesize;i++)
    {
        printf("\n Position = %d and Element= %d",i,a[i]);
    }
}

void inorder(int p)
{
    if(a[p]!=-1 && p<treesize)
    {
        inorder(p*2+1);
        printf("\n %d",a[p]);
        inorder(p*2+2);
    }
}

void preorder(int p)
{
    if(a[p]!=-1 && p<treesize)
    {
        printf("\n %d",a[p]);
        preorder(p*2+1);
        preorder(p*2+2);
    }
}

void postorder(int p)
{
    if(a[p]!=-1 && p<treesize)
    {
        postorder(p*2+1);
        postorder(p*2+2);
        printf("\n %d",a[p]);
    }
}

int main()
{
    for(int i=0;i<treesize;i++)
    {
        a[i]=-1;
    }
    insert_tree(100);
    insert_tree(120);
    insert_tree(25);
    insert_tree(50);
    display();
    printf("\n In inorder: ");
    inorder(0);
    printf("\n In preorder: ");
    preorder(0);
    printf("\n In postorder: ");
    postorder(0);

}