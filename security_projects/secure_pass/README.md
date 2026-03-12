#  MyPass: My First Python Project

Welcome to **MyPass**, a desktop password validator. This is my very first project built with **Python**, focusing on GUI (Graphical User Interface) development and string logic with a cybersecurity focus

---

## Overview
The goal of this project was to create a functional tool that helps users evaluate password strength. It taught me how to bridge the gap between "code logic" and a "user window." I ran into a few issues. I utilized AI to help with creation of code pieces and then fix the errors from my python learning. 

---

## Features
* **Security Check:** Instantly validates if a password meets safety standards (this was simply to create a project, will expand on password complexity and create more options such as including a password generator.)
* **Visibility Toggle:** A "Show Password" checkbox to mask or reveal text.
* **Dynamic Feedback:** The UI updates colors (Green/Red) based on the result.
* **Credential Storage:** Save username and password combinations to a text file for demonstration purposes (not secure for real use).

---

## What I Learned
Through this project, I mastered several core programming concepts:
* **Use of Tkinter** this was helpful to create user interction in a window, not just commandline.
* **Event Handling:** Using buttons to trigger functions.
* **State Management:** Using `tk.IntVar()` to remember if a checkbox is clicked.
* **String Analysis:** Using `any()` and `isdigit()` to "peek" inside text strings. I learned this recently in my 30 days of python project(other repository)
* **The Main Loop:** Understanding how `root.mainloop()` keeps an app running.

---
## AI-Assisted Learning & Syntax
I utilized AI to break down complex Python concepts into understandable pieces, to find out how to do things like create buttons with tkinter and create file and save input to it. Here are the specific functions I mastered during this build:

### **Tkinter Functions (The UI)**
* **`.get()`**: The "magic method" used to grab whatever text the user typed into the box so the code can analyze it.
* **`.config()`**: Used to dynamically update the Label's text and color (e.g., changing "Waiting..." to "Strong ✅") without restarting the app.
* **`tk.IntVar()`**: A special Tkinter variable used to track the "state" (on or off) of the Show Password checkbox.
* **`root.mainloop()`**: The engine of the app that keeps the window open and listening for clicks.

### **Logic Functions (The Brain)**
* **`len()`**: Used to calculate the total count of characters to ensure the password is at least 12 digits long.
* **`any()`**: A powerful tool that scans the password string and returns "True" if it finds at least one match for my rules.
* **`.isupper()` / `.islower()`**: String methods that check for capital and small letters.
* **`.isdigit()`**: A method used to identify if a character is a number.
* **`open()` and File I/O**: The core function for creating and writing to files; using mode "a" (append) to add new data without overwriting existing entries.
* **`with` Statement**: A context manager that automatically handles opening and closing files, preventing resource leaks.
* **Encoding (`utf-8`)**: Specifies character encoding to ensure text is stored correctly and can be read across different systems and languages.
* **Dictionary Storage**: Saving credentials in a key-value format (username:password) for structured, parseable data storage. This was recently learned as part of my python learning and inspiration for adding this to the program. 
---

## The "Strong Password" Rules
To be marked as **Strong ✅**, the password must pass these four tests:

1.  **Length:** At least 12 characters long.
2.  **Uppercase:** Contains at least one CAPITAL letter.
3.  **Lowercase:** Contains at least one lowercase letter.
4.  **Numbers:** Contains at least one digit (0-9).
---

## Core Concepts Mastered
* **Event Handling:** Connecting a button click (`command=`) to a specific Python function.
* **Boolean Logic:** Using `and` to ensure *all* conditions are met before validating.
* **Conditional Branching:** Using `if/else` to provide different feedback based on user input.