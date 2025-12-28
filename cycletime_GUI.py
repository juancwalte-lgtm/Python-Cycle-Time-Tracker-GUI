import time
import random
import pandas as pd
from tkinter import *
from datetime import datetime

# Define function for start button
def start():
    global start_time
    start_time = time.time()

# Define function for stop button
def stop():
    global stop_time
    stop_time = time.time()
    # Calculate cycle time
    cycle_time = stop_time - start_time
    # Generate serial number
    serial_number = random.randint(1000, 9999)
    # Get user input
    name = name_entry.get()
    item = item_entry.get()
    # Get current date and time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # Create dataframe
    df = pd.DataFrame({'Date/Time': [date_time], 'Name': [name], 'Item': [item], 'Cycle Time': [cycle_time], 'Serial Number': [serial_number]})
    # Export to Excel
    with pd.ExcelWriter('manufacturing_cycle_time_GUI.xlsx', mode='a', engine='openpyxl', if_sheet_exists='new') as writer:
        df.to_excel(writer, index=False, sheet_name='Widget 1 cycle time')

# Create GUI
root = Tk()
root.title("Manufacturing Cycle Time Calculator")

# Add label for name field
name_label = Label(root, text="Name:")
name_label.grid(row=0, column=0)

# Add entry field for name
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

# Add label for item field
item_label = Label(root, text="Item:")
item_label.grid(row=1, column=0)

# Add entry field for item
item_entry = Entry(root)
item_entry.grid(row=1, column=1)

# Add start button
start_button = Button(root, text="Start", command=start)
start_button.grid(row=2, column=0)

# Add stop button
stop_button = Button(root, text="Stop", command=stop)
stop_button.grid(row=2, column=1)

# Add serial number button
serial_button = Button(root, text="Generate Serial Number", command=lambda: random.randint(1000, 9999))
serial_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
