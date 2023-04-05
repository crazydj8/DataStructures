import java.util.*;

// Node class
class Node {
    int data;
    Node left, right;

    public Node(int data) {
        this.data = data;
        left = right = null;
    }
}

// Binary Search Tree class
class BST {
    Node root;

    // Constructor
    BST() {
        root = null;
    }

    // Insert a Node
    void insert(int data) {
        root = insertRec(root, data);
    }

    // Recursive function to insert a Node
    Node insertRec(Node root, int data) {
        if (root == null) {
            root = new Node(data);
            return root;
        }

        if (data < root.data) {
            root.left = insertRec(root.left, data);
        } else if (data > root.data) {
            root.right = insertRec(root.right, data);
        }

        return root;
    }

    // Delete a Node
    void delete(int data) {
        root = deleteRec(root, data);
    }

    // Recursive function to delete a Node
    Node deleteRec(Node root, int data) {
        if (root == null) {
            return root;
        }

        if (data < root.data) {
            root.left = deleteRec(root.left, data);
        } else if (data > root.data) {
            root.right = deleteRec(root.right, data);
        } else {
            // Node with only one child or no child
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }

            // Node with two children
            root.data = minValue(root.right);

            root.right = deleteRec(root.right, root.data);
        }

        return root;
    }

    // Find minimum value in a Node
    int minValue(Node root) {
        int minv = root.data;
        while (root.left != null) {
            minv = root.left.data;
            root = root.left;
        }
        return minv;
    }

    // Inorder traversal
    void inorder() {
        inorderRec(root);
    }

    // Recursive function for inorder traversal
    void inorderRec(Node root) {
        if (root != null) {
            inorderRec(root.left);
            System.out.print(root.data + " ");
            inorderRec(root.right);
        }
    }

    // Preorder traversal
    void preorder() {
        preorderRec(root);
    }

    // Recursive function for preorder traversal
    void preorderRec(Node root) {
        if (root != null) {
            System.out.print(root.data + " ");
            preorderRec(root.left);
            preorderRec(root.right);
        }
    }

    // Postorder traversal
    void postorder() {
        postorderRec(root);
    }

    // Recursive function for postorder traversal
    void postorderRec(Node root) {
        if (root != null) {
            postorderRec(root.left);
            postorderRec(root.right);
            System.out.print(root.data + " ");
        }
    }

    // Main function
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Create a new Binary Search Tree
        BST tree = new BST();

        int c = 1;
        while (c != 0) {
            // Display menu
            System.out.println("Enter your choice:");
            System.out.println("1: insert");
            System.out.println("2: delete");
            System.out.println("4: inorder");
            System.out.println("5: preorder");
            System.out.println("6: postorder");
            System.out.println("7: Exit");
            int ch = sc.nextInt();
            switch (ch) {
                case 1: {
                    System.out.println("Enter the data to be entered");
                    int a = sc.nextInt();
                    tree.insert(a);
                    break;
                }

                case 2: {
                    System.out.println("Enter the data to be deleted");
                    int a = sc.nextInt();
                    tree.delete(a);
                    break;
                }

                case 4: {
                    tree.inorder();
                    break;
                }

                case 5: {
                    tree.preorder();
                    break;
                }
                case 6: {
                    tree.postorder();
                    break;
                }
                case 7: {
                    c = 0;
                    break;
                }
            }
            sc.close();
        }
    }
}
