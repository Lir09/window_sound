# sound control program

## Project Overview 
**The Sound Control Program** lets you control the sound of Windows running on your Windows operating system. 
This app has a GUI built with PySide6.

### Key Features
- Automatically imports the active window list.
- You can control the sound of the selected window. 
- Intuitive and user-friendly interface.

---

## Installation Guide

### preconditions
1. Python 3.8 and later
2. 'pip' Package Manager

### Install Dependencies
Run the following command to install the required package:

pip 설치 pyside6 comtypes pycaw

# Build Instructions
To deploy a program as an executable:

Install the Pi installer: Run the following command to install the Pi installer:

Pipe Installation Finestaller

Create an executable. Navigate to the directory that contains the script and run the following command:

Pyinstaller -- no console main.py

--One file: Packages the program into one executable file.
--No console: Hides the console window when running the application.
Locate the executable: The executable is created in the dist folder within the project directory.

Distribution: Share the executable in the Deployment folder. Verify that the target computer meets the program's requirements.

# Instructions for Use

1. Run the program (double-click the executable or run a Python script).
2. From the Select Window drop-down menu, select the window you want to resize.
3. It adjusts the sound. It also has a mute function to completely reduce the sound. 

# Licenses
The project is licensed under the MIT License. The code can be used, modified and distributed free of charge if the original author is given appropriate credit.

# Reference and Resources

PySide6: https://pyside.org/

Pycaw: https://pypi.org/project/pycaw/

Comtypes: https://pypi.org/project/comtypes/

# FAQ
1. The program is not working. What should I do?
Verify that Python and the required dependencies are installed correctly.
Try running the program with administrator privileges.
2. The drop-down does not display the window you want.
After starting the program, when the target window opens, restart the program to refresh the window list.
For additional questions, please contact gbin8498@gmail.com .
