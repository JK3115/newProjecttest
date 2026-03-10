
# mypass: Password Security Checker

A lightweight Python desktop application built with **Tkinter** that evaluates the strength of a password in real-time. This tool is designed to showcase my understanding basic security requirements for strong credentials and my learning experience with python. 

##  Project Context
This is my **first Python project**, developed to showcase my initial learning in the language. It focuses on several core programming concepts:
* **GUI Development:** Using the Tkinter library to build a functional desktop interface.
* **Logic & Validation:** Implementing conditional statements and list comprehensions to verify security requirements.
* **User Experience:** Incorporating interactive features like visibility toggles and dynamic feedback.

##  Features
* **Security Logic:** Automatically validates passwords for complexity.
* **Interactive UI:** A clean, responsive 600x400 window for user interaction.
* **Toggle Visibility:** Includes a "Show Password" checkbox to toggle between masked (`***`) and plain text.
* **Visual Feedback:** Dynamic color-coded status messages:
  * **Green:** Strong password meets all requirements.
  * **Red:** Weak password needs improvement.

##  Built With
* **Python 3.x**
* **Tkinter**: Python’s standard library for Graphical User Interfaces.

##  Installation & Setup
Since this project uses Python's standard library, no external `pip` installations are required.

1. **Clone the repository:**
   ```powershell
   git clone [https://github.com/your-username/mypass-repo.git](https://github.com/your-username/mypass-repo.git)
   cd mypass-repo

2. **Run the application:**
```
python mypass.py
```
##  Security Criteria

To receive a **"Strong ✅"** rating, the password must meet the following logic:

* At least **12 characters** long.
* Contains at least one **uppercase** letter.
* Contains at least one **lowercase** letter.
* Contains at least one **number**.

##  Project Structure

* `mypass.py`: The main script containing the Tkinter UI and validation logic.

---
## Acknowledgments & Learning Process
This project was built as a practical application of the concepts learned through:
* **[30 Days Of Python](https://github.com/Asabeneh/30-Days-Of-Python):** This curriculum provided the foundation for my understanding of Python syntax, data types, and functional programming.
* **AI Collaboration:** I utilized AI assistance to help debug UI layout issues, refine the password validation logic, and structure the project documentation. This collaborative approach allowed me to bridge the gap between theoretical lessons and a working application.
* **Lessons Learned:** While AI did much of the architecture here, I did see that initial planning of a project is vital to creating any program or app. I have a better idea on how to start in the future and take more of the so-called "training wheels" off when using AI and lessen my reliance on that tool.

*Developed as part of my journey into Python and Cybersecurity.*
