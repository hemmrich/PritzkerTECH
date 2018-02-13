# Python & IDLE Installation Instructions

## Why Python?

Python is one of the most popular general-purpose programming languages available at this time. It's easy to learn and use, has extensive community support, and runs on all major operating systems. It can be used for essentially any task including web development, data analysis, game development, machine learning...you get the point.


## What is IDLE?

Software developers use text editors or integrated development environments (IDEs) to write their code - think Microsoft Word for programming. There are many good IDEs for Python, with Python's Integrated Development and Learning Environment (IDLE) being one of the best free ones. Plus, it's bundled with our Python installation below so we don't have to install yet another thing.

## Python Installation (OSX)


#### Step 1: Install GCC

* Open Terminal (Applications > Terminal or search for Terminal using Spotlight), type `gcc`, then hit Enter
  * If the output is ``clang: error: no input files``, gcc is already installed. Move on to step 2. 
  * If gcc is not installed, macOS will prompt you to install it. Hit "Install" and follow the instructions.


#### Step 2: Install Homebrew

Homebrew is a package manager for macOS. Think App Store for developers. We will use Homebrew to install the newest version of Python.

* Open Terminal and copy/paste the following line.
  * ``ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)``
  * You'll be prompted to enter your macOS password during the installation. Type your password and hit Enter. Note that Terminal won't show that characters are being entered during a password prompt.
* Add Homebrew to PATH (so that your Mac can find it)
  * Copy/paste the following line into your terminal
    * ``echo "export PATH=/usr/local/bin:/usr/local/sbin:\$PATH" >> ~/.profile && source ~/.profile``


#### Step 3: Install Python using Homebrew

* Open Terminal and copy/paste the following line to install Python
  * ``brew install python3``
* Ensure that Python, pip (Python package manager), and IDLE were included in the installation
  * Run the command `python3 --version` (should output something like Python 3.6.4)
  * Run the command `pip3 --version` (should output something like pip 9.0.1)
  * Run the command `idle3` (should open a new Terminal window titled "Python 3.6.4 Shell")
  * If either output includes the phrase "command not found", the installation was unsuccessful.

#### Step 4: Install necessary Python modules for our workshop

Now that we have Python, IDLE, and the pip package manager installed, the last thing we need to do is install the necessary modules (code that other people wrote) that we'll use during the workshop for things like mathematical operations and making graphs.

* Run the following command in Terminal
  * `pip3 install matplotlib pandas numpy statsmodels`


If you struggled with any part of the instructions, please reach out to me (hemmrich@uchicago.edu or find me in person) before the workshop.

That's it! See you on Friday :)



## Python Installation (Windows)

#### Step 1: Determine if you're running 32 or 64 bit Windows

* Navigate to Control Panel > System and Security > System and check the "System type" field
* Most newer Windows installations should be 64-bit

#### Step 2: Download the Python Installer

* In a web browser, navigate to `https://www.python.org/ftp/python/3.6.4/python-3.6.4-amd64.exe` (for 64-bit versions of Windows) or `https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe` (for 32-bit version of Windows)
* Save the installer

#### Step 3: Run the installer

* Run the installer downloaded in the last step
* At the installation screen, check the box that says "Add Python 3.6 to PATH"
* Click "Install Now" and follow the instructions

#### Step 4: Install the necessary Python modules for our workshop

* Open Command Prompt by searching for "Command Prompt" or "cmd" using the Start Menu
* Run the following command in Command Prompt
  * `pip install matplotlib pandas numpy statsmodels`
* If the above command returns an error, try running:
  * `C:/Python36/Scripts/pip install matplotlib pandas numpy statsmodels`

#### Step 5: Make sure Python and IDLE were installed correctly

* Open the Start menu and search for IDLE. One of the results should be an application named "IDLE (Python 3.6 64-bit)". Ensure that opening IDLE brings up a Python shell window.


If you struggled with any part of the instructions, please reach out to me (hemmrich@uchicago.edu or find me in person) before the workshop.

That's it! See you on Friday :)

