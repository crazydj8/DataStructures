import java.util.*;

class Node {
    int data;
    Node prev;
    Node next;
    Node(int d) {
        data = d;                           //Assigns data to data variable of the node
        prev = null;                        //Makes the left link pointer of that node as NULL
        next = null;                        //Makes the right link pointer of that node as NULL
    }
}

public class DoublyLinkedList {
    Node head;
    DoublyLinkedList() {
        head = null;                        //To initialize the linked list head pointer
    }
    
    // Function to insert a node at the front of the doubly linked list
    void insertFront(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        if(head != null) {
            head.prev = newNode;
        }
        head = newNode;                     //change head pointer if list is not empty
    }
    
    // Function to insert a node at the rear of the doubly linked list
    void insertRear(int data) {
        Node newNode = new Node(data);
        Node current = head;
        if(current == null) {               //if list is empty, insert as first node
            head = newNode;
        } else {                             //if list is not empty
            while(current.next != null) {   //traverse to the end of the given list
                current = current.next;
            }
            current.next = newNode;             //make the newnode as the last node
            newNode.prev = current;             //store the address of the previous last node as the left link of the new last node
        }
    }
    
    // Function to insert a node at a given position in the doubly linked list
    void insertAtPos(int data, int pos) {
        Node newNode = new Node(data);
        if(pos == 1) {                           //if position is 1 then insert as next of first node
            newNode.next = head;
            if(head != null) {
                head.prev = newNode;
            }
            head = newNode;
        } else {
            Node current = head;
            for(int i = 1; i < pos - 1 && current != null; i++) {       //finding the node address where newnode is going to be added
                current = current.next;
            }
            if(current != null) {
                newNode.next = current.next;
                current.next = newNode;
                newNode.prev = current;
                if(newNode.next != null) {                                 //inserting the newnode at the specific position;
                    newNode.next.prev = newNode;
                }
            } else {
                System.out.println("Position out of range");
            }
        }
    }
    
    // Function to delete the node at the front of the doubly linked list
    void deleteFront() {
        if(head == null) {
            System.out.println("List is empty");
        } else {
            head = head.next;                                       //changing the head pointer to the second node
            if(head != null) {
                head.prev = null;                                   
            }
        }
    }
    
    // Function to delete the node at the rear of the doubly linked list
    void deleteRear() {
        if(head == null) {
            System.out.println("List is empty");
        } else {
            Node current = head;
            while(current.next != null) {                               //traversing till the end of the linked list
                current = current.next;
            }
            if(current.prev != null) {                                  //if the list has only one node
                current.prev.next = null;
            } else {
                head = null;
            }
        }
    }
    
    // Function to print the doubly linked list
    void printList() {
        Node current = head;
        while(current != null) {                        //traverses all the nodes of the linked list. If temp->rlink!=NULL is used then element in the last node won't be printed
            System.out.print(current.data + " ");        //prints the data of the nodes
            current = current.next;
        }
        System.out.println();
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        DoublyLinkedList dll = new DoublyLinkedList();
        int c=1;
		while(c!=0)
		{
		System.out.println("Enter your choice:");
		System.out.println("1: insert at rear");
		System.out.println("2: insert at front");
		System.out.println("3: insert at position");
		System.out.println("4: delete from first");
		System.out.println("5: delete from rear");
		System.out.println("7: Display");
		System.out.println("8: Exit");
		int ch=sc.nextInt();
		switch(ch)
		{
			case 1:
			{
				System.out.println("Enter the data to be entered");
				int a=sc.nextInt();
				dll.insertRear(a);
				break;
			}

			case 2:
			{
				System.out.println("Enter the data to be entered");
				int a=sc.nextInt();
				dll.insertFront(a);
				break;
			}

			case 3:
			{
				System.out.println("Enter the data to be entered");
				int a=sc.nextInt();
				System.out.println("Enter the position");
				int pos=sc.nextInt();
				dll.insertAtPos(a,pos);
				break;
			}

			case 4:
			{
				dll.deleteFront();
				break;
			}

			case 5:
			{
				dll.deleteRear();
				break;
			}
			case 7:
			{
				dll.printList();
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
