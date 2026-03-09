# import tkinter for UI features
import tkinter as tk
# function for toggle to show/hide password
def toggle_password():
    # If the checkbox is checked (var is 1), show the text
    if show_pass_var.get() == 1:
        entry.config(show="")
    else:
        entry.config(show="*")
# function for logic to check password for 12+ char, lower/uppper case, and numbers
def check_password():
    # .get() is the magic method that retrieves the text
    user_text = entry.get()
    is_secure = (len(user_text) >= 12 and 
                any(c.isupper() for c in user_text) and 
                any(c.islower() for c in user_text) and 
                any(c.isdigit() for c in user_text))
    if is_secure:
         label_result.config(text="Password strength: Strong ✅", fg="green")
    else:
        label_result.config(text="Too weak! (Needs 12+ chars, caps, & numbers)", fg="red")
        
# 1. Setup the main window, sizing and text
root = tk.Tk()
root.title("mypass")
root.geometry("600x400")
# 2. Create an Entry widget
label_instruction = tk.Label(root,text="Enter your password")
label_instruction.pack(pady=5)
# 3. Formatting for widget
entry = tk.Entry(root,show="*")
entry.pack(pady=5)
# 4. Create a Button to trigger the 'get' action
label_result = tk.Label(root, text="")
label_result.pack()
#  5. Creates toggle to show/hide password entered 
show_pass_var = tk.IntVar()
check_show = tk.Checkbutton(root, text="Show Password", variable=show_pass_var, command=toggle_password)
check_show.pack()
# 6. creates button for execution
btn_check = tk.Button(root, text="is this password secure?", command=check_password)
btn_check.pack(pady=10)
# 7. Starts the event loop and keeps the window responsive for repeated use
root.mainloop()

