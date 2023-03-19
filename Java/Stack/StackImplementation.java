package Java.Stack;

import java.util.*;

public class StackImplementation {
    private int top;
    private int[] arr;
    private int maxSize;

    // Constructor
    public StackImplementation(int maxSize) {
        this.maxSize = maxSize;
        arr = new int[maxSize];
        top = -1;
    }

    // push method to add elements to the stack
    public void push(int element) {
        if (top == maxSize - 1) {
            System.out.println("Stack Overflow");
        } else {
            arr[++top] = element;
        }
    }

    // pop method to remove and return the top element from the stack
    public int pop() {
        if (top == -1) {
            System.out.println("Stack Underflow");
            return -1;
        } else {
            return arr[top--];
        }
    }

    // peek method to return the top element from the stack without removing it
    public int peek() {
        if (top == -1) {
            System.out.println("Stack is Empty");
            return -1;
        } else {
            return arr[top];
        }
    }

    // display method to print all the elements in the stack
    public void display() {
        if (top == -1) {
            System.out.println("Stack is Empty");
        } else {
            System.out.println("Elements in the Stack are:");
            for (int i = top; i >= 0; i--) {
                System.out.print(" "+arr[i]);
            }
            System.out.println();
        }
    }

    // main method to test the Stack implementation
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the maximum size of the Stack:");
        int maxSize = sc.nextInt();

        StackImplementation stack = new StackImplementation(maxSize);

        while (true) {
            System.out.println("Enter the operation you want to perform:");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Display");
            System.out.println("5. Exit");

            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Enter the element to push:");
                    int element = sc.nextInt();
                    stack.push(element);
                    break;
                case 2:
                    int poppedElement = stack.pop();
                    if (poppedElement != -1) {
                        System.out.println("Popped Element: " + poppedElement);
                    }
                    break;
                case 3:
                    int peekedElement = stack.peek();
                    if (peekedElement != -1) {
                        System.out.println("Peeked Element: " + peekedElement);
                    }
                    break;
                case 4:
                    stack.display();
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
