#load_locked_accounts(filepath)
#    input:  a filename string
#    output: a set of clean account names

#check_username(username, locked_accounts)
#    input:  a username string, a set of account names
#    output: True or False

#report_result(username, result)
#    input:  a username string, a boolean
#    output: prints locked or allowed
    
def load_locked_accounts(filepath):
    locked_accounts = set()
    with open(filepath,"r") as locked_file:
        for name in locked_file:
             locked_accounts.add(name.strip())
    return locked_accounts

def check_username(username, locked_accounts):
    return username in locked_accounts

def report_result(username,result):
    if result == True:
        print(f"{username} is locked")
    else:
        print(f"{username} is allowed")

def main():
    locked_accounts = load_locked_accounts("locked_accounts.txt")
    with open("usernames_status.txt", "r") as f:
        for line in f:
            username = line.strip()
            account_name = check_username(username,locked_accounts)
            report_result(username,account_name)

if __name__ == "__main__":
    main()