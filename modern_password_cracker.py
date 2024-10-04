import crypt  # Import the crypt module for Unix-style password hashing
from passlib.hash import sha512_crypt

# Function to test passwords from the dictionary file against the hashed password
def testPass(cryptPass):
    # Extract the salt from the hashed password (first two characters)
    salt = cryptPass[0:2]
    custom_salt = "abc123XYZ789.pq"

    # Open the dictionary file containing potential passwords
    with open('dictionary.txt', 'r') as dictFile:
        # Iterate through each word in the dictionary file
        for word in dictFile:
            # Remove any newline characters from the word
            word = word.strip('\n')
            
            # Encrypt the word using the same salt as the hashed password
            cryptWord = crypt.crypt(word, salt)
            
            # Check if the encrypted word matches the hashed password
            if cryptWord == cryptPass:
                # If a match is found, print the found password and exit the function
                print("[+] Found Password using crypt: " + word + "\n")
                return
        
    # If no match was found with crypt.crypt, try sha512_crypt
    print("[-] Password not found with crypt.crypt, trying sha512_crypt...\n")
    
    # Re-open the dictionary file to iterate through words again
    with open('dictionary.txt', 'r') as dictFile:
        # Iterate through each word in the dictionary file
        for word in dictFile:
            word = word.strip('\n')
            
            # Encrypt the word using SHA-512 and a custom salt
            cryptWord = sha512_crypt.hash(word, salt=custom_salt)
            
            # Check if the encrypted word matches the hashed password
            if cryptWord == cryptPass:
                # If a match is found, print the found password and exit the function
                print("[+] Found Password using SHA-512: " + word + "\n")
                return
    
    # If no match is found after both attempts
    print("[-] Password not found with either method.\n")

# Main function to read the password file and attempt to crack each password
def main():
    # Open the file containing usernames and hashed passwords
    with open("password.txt") as passFile:
        # Iterate through each line in the password file
        for line in passFile:
            # Check if the line contains a ':' character, indicating a username:hashed_password format
            if ":" in line:
                # Split the line at ':' to separate the username and hashed password
                user = line.split(':')[0]  # Extract the username
                cryptPass = line.split(':')[1].strip()  # Extract the hashed password and remove any whitespace
                
                # Print the username for which the password is being cracked
                print("[+] Cracking Password for: " + user)
                
                # Call the testPass function to attempt to crack the hashed password
                testPass(cryptPass)

# Entry point for the script; only runs when the script is executed directly
if __name__ == "__main__":
    main()  # Call the main function
