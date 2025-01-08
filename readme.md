# <i> NLP Command Executor

## Introduction

NLP Command Executor is a graphical user interface (GUI) based tool designed to execute terminal commands using natural language prompts. This tool aims to simplify the process of running commands by allowing users to input plain English descriptions, which are then mapped to corresponding terminal commands. The application also includes features for command history management, command suggestions, and basic validation to prevent potentially dangerous actions.

## Key Features
<b> * Natural Language Prompts:</b> Users can input natural language descriptions, which are translated into specific terminal commands.

<b> * Command Suggestions:</b> The tool suggests commands based on the user's input, making it easier to find the right command.

<b> * Command History:</b> Users can view and manage a history of executed commands.
Security: The tool includes basic validation to prevent the execution of potentially dangerous commands.

<b> * Sudo Command Handling:</b> Securely handle sudo commands with password input.
User-Friendly Interface: A simple and intuitive GUI for entering commands and viewing outputs.

### Prerequisites

<b>1. Python:</b>  Ensure you have Python installed on your system. The script is compatible with Python 3.x.
                               You can download Python from the official Python website.

<b>2. Tkinter:</b> Tkinter is the standard GUI library for Python. It comes pre-installed with Python on most systems.
If it's not installed, you can install it using your package manager. For example, on Debian-based systems, you can use:
_A guide on how to install the tools needed for running the project._

## Installation Process
### Step 1: Install Python

1. **Download Python**:
   - Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.

2. **Install Python**:
   - Follow the installation instructions for your operating system.
   - Ensure that you check the option to add Python to your system PATH during installation.

3. **Verify Installation**:
   - Open a terminal or command prompt and run:
     ```sh
     python --version
     ```
   - You should see the installed Python version.

### Step 2: Install Pip

Pip is the package installer for Python and comes pre-installed with Python. To ensure pip is installed, follow these steps:

1. **Verify Pip Installation**:
   - Open a terminal or command prompt and run:
     ```sh
     pip --version
     ```
   - You should see the installed pip version.

2. **Install Pip (if not installed)**:
   - If pip is not installed, you can install it using the following command:
     ```sh
     python -m ensurepip --upgrade
     ```

### Step 3: Install Tkinter

Tkinter is the standard GUI library for Python and comes pre-installed with Python on most systems. To ensure Tkinter is installed, follow these steps:

1. **Verify Tkinter Installation**:
   - Open a terminal or command prompt and run:
     ```sh
     python -m tkinter
     ```
   - A small window should appear, indicating that Tkinter is installed correctly.

2. **Install Tkinter (if not installed)**:
   - If Tkinter is not installed, you can install it using your package manager. For example, on Debian-based systems, you can use:
     ```sh
     sudo apt-get install python3-tk
     ```

### Step 4: Clone the Repository

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/tarunerror/nlp-terminal.git

#### Navigate to the Project Directory:
 ```sh
     cd nlp-terminal
   ```

### Step 5: Create and Activate a Virtual Environment (Optional)
1. **Create a Virtual Environment:**

     ```sh
     python -m venv venv
     ```


2. **Activate the Virtual Environment:**

- On Windows:
     ```sh
    venv\Scripts\activate
     ```


- On macOS and Linux:

     ```sh
    source venv/bin/activate
     ```

## Usage
1. **Run the Script:**

     ```sh
    python terminal_runner.py
     ```


2. **Enter Commands:** Use the GUI to enter natural language prompts and see the corresponding terminal commands executed.

## Technologies

_Technologies used in the project._ 
* [Python](https://www.python.org/) - Language Used.
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - UI Library.

## License
Mozilla Public [license](https://github.com/tarunerror/nlp-terminal/blob/main/LICENSE) 2.0

</i>
