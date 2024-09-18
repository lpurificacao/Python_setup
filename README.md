
<img align="right" src="python_logo/python-logo@2x.png">

${\huge{\textsf{\textcolor{#0A1589}{Tired of creating virtual environments and installing dependencies?}}}}$

I created this project generator script to automate the setting up a of new Python project.



${\large{\textsf{\textcolor{#0A1589}{How to use it?}}}}$

Just copy the script and run it from your shell or IDE. That's it.


${\large{\textsf{\textcolor{#0A1589}{What does it do?}}}}$

Your project is created one level above the directory from where you're running the script.

It creates the virtual environment, project structure and files for your project.

It upgrades pip to the latest version and installs any dependencies you need.

You can also create whatever directory structure you want.


${\large{\textit{\textcolor{#0A1589}{I have my own way of structuring the folders... Can I customize it?}}}}$

Yes. Right at the beginning of the script you'll find a tuple: ${\textbf{\textsf{\textcolor{Process#0A1589}{'project\\_folders'}}}}$

A single string represents a directory to be created.

A tuple of strings means a parent directory, a child directory, so on and so forth.

There is also a ${\textbf{\textsf{\textcolor{Process#0A1589}{'dependencies'}}}}$ list. This is where you instruct it to install any libraries.


${\large{\textsf{\textcolor{#0A1589}{Did you know?}}}}$

Nowhere in the script is the virtual environment activated.

One does not need to activate it to install packages or libraries.



