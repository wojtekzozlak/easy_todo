easy-todo
=========

A simple, command-line oriented TODO list manager in very early stage
of development.


Installation
-------------

    pyton setup.py install
        
Note: It may require root privileges.


How to use?
-----------

Few examples

* Adding an item:

        easy-todo -at "My new item" -p 5


* Displaying items:

        easy-todo -q


* Updating items:

        easy-todo -u 1 -t "My new description" -p 0

* Removing items:

        easy-todo -r 1


Try "easy-todo --help" for more options.
