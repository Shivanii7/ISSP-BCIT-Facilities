import os
import tkinter as tk
from tkinter import filedialog

# Function to either ask the user for a file path or use a file dialog
def select_file():
    # Ask the user if they want to use file dialog or enter file path manually
    use_file_dialog = input("Do you want to use a file dialog to select the file? (y/n): ").lower()
    
    if use_file_dialog == 'y':
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        file_path = filedialog.askopenfilename(title="Select a file to rename")
        return file_path
    else:
        file_path = input("Enter the full path of the file: ")
        if os.path.isfile(file_path):
            return file_path
        else:
            print("The file path is not valid.")
            return None

# Function to rename the selected file based on user input
def rename_file():
    # Let the user select a file
    original_file = select_file()
    if not original_file:
        print("No file selected or invalid file path.")
        return

    # Ask the user for the building name and date
    building_name = input("Enter the building name: ")
    date = input("Enter the date (YYYY-MM-DD): ")

    # Construct the new file name using the building name and date
    new_file_name = f"{building_name}_{date}{os.path.splitext(original_file)[1]}"
    new_file_path = os.path.join(os.path.dirname(original_file), new_file_name)

    try:
        # Rename the file
        os.rename(original_file, new_file_path)
        print(f"File renamed to: {new_file_name}")
    except FileNotFoundError:
        print("The file was not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the rename_file function
rename_file()
