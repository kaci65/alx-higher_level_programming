## **0x13-javascript_objects_scopes_closures**

### **Resouces**

    JavaScript object basics
    Object-oriented JavaScript (read all examples!)
    Class - ES6
    super - ES6
    extends - ES6
    Object prototypes
    Inheritance in JavaScript
    Closures
    this/self
    Modern JS

### **Learning Outcome**

    How to create an object in Javascript
    What this means
    What undefined means
    Why the variable type and scope is important
    What is a closure
    What is a prototype
    How to inherit an object from another

### **Tasks**
### **0-rectangle.js**
Empty class Rectangle that defines a rectangle:

    You must use the class notation for defining your class

### **1-rectangle.js**
Class Rectangle that defines a rectangle:

    You must use the class notation for defining your class
    The constructor must take 2 arguments w and h
    Initialize the instance attribute width with the value of w
    Initialize the instance attribute height with the value of h

### **2-rectangle.js**
Class Rectangle that defines a rectangle:

    You must use the class notation for defining your class
    The constructor must take 2 arguments w and h
    Initialize the instance attribute width with the value of w
    Initialize the instance attribute height with the value of h
    If w or h is equal to 0 or not a positive integer, create an empty object

### **3-rectangle.js**
Class Rectangle that defines a rectangle:

    You must use the class notation for defining your class
    The constructor must take 2 arguments: w and h
    Initialize the instance attribute width with the value of w
    Initialize the instance attribute height with the value of h
    If w or h is equal to 0 or not a positive integer, create an empty object
    Create an instance method called print() that prints the rectangle using the character X

### **4-rectangle.js**
Class Rectangle that defines a rectangle:

    You must use the class notation for defining your class
    The constructor must take 2 arguments: w and h
    Initialize the instance attribute width with the value of w
    Initialize the instance attribute height with the value of h
    If w or h is equal to 0 or not a positive integer, create an empty object
    Create an instance method called print() that prints the rectangle using the character X
    Create an instance method called rotate() that exchanges the width and the height of the rectangle
    Create an instance method called double() that multiples the width and the height of the rectangle by 2

### **5-square.js**
class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

    You must use the class notation for defining your class and extends
    The constructor must take 1 argument: size
    The constructor of Rectangle must be called (by using super())

### **6-square.js**
Class Square that defines a square and inherits from Square of 5-square.js:

    You must use the class notation for defining your class and extends
    Create an instance method called charPrint(c) that prints the rectangle using the character c
        If c is undefined, use the character X

### **7-occurrences.js**
Function that returns the number of occurrences in a list:

    Prototype: exports.nbOccurences = function (list, searchElement)

### **8-esrever.js**
Function that returns the reversed version of a list:

    Prototype: exports.esrever = function (list)
    You are not allow to use the built-in method reverse

### **9-logme.js**
Function that prints the number of arguments already printed and the new argument value. (see example below)

    Prototype: exports.logMe = function (item)
    Output format: <number arguments already printed>: <current argument value>

### **10-converter.js**
Function that converts a number from base 10 to another base passed as argument:

    Prototype: exports.converter = function (base)
    You are not allowed to import any file
    You are not allowed to declare any new variable (var, let, etc..)
