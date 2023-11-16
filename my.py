import os
import subprocess
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def list_games(directory):
    """Lists directories containing a main.lua file and their names."""
    game_dirs = []
    for root, dirs, files in os.walk(directory):
        if 'main.lua' in files:
            dir_name = os.path.basename(root)
            game_dirs.append((dir_name, root))
    return game_dirs

def launch_game(event):
    """Launches the selected game."""
    selected_item = game_tree.focus()
    if selected_item:
        game_info = game_tree.item(selected_item)
        game_path = game_info['values'][1]
        if game_path:
            subprocess.run(["love", game_path])

# Change this to the path where your games are stored
games_directory = "/path/to/your/games"

# Set up the main window
root = tk.Tk()
root.title("Love2D Game Launcher")

# Create a treeview to show the games with images
game_tree = ttk.Treeview(root, columns=("Name", "Path"), show='headings')
game_tree.heading('Name', text="Game Name")
game_tree.column('Name', width=150)
game_tree.heading('Path', text="Path")
game_tree.column('Path', width=0)  # Hide the 'Path' column

# Store the photo images in a list to prevent garbage collection
photo_images = []

# Populate the treeview with available games
for game_name, game_dir in list_games(games_directory):
    image_path = os.path.join(game_dir, "game_icon.png")  # Path to the game's icon image
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((20, 20), Image.ANTIALIAS)  # Resize the image
        img = ImageTk.PhotoImage(img)
        photo_images.append(img)  # Add to the list to prevent garbage collection
        game_tree.insert('', tk.END, values=(game_name, game_dir), image=img)
    else:
        game_tree.insert('', tk.END, values=(game_name, game_dir))

game_tree.bind('<Double-1>', launch_game)
game_tree.pack(fill=tk.BOTH, expand=True)

# Start the GUI event loop
root.mainloop()
