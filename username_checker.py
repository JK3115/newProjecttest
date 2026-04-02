# 1. Create Locked account file
# 2. Create file of usernames to check against locked account file
# 3. for username check against locked account file
# 4. if account is in list, print denied
# 5. if account not in list, print allowed.

def main():
    locked_accounts = set()  # Create an empty set to store locked account names
    with open("locked_accounts.txt", "r") as locked_file:  # Open the locked accounts file for reading
        for name in locked_file:  # Loop through each line in the locked accounts file
            locked_accounts.add(name.strip())  # Remove whitespace/newline and add the name to the set

    with open("usernames_status.txt", "r") as f:  # Open the usernames file for reading
        for line in f:  # Loop through each line in the usernames file
            username = line.strip()  # Remove whitespace/newline from the username
            if username in locked_accounts:  # Check if the username exists in the locked accounts set
                print(f"{username} is locked.")  # Print locked message if found
            else:
                print(f"{username} is allowed.")  # Print allowed message if not found

if __name__ == "__main__":  # Only run main() if this script is executed directly (not imported)
    main()  # Call the main function