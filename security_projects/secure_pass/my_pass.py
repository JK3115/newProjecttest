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
    user_password = entry.get()
    is_secure = (len(user_password) >= 12 and 
                any(c.isupper() for c in user_password) and 
                any(c.islower() for c in user_password) and 
                any(c.isdigit() for c in user_password))
    if is_secure:
         label_result.config(text="Password strength: Strong ✅", fg="green")
    else:
        label_result.config(text="Too weak! (Needs 12+ chars, caps, & numbers)", fg="red")
# function to save password and username to a file (not secure, just for demonstration)
def save_credentials():
    # grab the values from the entry widgets
    username = entry_username.get()
    user_password = entry.get()
    # open (or create) a text file in append mode so we don't overwrite
    # every time the user clicks the button,
    with open("spice_rack.txt", "a", encoding="utf-8") as f:
        # write a simple line with a separator (This utilizes dictionaries for the list of credentials)
        f.write(f"{username}:{user_password}\n")
    # give the user feedback that we saved something
    label_result.config(text="Credentials saved!", fg="blue")

# 1. Setup the main window, sizing and text
root = tk.Tk()
root.title("mypass")
root.geometry("600x400")
# 2 . Create a Label widget for the title
label_title = tk.Label(root, text="Welcome to MyPass", font=("Arial", 24))
label_title.pack(pady=10)
# 2. Create an Entry widget for username (not required for password checking, just for demonstration)
label_username = tk.Label(root,text="Enter your username")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)
# 3. Create an Entry widget
label_instruction = tk.Label(root,text="Enter your password")
label_instruction.pack(pady=5)
entry = tk.Entry(root,show="*")
entry.pack(pady=5)
# 4. Create a Label to display results
label_result = tk.Label(root, text="")
label_result.pack(pady=5)
#  7. Creates toggle to show/hide password entered 
show_pass_var = tk.IntVar()
check_show = tk.Checkbutton(root, text="Show Password", variable=show_pass_var, command=toggle_password)
check_show.pack()
# 8. creates button for execution
btn_check = tk.Button(root, text="is this password secure?", command=check_password)
btn_check.pack(pady=10)
# 4. Button to save the username/password to a text file
btn_save = tk.Button(root, text="Save credentials", command=save_credentials)
btn_save.pack(pady=10)
# 9. Starts the event loop and keeps the window responsive for repeated use
root.mainloop()
