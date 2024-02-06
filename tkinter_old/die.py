import tkinter as tk 
import random
import winsound as ws


#This is an old version of PyDie, using tkinter instead of PyQt5. 
#This version will not be maintained, and is only here for historical purposes.

# Create a new Tk instance with a dark background
root = tk.Tk()
root.configure(bg='#333333')
root.geometry("500x500")
root.title("PyDie")

try:
    root.iconbitmap("pydie.ico")
except Exception as e:
    print("Error Encountered: " + str(e))
    

# Map die types to their maximum values
die_values = {"D100":100, "D20": 20, "D12": 12, "D10": 10, "D8": 8, "D6": 6, "D4": 4, "Coin Flip":2, "Custom": 1}

# Create a StringVar for the result with a default value
result = tk.StringVar()
result.set("Roll a Die")

# Create an entry for custom die values, not visible by default
 


def roll_die():
    ws.Beep(random.randrange(37,2500), 100)
    die_type = selected.get()
    roll_result = random.randint(1, die_values[die_type])
    
    if die_type == "Coin Flip":
        if roll_result == 1: 
            roll_result = "Tails"
        else:
            roll_result = "Heads"
    
    if die_type == "Custom":
        custom_die_value = custom_die_entry.get()
        if custom_die_value.isnumeric():
            roll_result = random.randint(1, int(custom_die_value))
        else:
            roll_result = "Invalid Custom Die Value"

    history.insert(0, f"{'Die Type:' + die_type + ' ' if die_type != 'Coin Flip' else die_type + ' '}Result: {roll_result}")
    result.set(roll_result)



def die_selector_handler(value):
    print(value)
    if selected.get() == "Custom":
        custom_die_entry.pack()
    else:
        custom_die_entry.pack_forget()
        print("Custom Die Entry Hidden")

# Create a label to display the result
result_label = tk.Label(root, textvariable=result, bg='black', fg='white', font=("Aptos", 24))
result_label.pack(pady=20)

# Create a StringVar for the selected die type with a default value
selected = tk.StringVar(root)
selected.set("D20")

# Create an OptionMenu for selecting the die type
die_selector = tk.OptionMenu(root, selected, *die_values.keys(), command=die_selector_handler)
die_selector.configure(bg='grey', fg='white', font=("Helvetica", 16))
die_selector.pack(pady=20)

#Custom die entry, hidden by default
custom_die_entry_container =tk.Frame(root, bg='grey')
custom_die_entry_container.pack() 
custom_die_entry = tk.Entry(custom_die_entry_container, bg='grey', fg='white', font=("Helvetica", 16))  
custom_die_entry.pack()
custom_die_entry.pack_forget()

# Create a button to roll the die
roll_button = tk.Button(root, text="Roll", command=roll_die, bg='grey', fg='white', font=("Helvetica", 16))
roll_button.pack(pady=20)

history = tk.Listbox(root, bg='grey', fg='white', font=("Helvetica", 16), width=30)
history.pack(pady=20)

root.mainloop()