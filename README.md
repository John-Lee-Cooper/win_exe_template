# win-exe-template

This template is a starting point for writing a windows executable with python.
The executable is created using pyinstaller.  The user interface is provided by click.
It comes with a simple exmplae script that searches for all files in a directory that matches a regular expression.

## Installation

* Clone this repo on a Windows machine.
* Double click the **setup.bat** file to build the python virtual environment and install the required libraries.
* Double click the **build.bat** file to build the executable.  (Note: run build.bat in console to see any errors.)

## How do I use?

* Drag a folder containing files onto executable icon.  (Note: the script will run **slowly** the first time).
* Enter the regular expression for the files you want to find in the folder.
* The converter will write the matching file into a file names search_<datetime>.txt.

## Developed by

Lee Cooper  
lee.cooper@aciwebs.com

