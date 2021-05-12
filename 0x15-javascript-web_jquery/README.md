## **0x15-javascript-web_jquery**

### **Resources**
Read or watch:

    What is JavaScript?<https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript>
    Selector<https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/>
    Get and set content<https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/>
    Manipulate CSS classes<https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/>
    Manipulate DOM elements<https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/>
    API<https://oscarotero.com/jquery/>
    Introduction<https://jquery-tutorial.net/ajax/introduction/>
    GET & POST request<https://jquery-tutorial.net/ajax/the-get-and-post-methods/>
    jQuery Ajax Tutorial #1 - Using AJAX & API’s<https://www.youtube.com/watch?v=fEYx8dQr_cQ>
    What went wrong? Troubleshooting JavaScript<https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong>
    jQuery<https://jquery.com/>
    jQuery API<https://api.jquery.com/>
    jQuery Ajax<https://learn.jquery.com/ajax/>

### **Learning Outcomes**
General:

    Why jQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
    How to select HTML elements in Javascript
    How to select HTML elements with jQuery
    What are differences between ID, class and tag name selectors
    How to modify an HTML element style
    How to get and update an HTML element content
    How to modify the DOM
    How to make a GET request with jQuery Ajax
    How to make a POST request with jQuery Ajax
    How to listen/bind to DOM events
    How to listen/bind to user events

### **Import jQuery
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>

### **Tasks**
#### **0-script.js**
Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):

    You must use document.querySelector to select the HTML tag
    You can’t use the jQuery API

#### **1-script.js**
Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):

    You can’t use document.querySelector to select the HTML tag
    You must use the jQuery API

#### **2-script.js**
Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:

    You can’t use document.querySelector to select the HTML tag
    You must use the jQuery API

#### **3-script.js**
Javascript script that adds the class red to the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:

    You can’t use document.querySelector to select the HTML tag
    You must use the jQuery API

#### **4-script.js**
Javascript script that toggles the class of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#toggle_header:

    The HEADER tag must always have one class: red or green, never both in the same time, never empty.
    If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
    You can’t use document.querySelector to select the HTML tag
    You must use the jQuery API

#### **5-script.js**
Javascript script that adds a LI element to a list when the user clicks on the tag DIV#add_item:

    The new element must be: <li>Item</li>
    The new element must be added to UL.my_list
    You can’t use document.querySelector to select the HTML tag
    You must use the jQuery API

#### **6-script.js**
Javascript script that updates the text of the HTML tag HEADER to “New Header!!!” when the user clicks on DIV#update_header

    You can’t use document.querySelector to select the HTML tag
    You must use the jQuery API

#### **7-script.js**
Javascript script that fetches and replaces the name of this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

    The name must be displayed in the HTML tag DIV#character
    You can’t use document.querySelector to select the HTML tag
    You must use the jQuery API

#### **8-script.js**
Javascript script that fetches and lists all movies title by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

    All movie titles must be list in the HTML tag UL#list_movies
    You can’t use document.querySelector to select the HTML tag
    You must use the jQuery API

#### **9-script.js**
Javascript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML’s tag DIV#hello.

    The translation of “hello” must be display in the HTML tag DIV#hello
    You can’t use document.querySelector to select the HTML tag
    You must use the jQuery API
    Your script must work when it is imported from the HEAD tag

#### **100-script.js**
Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):

    You must use document.querySelector to select the HTML tag
    You can’t use the jQuery API
    Note: Your script must be imported from the HEAD tag, not at the end of the HTML

#### **101-script.js**
avascript script that adds, removes and clears LI elements from a list when the user clicks:

    The new element must be: <li>Item</li>
    The new element must be added to UL.my_list
    When the user clicks on DIV#add_item: a new element is added to the list
    When the user clicks on DIV#remove_item: a last element is removed to the list
    When the user clicks on DIV#clear_list: all elements of the list are removed
    You can’t use document.querySelector to select the HTML tag
    You must use the jQuery API
    You script must be work when it imported from the HEAD tag
