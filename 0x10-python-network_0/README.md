## **0x10-python-network_0**

### **Resources**

    HTTP (HyperText Transfer Protocol) (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)<https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html>
    HTTP Cookies<https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies>

### **Learning Outcomes**

    What a URL is
    What HTTP is
    How to read a URL
    The scheme for a HTTP URL
    What a domain name is
    What a sub-domain is
    How to define a port number in a URL
    What a query string is
    What an HTTP request is
    What an HTTP response is
    What HTTP headers are
    What the HTTP message body is
    What an HTTP request method is
    What an HTTP response status code is
    What an HTTP Cookie is
    How to make a request with cURL
    What happens when you type google.com in your browser (Application level)

### **Tasks**
### **0-body_size.sh**
Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

    The size must be displayed in bytes
    You have to use curl

Please test your script in the container provided, using the web server running on port 5000

### **1-body.sh**
Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

    Display only body of a 200 status code response
    You have to use curl

Please test your script in the container provided, using the web server running on port 5000

### **2-delete.sh**
Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

    You have to use curl

Please test your script in the container provided, using the web server running on port 5000

### **3-methods.sh**
Bash script that takes in a URL and displays all HTTP methods the server will accept.

    You have to use curl

Please test your script in the container provided, using the web server running on port 5000

### **4-header.sh**
Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

    A header variable X-HolbertonSchool-User-Id must be sent with the value 98
    You have to use curl

Please test your script in the container provided, using the web server running on port 5000

### **5-post_params.sh**
Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

    A variable email must be sent with the value hr@holbertonschool.com
    A variable subject must be sent with the value I will always be here for PLD
    You have to use curl

Please test your script in the container provided, using the web server running on port 5000

### **6-peak.py, 6-peak.txt**
Technical interview preparation:

    You are not allowed to google anything
    Whiteboard first

Write a function that finds a peak in a list of unsorted integers.

    Prototype: def find_peak(list_of_integers):
    You are not allowed to import any module
    Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
    6-peak.py must contain the function
    6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
    Note: there may be more than one peak in the list
