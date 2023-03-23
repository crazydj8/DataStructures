import java.util.*;

public class Singly_LinkedList {
	
	Node head; 
	static class Node {
	
		int data;
		Node next;
	
		// Constructor
		Node(int d)
		{
			data = d;			//Assigns data to data variable of the node
			next = null;		//Makes the next pointer of that node as NULL
		}
	}
	
	//To insert the element at the end of the linked list
	public static Singly_LinkedList insert(Singly_LinkedList list, int data)
	{
		Node new_node = new Node(data);
		
	
		if (list.head == null) {				//if list is empty, insert as first node
			list.head = new_node;
		}
		else {
			Node cur = list.head;
			while (cur.next != null) {			//traverse to the last node
				cur = cur.next;
			}
	
			cur.next = new_node;				//insert newnode as last node
		}
	
		return list;
	}

	//To insert the element at the begining of the linked list
	public static Singly_LinkedList insertf(Singly_LinkedList list, int data)
	{
		Node new_node = new Node(data);
		
	
		if (list.head == null) {				//if list is empty, insert as first node
			list.head = new_node;
		}
		else {
			new_node.next=list.head;			//change head pointer if list is not empty
			list.head=new_node;
		}
	
		return list;
	}
	
	//To insert the element at a specific position in the linked list
	public static Singly_LinkedList insertp(Singly_LinkedList list, int data,int pos)
	{
		Node new_node = new Node(data);
		
	
		if (list.head == null) {				//if list is empty, insert as first node
			list.head = new_node;
		}
		else {
			Node cur=list.head,pre=list.head;
			for(int i=0;i<pos;i++)				//finding the node address where newnode is going to be added
			{
				pre=cur;
				cur=cur.next;
			}
			pre.next=new_node;					//inserting the newnode after prev pointer
			new_node.next=cur;
		}
	
		return list;
	}

	//To delete a node from the begining of the linked list
	public static Singly_LinkedList deletef(Singly_LinkedList list)
	{
	
		if (list.head == null) {
			System.out.println("LIST IS EMPTY");
		}
		else {
			list.head=list.head.next;					//changing the head pointer to the second node
		}
	
		return list;
	}

	//To delete a node from the end of the linked list
	public static Singly_LinkedList deleter(Singly_LinkedList list)
	{

		if (list.head == null) {
			System.out.println("EMPTY LIST");
		}
		else if(list.head.next==null)						//if the list has only one node
		{
			list.head=null;
		}
		else {
			Node cur=list.head,pre=list.head;
			while (cur.next != null) {						//traversing till the end of the linked list
				pre=cur;
				cur = cur.next;
			}
			pre.next=null;										//change the second last node's next address to NULL
		}
	
		return list;
	}

	//To delete a node from a particulat position from the linked list
	public static Singly_LinkedList deletepos(Singly_LinkedList list,int position)
    {
        // If linked list is empty
        if (list.head == null)
            System.out.println("EMPTY LIST");
 
        Node temp = list.head;
 
        if (position == 0)						//if pos is 0
        {
            list.head = temp.next;   
        }
 
        for (int i=0; temp!=null && i<position-1; i++)
            temp = temp.next;
 
        if (temp == null || temp.next == null)
            return list;
 
        Node next = temp.next.next;
 
        temp.next = next;  
	return list;
    }

	//To print the elements of the linked list
	public static void printList(Singly_LinkedList list)
	{
		Node currNode = list.head;
	
		System.out.print("LinkedList: ");
	
		while (currNode != null) {					//traverses all the nodes of the linked list. If temp->next!=NULL is used then element in the last node won't be printed
			
			System.out.print(currNode.data + " ");		//prints the data of the nodes

			
			currNode = currNode.next;
		}
		System.out.println();
	}

	//Menu based operation
	public static void main(String[] args)
	{
		Scanner sc= new Scanner(System.in);
		Singly_LinkedList list = new Singly_LinkedList();
		int c=1;
		while(c!=0)
		{
		System.out.println("Enter your choice:");
		System.out.println("1: insert at rear");
		System.out.println("2: insert at front");
		System.out.println("3: insert at position");
		System.out.println("4: delete from first");
		System.out.println("5: delete from rear");
		System.out.println("6: delete from position");
		System.out.println("7: Display");
		System.out.println("8: Exit");
		int ch=sc.nextInt();
		switch(ch)
		{
			case 1:
			{
				System.out.println("Enter the data to be entered");
				int a=sc.nextInt();
				list=insert(list,a);
				break;
			}

			case 2:
			{
				System.out.println("Enter the data to be entered");
				int a=sc.nextInt();
				list=insertf(list,a);
				break;
			}

			case 3:
			{
				System.out.println("Enter the data to be entered");
				int a=sc.nextInt();
				System.out.println("Enter the position");
				int pos=sc.nextInt();
				list=insertp(list,a,pos);
				break;
			}

			case 4:
			{
				list=deletef(list);
				break;
			}

			case 5:
			{
				list=deleter(list);
				break;
			}

			case 6:
			{
				System.out.println("Enter the position to be deleted");
				int pos=sc.nextInt();
				list=deletepos(list,pos);
				break;
			}

			case 7:
			{
				printList(list);
				break;
			}
			case 8:
			{
				c=0;
				break;
			}
		}
	}
		sc.close();
	
	}
}
