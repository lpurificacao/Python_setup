
<img align="right" src="python_logo/python-logo@2x.png">

${\huge{\textsf{\textcolor{#0A1589}{This is my Python starter}}}}$

I created this project generator script to automate the setting up a of new Python project.



${\large{\textsf{\textcolor{#0A1589}{How to use it?}}}}$

Just copy the script to the directory where you want to create your Python project.

Run it from your shell or IDE. That's it.



${\large{\textsf{\textcolor{#0A1589}{What does it do?}}}}$

It creates the virtual environment, project structure, files and configuration for your project.

It upgrades pip, installs Django or any other dependencies you want and applies initial migrations to the database.



${\large{\textit{\textcolor{#0A1589}{I have my own way of structuring the folders... Can I customize it?}}}}$

Yes. Right at the beginning of the script you'll find 2 tuples: ${\textbf{\textsf{\textcolor{Process#0A1589}{'project\\_folders'}}}}$ and ${\textbf{\textsf{\textcolor{Process#0A1589}{'app\\_folders'}}}}$

A single string represents a directory to be created.

A tuple of strings means a parent directory, a child directory, so on and so forth.

There is also a ${\textbf{\textsf{\textcolor{Process#0A1589}{'dependencies'}}}}$ dictionary. This is where you instruct it to install any libraries.


${\large{\textsf{\textcolor{#0A1589}{What have I learned working on this project?}}}}$

Unknown to me before, one does not need to activate the virtual environment to install packages or libraries.

Running system commands while handling input/output errors with Python's very handy built-in module [subprocess](https://docs.python.org/3/library/subprocess.html)
