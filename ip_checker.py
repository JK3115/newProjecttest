# PLAN:
# 1. Load the known-bad IP list from a file
# 2. Load the IPs I want to check from another file
# 3. Loop through each IP I want to check
# 4. If it's in the bad list, print a warning
# 5. If it's not, print it's clean

# A set of known-bad IP addresses to check against
BLOCKLIST = {
    "192.168.1.1",
    "10.0.0.1",
    "203.0.113.42",
}

# Define the main function — all script logic lives here
def main():
    # Open ips.txt in read mode; "with" ensures the file is closed automatically when done, f is an accepted convention for file handles. Its short and established as a vairable constant.
    with open("ips.txt", "r") as f:
        # Loop over each line in the file one at a time
        for line in f:
            # Remove the trailing newline character so the IP matches cleanly
            ip = line.strip()
            # Check if the IP exists in the blocklist set
            if ip in BLOCKLIST:
                # IP was found in the blocklist — flag it
                print(f"BLOCKED: {ip}")
            else:
                # IP was not found in the blocklist — it's clean
                print(f"clean:   {ip}")

# Only run main() if this script is executed directly (not imported by another script)
if __name__ == "__main__":
    main()
