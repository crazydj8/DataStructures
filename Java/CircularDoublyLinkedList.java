import java.util.*;

public class CircularDoublyLinkedList {
    
    // Node class
    class Node {
        int data;
        Node next;
        Node prev;
        
        public Node(int data) {
            this.data = data;
            this.next = null;
            this.prev = null;
        }
    }
    
    // Linked list class
    private Node head;
    private int size;
    
    public CircularDoublyLinkedList() {
        head = null;
        size = 0;
    }
    
    // Method to insert a node at the front of the list
    public void insertFront(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            head.next = head;
            head.prev = head;
        } else {
            newNode.next = head;
            newNode.prev = head.prev;
            head.prev.next = newNode;
            head.prev = newNode;
            head = newNode;
        }
        size++;
    }
    
    // Method to insert a node at the rear of the list
    public void insertRear(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            head.next = head;
            head.prev = head;
        } else {
            newNode.next = head;
            newNode.prev = head.prev;
            head.prev.next = newNode;
            head.prev = newNode;
        }
        size++;
    }
    
    // Method to insert a node at a specified position in the list
    public void insertAtPos(int data, int pos) {
        if (pos < 1 || pos > size + 1) {
            System.out.println("Invalid position!");
            return;
        }
        Node newNode = new Node(data);
        if (pos == 1) {
            insertFront(data);
            return;
        }
        if (pos == size + 1) {
            insertRear(data);
            return;
        }
        Node current = head;
        for (int i = 1; i < pos; i++) {
            current = current.next;
        }
        newNode.next = current;
        newNode.prev = current.prev;
        current.prev.next = newNode;
        current.prev = newNode;
        size++;
    }
    
    // Method to delete a node from the front of the list
    public void deleteFront() {
        if (head == null) {
            System.out.println("List is empty!");
            return;
        }
        if (size == 1) {
            head = null;
        } else {
            head.next.prev = head.prev;
            head.prev.next = head.next;
            head = head.next;
        }
        size--;
    }
    
    // Method to delete a node from the rear of the list
    public void deleteRear() {
        if (head == null) {
            System.out.println("List is empty!");
            return;
        }
        if (size == 1) {
            head = null;
        } else {
            head.prev.prev.next = head;
            head.prev = head.prev.prev;
        }
        size--;
    }
    
    // Method to display the contents of the list
    public void display() {
        if (head == null) {
            System.out.println("List is empty!");
            return;
        }
        Node current = head;
        do {
            System.out.print(current.data + " ");
            current = current.next;
        } while (current != head);
        System.out.println();
    }
    //main method
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        CircularDoublyLinkedList dll = new CircularDoublyLinkedList();
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
				dll.display();
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


