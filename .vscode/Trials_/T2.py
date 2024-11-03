import customtkinter as ctk
from tkcalendar import Calendar
from tkinter import Toplevel
import subprocess
import sys
from datetime import datetime
def install_requirements():
    try:
        # Attempt to import a core package to test if dependencies are installed
        import customtkinter  # replace with a package your app needs
    except ImportError:
        print("Required packages not found. Installing...")
        # Install packages from requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("All packages installed.")

install_requirements()

# Your main program starts here
# Example: root = ctk.CTk()
# Create the main window
root = ctk.CTk()
root.geometry("300x200")

def open_date_picker():
    # Create a new Toplevel window for the date picker
    top = Toplevel(root)
    top.title("Select a Date")
    
    # Create a Calendar widget
    cal = Calendar(top, selectmode='day', date_pattern = "yyyy-mm-dd")
    cal.pack(pady=10)

    # Function to get and display the selected date
    def select_date():
        selected_date = cal.get_date()
        date_label.configure(text=f"Selected Date: {selected_date}")
        top.destroy()  # Close the date picker

    # Button to confirm the date selection
    select_button = ctk.CTkButton(top, text="Select Date", command=select_date)
    select_button.pack(pady=10)

# Button to open the date picker
open_button = ctk.CTkButton(root, text="Pick a Date", command=open_date_picker)
open_button.pack(pady=20)

# Label to display the selected date
date_label = ctk.CTkLabel(root, text="No Date Selected")
date_label.pack(pady=10)

# Start the main loop
root.mainloop()
date_time = datetime. now()
todays_date = date_time.date()
print(todays_date)
print("Thiruvananthapuram".upper())