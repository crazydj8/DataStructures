# Important

**For those who are wondering why** ```if __name__ == "__main__":``` **has been used in the end before the menu in all the programs,**

The program can also work without it but it is advisable to use it as:

The program can be divided into 2 parts:
1) The class and function definitons
2) The main program script: which contains executable lines like menu

the class and function defintions are very useful as they can be imported and used directly in other programs.

### **Now what does** ```if __name__ == "__main__":``` **do?**

It makes it so that the part thats indented under it will be specifically for testing and running the script, and will not run when you import the same code to be used as a module in another program. 

### **What will happen if I do not use it?**

When you run the program by itself, it will run normally, but when you import the same code in some other program as a module, the menu script will also run in the child program, which might not be desired.

### **Conclusion?**

In the end, its an unwritten code of convention to be followed by python programmers to differentiate between a module that needs to be imported(do not include inside ```if __name__ == "__main__":```) and a script that needs to be run(include inside ```if __name__ == "__main__":```),
or for the code to work as both if necessary.
