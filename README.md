# Portscanner
Port Scanner created on python

## Sys library 
The sys library in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter.

## Socket library
This library allows you to work with sockets. Socket programming is a way of connecting two nodes on a network to communicate with each other.

### How does the code works
It's pretty simple: after asking which type of packages you want to work with, it will ask for the IP of the target.

![image](https://user-images.githubusercontent.com/72951047/136639321-d1d195bf-953f-4b84-98f2-cb3b548eb369.png)

This is the part of the code that go through each port to see if it is open. The UDP conection is very similar, changing only the socket package. After analizing if the port is open, the program will register it in a .txt document. 
