import java.util.*;

class Node {
    int data;
    Node prev;
    Node next;
    Node(int d) {
        data = d;
        prev = null;
        next = null;
    }
}

public class DoublyLinkedList {
    Node head;
    DoublyLinkedList() {
        head = null;
    }
    
    // Function to insert a node at the front of the doubly linked list
    void insertFront(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        if(head != null) {
            head.prev = newNode;
        }
        head = newNode;
    }
    
    // Function to insert a node at the rear of the doubly linked list
    void insertRear(int data) {
        Node newNode = new Node(data);
        Node current = head;
        if(current == null) {
            head = newNode;
        } else {
            while(current.next != null) {
                current = current.next;
            }
            current.next = newNode;
            newNode.prev = current;
        }
    }
    
    // Function to insert a node at a given position in the doubly linked list
    void insertAtPos(int data, int pos) {
        Node newNode = new Node(data);
        if(pos == 1) {
            newNode.next = head;
            if(head != null) {
                head.prev = newNode;
            }
            head = newNode;
        } else {
            Node current = head;
            for(int i = 1; i < pos - 1 && current != null; i++) {
                current = current.next;
            }
            if(current != null) {
                newNode.next = current.next;
                current.next = newNode;
                newNode.prev = current;
                if(newNode.next != null) {
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
            head = head.next;
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
            while(current.next != null) {
                current = current.next;
            }
            if(current.prev != null) {
                current.prev.next = null;
            } else {
                head = null;
            }
        }
    }
    
    // Function to print the doubly linked list
    void printList() {
        Node current = head;
        while(current != null) {
            System.out.print(current.data + " ");
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
