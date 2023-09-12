# 1. Environment setup

A developer environment involves with the following setups:

  * Integrated Development Environment (IDE),  
  * Programming language,  
  * Version control system

## 1.1 Integrated Development Environment (IDE)

For the course we will use [Visual Studio Code](https://code.visualstudio.com/). It is a free and open-source IDE developed by Microsoft. It is available for Windows, Mac and Linux. 

### Install Visual Studio Code

1. Download the latest version of Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com/download).
2. Run the installer.

## 1.2 Programming language     

For the course we will use [Python](https://www.python.org/). It is a free and open-source programming language. It is available for Windows, Mac and Linux.


### Install Python

#### a. Windows

1. Download the latest version of Python from [python.org](https://www.python.org/downloads/windows/).
2. Run the installer.
3. Check the box to add Python to your PATH.  
4. Click "Install Now".
5. Click "Close" when the installation is complete.  

9. Type `exit` to close the command prompt.  
10. You're done!

#### b. Mac

1. Download the latest version of Python from [python.org](https://www.python.org/downloads/macos/).   
2. Run the installer.  
3. Click "Continue".  
4. Click "Install".  
5. Enter your password.  
6. Click "Install Software".  
7. Click "Close".  

***

Once you have installed Python, you can verify that it is installed by following these steps:

 1. Launch your Visual Studio Code.  
 2. Click ![](Toggle%20Panel.png) on the top right corner of the window.  
 3. Click "Terminal" in the menu bar.
 4. Type `python --version` to verify that Python is installed.
 5. Type `exit()` to exit the Python interpreter. 

You also want to check if `pip` (which is a package manager for Python) is installed. To do so, type `pip --version` in the terminal as in step 4. If it is installed, you will see the version number. If not, you will see an error message.


## 1.3 Version control system  

### a. What is version control system?  

Version control system is a system that records changes to a file or set of files over time so that you can recall specific versions later. It allows you to revert files or the entire project back to a previous state, compare changes over time, see who last modified something that might be causing a problem, who introduced an issue and when, and more.

> You need to setup which folder should be under version control. The folder chosen will be called a **repository**.


For the course we will use [Git](https://git-scm.com/). It is a free and open-source version control system. It is available for Windows, Mac and Linux.  

### b. Install Git

1. Download the latest version of Git from [git-scm.com](https://git-scm.com/downloads).
2. Run the installer.
3. Accept the default settings.
4. Click "Install".
5. Click "Finish".
6. You're done!

### c. Github.com account

Github is a website that hosts Git repositories. It is a cloud-based service that lets you manage Git repositories. It is free for public repositories. You can create a Github account at [github.com](https://github.com).

Github provides an app called [Github Desktop](https://desktop.github.com/) that allows you to manage your repositories on Github. You can download the latest version of Github Desktop from [desktop.github.com](https://desktop.github.com/).

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

## Run codes in the terminal  

1. Click ![](Toggle%20Panel.png) in the top right corner of the window.
2. Click "Terminal" in the menu bar.
3. Click "New Terminal".
4. Type `python filename.py` to run the code.  

Step 3 defines the root of the workspace. Therefore, `filename.py` in step 8 means the file sits in the root of the workspace. If the file sits in a subdirectory of the workspace, you need to type `python subdirectory/filename.py` to run the code. 

> Setting the root of the workspace is very important. It exempts you from typing the full path of the file. Also if you passed your workspace to someone else, he/she can run the code without changing the path.  

## Run codes in Jupyter Notebook

  * [Jupyter Notebook in vscode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
   

