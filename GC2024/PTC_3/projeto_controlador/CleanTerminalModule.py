"""This is just a Module that holds a function which can clean the user/
developer terminal. Simple. To use, call 'clean_terminal()'"""

# Built-in Python Modules
import os

# Third-Party Python Modules
import platform

registered_os = {'windows' : lambda: os.system('cls'),
                 'linux' : lambda: os.system('clear'),
                   'mac' : lambda: os.system('clear')}

def clean_terminal():
    """Normally, it's a self-explanatory function, although, this function
    is meant to clean the terminal depending on which system the user or the
    developer is coding."""
    current_os = platform.system()

    do_with_terminal = registered_os.get(current_os.lower()) if current_os is not None\
                       else print("Unknown terminal cleaning method. ")
    
    return do_with_terminal()