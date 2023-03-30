package Java.Queue;

import java.util.*;

class Queue {
    int front, rear, size;
    int capacity;
    int[] array;

    public Queue(int capacity) {
        this.capacity = capacity;                           //Hardcoding the maximum size of the queue.
        this.front = this.size = 0;                         //stores the position of the front and size of the queue
        this.rear = capacity - 1;                           //stores the position of the rear of the queue
        this.array = new int[this.capacity];                //actual queue where elements are stored
    }

    public boolean isFull(Queue queue) {                     //checks if queue is full 
        return (queue.size == queue.capacity);
    }

    public boolean isEmpty(Queue queue) {                   //checks if queue is empty
        return (queue.size == 0);
    }

    public void enqueue(int item) {
        if (isFull(this))                                    //checks if queue is full 
            return;
        this.rear = (this.rear + 1) % this.capacity;         //first changing the rear pointer then adding the elment there.
        this.array[this.rear] = item;                       //adding data to the queue
        this.size++;                                        //incrementing size
    }

    public int dequeue() {
        if (isEmpty(this))                                  //if queue is empty
            return Integer.MIN_VALUE;
        int item = this.array[this.front];                  //adding first data toa variable
        this.front = (this.front + 1) % this.capacity;      //changing the front pointer value. The data is not removed from the array, only the first pointer value is incremented
        this.size--;                                        //decrementing size
        return item;
    }

    public int peek() {                                      //to see which is the next element in the queue
        if (isEmpty(this))                                  //if the queue is empty
            return Integer.MIN_VALUE;
        return this.array[this.front];                      //returning the data at front position of the queue 
    }

    public void display() {                                  //to print the data in the queue in order
        System.out.print("Queue: ");
        for (int i = this.front; i <= this.rear; i++) {      //running the loop from front of the queue till the rear of the queue
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

