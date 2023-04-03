
# menu_bar.py: A module to create a menu bar at the top of the main window, 
# containing options like 'File', 'Settings', 'Help', and 'About'. This would
# improve the overall organization of the application.

# The create_menu_bar function creates a menu bar at the top of the main 
# window with 'File', 'Settings', 'Help', and 'About' options. The 'File' 
# menu contains an 'Exit' option to close the application, and the 'Settings', 
# 'Help', and 'About' options open the corresponding windows.

# Remember to implement the about_callback function to display information 
# about the application in the 'About' window.

import tkinter as tk

def create_menu_bar(root, settings_callback, help_callback, about_callback):
    menu_bar = tk.Menu(root)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    settings_menu = tk.Menu(menu_bar, tearoff=0)
    settings_menu.add_command(label="Settings", command=settings_callback)
    menu_bar.add_cascade(label="Settings", menu=settings_menu)

    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="Help", command=help_callback)
    help_menu.add_command(label="About", command=about_callback)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    root.config(menu=menu_bar)
