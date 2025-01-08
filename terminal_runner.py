import subprocess
import sys
import tkinter as tk
from tkinter import scrolledtext, messagebox, Listbox, END, simpledialog
import logging
import re
import shlex  # Import the shlex module

# Set up logging
logging.basicConfig(filename='command_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

command_history = []

# Mapping of natural language prompts to commands
command_mapping = {
    "list files": "ls",
    "show directory contents": "ls",
    "display files": "ls",
    "current directory": "pwd",
    "show current directory": "pwd",
    "change directory": "cd",
    "move to directory": "cd",
    "copy file": "cp",
    "copy": "cp",
    "move file": "mv",
    "move": "mv",
    "delete file": "rm",
    "remove file": "rm",
    "delete directory": "rm -r",
    "remove directory": "rm -r",
    "create directory": "mkdir",
    "make directory": "mkdir",
    "show disk usage": "df -h",
    "disk usage": "df -h",
    "show processes": "ps",
    "list processes": "ps",
    "kill process": "kill",
    "terminate process": "kill",
    "show date": "date",
    "current date": "date",
    "show time": "date",
    "current time": "date",
    "show calendar": "cal",
    "calendar": "cal",
    "show users": "who",
    "list users": "who",
    "show environment variables": "env",
    "environment variables": "env",
    "show system information": "uname -a",
    "system information": "uname -a",
    "show network interfaces": "ifconfig",
    "network interfaces": "ifconfig",
    "show ip address": "ip addr",
    "ip address": "ip addr",
    "update packages": "sudo pacman -Syuv ",
    "update all packages": "sudo pacman -Syu --noconfirm",
    "upgrade packages": "sudo pacman -Syu --noconfirm",
    "upgrade all packages": "sudo pacman -Syu --noconfirm",
    "install package": "sudo pacman -S --noconfirm",
    "remove package": "sudo pacman -R --noconfirm",
    "clean package cache": "sudo pacman -Sc --noconfirm",
    "clean all package cache": "sudo pacman -Scc --noconfirm",
}

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout
        logging.info(f"Command: {command}\nOutput: {output}")
        return output
    except subprocess.CalledProcessError as e:
        error_msg = f"Error: {e.stderr}"
        logging.error(f"Command: {command}\nError: {error_msg}")
        return error_msg

def validate_command(command):
    # Simple validation to check for potentially dangerous commands
    dangerous_patterns = [r'rm -rf', r'format', r'del /q']
    for pattern in dangerous_patterns:
        if re.search(pattern, command, re.IGNORECASE):
            return False
    return True

def suggest_commands(prompt):
    suggestions = []
    for key, command in command_mapping.items():
        if key in prompt.lower():
            suggestions.append(command)
    return suggestions

def execute_command():
    prompt = command_entry.get()
    print(f"User prompt: {prompt}")  # Debug statement
    if prompt.lower() == 'exit':
        root.quit()
    elif prompt.lower() == 'history':
        history_text.delete(1.0, tk.END)
        for idx, cmd in enumerate(command_history, start=1):
            history_text.insert(tk.END, f"{idx}. {cmd}\n")
    else:
        suggestions = suggest_commands(prompt)
        print(f"Suggestions: {suggestions}")  # Debug statement
        if suggestions:
            if len(suggestions) == 1:
                selected_command = suggestions[0]
                if not validate_command(selected_command):
                    messagebox.showerror("Validation Error", "Potentially dangerous command detected!")
                    return
                if "sudo" in selected_command:
                    password = simpledialog.askstring("Password", "Enter your password:", show='*')
                    if password:
                        # Properly escape the password and format the command
                        selected_command = f"echo {shlex.quote(password)} | sudo -S {selected_command.split('sudo ', 1)[1]}"
                    else:
                        messagebox.showerror("Permission Denied", "Password is required for this command.")
                        return
                output = run_command(selected_command)
                command_history.append(selected_command)
                output_text.insert(tk.END, f"Command: {selected_command}\nOutput:\n{output}\n\n")
                output_text.see(tk.END)
            else:
                suggestion_listbox.delete(0, END)
                for suggestion in suggestions:
                    suggestion_listbox.insert(END, suggestion)
                suggestion_label.pack()
                suggestion_listbox.pack()
                select_button.pack()
        else:
            messagebox.showinfo("No Suggestions", "No commands suggested for the given prompt.")

def select_command():
    selected_command = suggestion_listbox.get(suggestion_listbox.curselection())
    if not validate_command(selected_command):
        messagebox.showerror("Validation Error", "Potentially dangerous command detected!")
        return
    if "sudo" in selected_command:
        password = simpledialog.askstring("Password", "Enter your password:", show='*')
        if password:
            # Properly escape the password and format the command
            selected_command = f"echo {shlex.quote(password)} | sudo -S {selected_command.split('sudo ', 1)[1]}"
        else:
            messagebox.showerror("Permission Denied", "Password is required for this command.")
            return
    output = run_command(selected_command)
    command_history.append(selected_command)
    output_text.insert(tk.END, f"Command: {selected_command}\nOutput:\n{output}\n\n")
    output_text.see(tk.END)
    suggestion_label.pack_forget()
    suggestion_listbox.pack_forget()
    select_button.pack_forget()

# Set up the GUI
root = tk.Tk()
root.title("Terminal Command Runner")

command_label = tk.Label(root, text="Enter command:")
command_label.pack()

command_entry = tk.Entry(root, width=50)
command_entry.pack()

run_button = tk.Button(root, text="Run Command", command=execute_command)
run_button.pack()

output_label = tk.Label(root, text="Output:")
output_label.pack()

output_text = scrolledtext.ScrolledText(root, width=70, height=20)
output_text.pack()

history_label = tk.Label(root, text="Command History:")
history_label.pack()

history_text = scrolledtext.ScrolledText(root, width=70, height=10)
history_text.pack()

suggestion_label = tk.Label(root, text="Suggested Commands:")
suggestion_listbox = Listbox(root, width=50, height=5)
select_button = tk.Button(root, text="Select Command", command=select_command)

root.mainloop()