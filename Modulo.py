prompt=("\nPlease give me a number, I will tell you if its divisible by 10?")
prompt+="\n(Enter 'quit' to exit:) "


digit=int(prompt)
while digit == "quit":
        if digit % 10 == 0:
         print("This is divisible by 10!.")
        else:
         print("Please please try again.")

        if digit == "quit":
                print("Goodbye!")