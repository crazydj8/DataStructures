package Java.Queue;

import java.util.*;

class Queue {
    int front, rear, size;
    int capacity;
    int[] array;

    public Queue(int capacity) {
        this.capacity = capacity;
        this.front = this.size = 0;
        this.rear = capacity - 1;
        this.array = new int[this.capacity];
    }

    public boolean isFull(Queue queue) {
        return (queue.size == queue.capacity);
    }

    public boolean isEmpty(Queue queue) {
        return (queue.size == 0);
    }

    public void enqueue(int item) {
        if (isFull(this))
            return;
        this.rear = (this.rear + 1) % this.capacity;
        this.array[this.rear] = item;
        this.size++;
    }

    public int dequeue() {
        if (isEmpty(this))
            return Integer.MIN_VALUE;
        int item = this.array[this.front];
        this.front = (this.front + 1) % this.capacity;
        this.size--;
        return item;
    }

    public int peek() {
        if (isEmpty(this))
            return Integer.MIN_VALUE;
        return this.array[this.front];
    }

    public void display() {
        System.out.print("Queue: ");
        for (int i = this.front; i <= this.rear; i++) {
            System.out.print(this.array[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the maximum size of the Queue:");
        int maxSize = sc.nextInt();

        Queue q=new Queue(maxSize);

        while (true) {
            System.out.println("Enter the operation you want to perform:");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Peek");
            System.out.println("4. Display");
            System.out.println("5. Exit");

            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Enter the element to enqueue:");
                    int element = sc.nextInt();
                    q.enqueue(element);
                    break;
                case 2:
                    int poppedElement = q.dequeue();
                    if (poppedElement != -1) {
                        System.out.println("Dequeued Element: " + poppedElement);
                    }
                    break;
                case 3:
                    int peekedElement = q.peek();
                    if (peekedElement != -1) {
                        System.out.println("Peeked Element: " + peekedElement);
                    }
                    break;
                case 4:
                    q.display();
                    break;
                case 5:
                    sc.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid Choice");
            }
        }
    }
}

