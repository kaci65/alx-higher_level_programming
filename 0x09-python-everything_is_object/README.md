# 0x09-python-everything_is_object
## 0-answer.txt
### What function would you use to print the type of an object?

## 1-answer.txt
### How do you get the variable identifier (which is the memory address in the CPython implementation)?

## 2-answer.txt
### In the following code, do a and b point to the same object? Answer with Yes or No

>>> a = 89
>>> b = 100

## 3-answer.txt
### In the following code, do a and b point to the same object? Answer with Yes or No

>>> a = 89
>>> b = 89

## 4-answer.txt
### In the following code, do a and b point to the same object? Answer with Yes or No

>>> a = 89
>>> b = a

## 5-answer.txt
### In the following code, do a and b point to the same object? Answer with Yes or No

>>> a = 89
>>> b = a + 1

## 6-answer.txt
### What do these 3 lines print?

>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)

## 7-answer.txt
### What do these 3 lines print?

>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)

## 8-answer.txt
### What do these 3 lines print?

>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)

## 9-answer.txt
### What do these 3 lines print?

>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)

## 10-answer.txt
### What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

## 11-answer.txt
### What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

## 12-answer.txt
### What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)

## 13-answer.txt
### What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

## 14-answer.txt
### What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

## 15-answer.txt
### What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

## 16-answer.txt
### What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

## 17-answer.txt
### What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

## 18-answer.txt
### What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

## 19-copy_list.py
### a function def copy_list(l): that returns a copy of a list.

    The input list can contain any type of objects
    Your file should be maximum 3-line long (no documentation needed)
    You are not allowed to import any module

## 20-answer.txt
### a = ()

Is a a tuple? Answer with Yes or No

## 21-answer.txt
### a = (1, 2)

Is a a tuple? Answer with Yes or No

## 22-answer.txt
### a = (1)

Is a a tuple? Answer with Yes or No

## 23-answer.txt
## a = (1, )

Is a a tuple? Answer with Yes or No

## 24-answer.txt
### What does this script print?

a = (1)
b = (1)
a is b

## 25-answer.txt
### What does this script print?

a = (1, 2)
b = (1, 2)
a is b

## 26-answer.txt
### What does this script print?

a = ()
b = ()
a is b

## 27-answer.txt
### >>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)

Will the last line of this script print 139926795932424? Answer with Yes or No

## 28-answer.txt
### Will the last line of this script print 139926795932424? Answer with Yes or No
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)

## 106-line1.txt, 106-line2.txt, 106-line3.txt, 106-line4.txt, 106-line5.txt
### Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

    How many string objects are created by the execution of the first line of the script? (106-line1.txt)
    How many string objects are created by the execution of the second line of the script (106-line2.txt)
    After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
    After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
    How many string objects are created by the execution of the last line of the script (106-line5.txt)
guillaume@ubuntu:/python3$ cat string.py 
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
guillaume@ubuntu:/python3$
