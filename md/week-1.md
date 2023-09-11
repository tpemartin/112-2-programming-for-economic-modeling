# Environment setup

## Install Python

### Windows

1. Download the latest version of Python from [python.org](https://www.python.org/downloads/windows/).
2. Run the installer.
3. Check the box to add Python to your PATH.  
4. Click "Install Now".
5. Click "Close" when the installation is complete.  
6. Open a command prompt and type `python --version` to verify that Python is installed.  
7. Type `pip --version` to verify that pip is installed.  
8. Type `exit()` to exit the Python interpreter.  
9. Type `exit` to close the command prompt.  
10. You're done!

### Mac

1. Open a terminal window.
2. Type `python --version` to verify that Python is installed.
3. Type `exit()` to exit the Python interpreter.
4. Type `exit` to close the terminal window.
5. You're done!

## Install Visual Studio Code

1. Download the latest version of Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com/download).
2. Run the installer.

## Install Git

1. Download the latest version of Git from [git-scm.com](https://git-scm.com/downloads).
2. Run the installer.
3. Accept the default settings.
4. Click "Install".
5. Click "Finish".
6. You're done!

## Install the Python extension for Visual Studio Code

1. Open Visual Studio Code.
2. Click the "Extensions" icon in the left sidebar.
3. Type "Python" in the search box.
4. Click "Install" on the "Python" extension.
5. Click "Reload" to reload Visual Studio Code.
6. You're done!

## Install the GitLens extension for Visual Studio Code

1. Open Visual Studio Code.
2. Click the "Extensions" icon in the left sidebar.
3. Type "GitLens" in the search box.
4. Click "Install" on the "GitLens" extension.
5. Click "Reload" to reload Visual Studio Code.
6. You're done!

## Run py inside markdown files

1. Open Visual Studio Code.
2. Click the "Extensions" icon in the left sidebar.
3. Type "Markdown Preview Enhanced" in the search box. 
4. Click "Install" on the "Markdown Preview Enhanced" extension. 
5. Click "Reload" to reload Visual Studio Code.

## Github

### Github Desktop

1. Download the latest version of Github Desktop from [desktop.github.com](https://desktop.github.com/).
2. Run the installer.
3. Accept the default settings.
4. Click "Install".
5. Click "Finish".
6. You're done!

### Create a Github account  

1. Go to [github.com](https://github.com)
2. Click "Sign up".
3. Enter your email address.
4. Enter a username.
5. Enter a password.
6. Click "Create account".
7. Click "Verify email address".
8. Click "Send verification email".
9. Go to your email inbox.
10. Open the email from Github.
11. Click "Verify email address".
12. You're done!

# Codes 

To run codes properly in Visual Studio Code, you need to set the root of the workspace, using the **Open Folder** method. 

1. Open Visual Studio Code.
2. Click "File" in the menu bar.
3. Click "Open Folder". (**VERY IMPORTANT**)
4. Navigate to the directory that contains the code you want to run.
5. Click "Select Folder".

## Run the codes in the terminal  

1. Click ![](Toggle%20Panel.png) in the top right corner of the window.
2. Click "Terminal" in the menu bar.
3. Click "New Terminal".
4. Type `python filename.py` to run the code.  

Step 3 defines the root of the workspace. Therefore, `filename.py` in step 8 means the file sits in the root of the workspace. If the file sits in a subdirectory of the workspace, you need to type `python subdirectory/filename.py` to run the code. 

> Setting the root of the workspace is very important. It exempts you from typing the full path of the file. Also if you passed your workspace to someone else, he/she can run the code without changing the path.  
