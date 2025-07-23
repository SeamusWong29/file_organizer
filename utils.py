from datetime import datetime
from pathlib import Path
import os, shutil


def organize_by_extension(folder_path: str, dry_run=False):
    """
    Organize files in the given folder into sub-folder based on file extension

    Parameters:
        folder_path (str): Path to the folder containing files
    """
    folder = Path(folder_path) # convert raw string into an intelligent path object
    for file in folder.iterdir(): # Loop through everything inside this folder
        if file.is_file(): # only file, not a folder 
            ext = file.suffix[1:] or "no_ext" # file.suffix gets the part from the last dot, including the dot itself:
            target = folder / ext # / operator between two opbjects return a new path object
            
            if dry_run:
                print(f"[DRY-RUN] Would move {file.name} -> {target / file.name}")
            else:
                target.mkdir(exist_ok=True) # # Create the folder at 'target' path if it doesn't exist yet.
                shutil.move(str(file), str(target / file.name))
            # Move the file from its current location to the 'target' folder,
            # keeping the same filename. Convert Path objects to strings because shutil.move expects strings.

def organize_by_date(folder_path: str, dry_run=False):
    """
    Organize files in the given folder based on file creation date

    Parameters:
        folder_path (str): Path to the folder containing files
        dry_run (bool): If True, actions are only printed, not executed
    """
    folder = Path(folder_path)
    for file in folder.iterdir():
        if file.is_file():
            timestamp = file.stat().st_ctime # unix timestamp (unreadable) to datetime object to human readable string
            date_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
            target = folder / date_str # Path object for target folder

            if dry_run:
                print(f"[DRY-RUN] Would move {file.name} -> {target / file.name}")
            else:
                target.mkdir(exist_ok=True)
                shutil.move(str(file), str(date_str / file.name)) #Must include the filename, not just the target folder

            



    # Shell Untilites for copying moving, deleting files/folders 
    # 1. iterate the folder
    # 2. check if it's a file
    # 3. check if the file has an ext 
    # 4. create folder with its ext name
    # 5. move the file there
    
    