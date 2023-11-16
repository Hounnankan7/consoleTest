import os
import subprocess
import tkinter as tk
import PIL as pil
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def list_games(directory):
    """Recursively lists directories containing a main.lua file."""
    game_dirs = []
    for root, dirs, files in os.walk(directory):
        if 'main.lua' in files:
            dir_name = os.path.basename(root)
            game_dirs.append(dir_name, root)
    print("Found games:",game_dirs) # DEBUGGING LINE
    return game_dirs

def launch_game(event):
    """Launches the selected game."""
    selected_item = game_tree.focus()
    game_info = game_tree.item(selected_item)
    """selected_game_dir = game_listbox.get(tk.ANCHOR)"""
    game_path = game_info['values'][1]
    if game_path:
        subprocess.run(["love", game_path])
    else:
        messagebox.showinfo("Info", "Please select a game first.")

# Change this to the path where your games are stored
games_directory = "/root/Bureau/Project"

# Set up the main window
root = tk.Tk()
root.title("Love2D Game Launcher")

#Create a treeview to show the games with images
game_tree = ttk.Treeview(root, columns=("Name", "Path"), show='headings')
game_tree.heading('Name', text="Game Name")
game_tree.column('Name', width=150)
game_tree.heading('Path', text="Path")
game_tree.column('Path', width=0) #Hide the 'Path' column

#Populate the treeview with available game
for game_name, game_dir in list_games(games_directory):
    image_path = os.path.join(game_dir, "game_icon.png")
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((20, 20), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        game_tree.insert('', tk.END, values=(game_name, game_dir), image=img)
    else:
        game_tree.insert('', tk.END, values=(game_name, game_dir))

game_tree.bind('<Double-1>', lauch_game)
game_tree.pack(fill=tk.BOTH, expand=True)

# Start the GUI event loop
root.mainloop()
