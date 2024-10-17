
<img align="right" src="python_logo/python-logo@2x.png">


${\huge{\textsf{\textcolor{#0A1589}{Tired of creating virtual environments and installing dependencies?}}}}$

I created this project generator script to automate the setting up a of new Python project.



${\large{\textsf{\textcolor{#0A1589}{How to use it?}}}}$

Just copy the script `python_setup.py` and run it. 

You will be prompted to name your project and app. That's it.


${\large{\textsf{\textcolor{#0A1589}{What does it do?}}}}$

It creates the virtual environment in the parent folder, project structure and files for your project.

It upgrades pip to the latest version and installs any dependencies you need.


${\large{\textit{\textcolor{#0A1589}{I have my own way of structuring the folders I need... Can I customize it?}}}}$

Yes. You'll find a tuple named ${\textbf{\textsf{\textcolor{ProcessBlue}{'project\\_folders'}}}}$. A single string inside this tuple represents a folder to be created.

A tuple of strings means a folder, its subfolder, so on and so forth.

There is also a ${\textbf{\textsf{\textcolor{ProcessBlue}{'dependencies'}}}}$ list. This is where you instruct it to install any libraries.


${\large{\textsf{\textcolor{#0A1589}{Did you know?}}}}$

Nowhere in the script is the virtual environment activated.

One does not need to activate it to install packages or libraries.
