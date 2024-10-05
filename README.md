A Python hashing crash crourse, if needed:
git push
[Understanding Hashing by Building Your Own Password Cracker (For Beginners)](https://medium.com/@sassom2112/understanding-hashing-by-building-your-own-password-cracker-for-beginners-9f0591e1e98d)
# SHA512 Password Cracker

This project demonstrates password cracking techniques based on poor salting practices and the strength of more robust hashing algorithms like SHA512. It consists of two password cracking approaches:

1. **Legacy Cracking Method** – Uses poor salting and Unix crypt (`/bin/shadow`) to crack passwords.
2. **Modern Cracking Method** – Leverages the SHA512 hashing algorithm to crack passwords with a known salt, highlighting its robustness compared to the older method.

## Project Structure

- **password.txt**: Contains two `/bin/shadow` credential entries.
- **dictionary.txt**: A dictionary file with possible password guesses.
- **unix_crypt_cracker.py**: A Python script that cracks passwords using the legacy Unix crypt method, leveraging the first two characters as the salt.
- **cryptWord.py**: A script that generates a SHA512 hash from a password and salt, which is used for the modern password cracker.
- **modern_password_cracker.py**: A Python program that cracks passwords using the SHA512 hashing algorithm. It works by hashing each word in the dictionary and comparing the results to the known hash in `password.txt`.

## How to Use This Repo

### Prerequisites

- **Python 3.x** must be installed on your system.
- Install any required dependencies (if applicable) using `pip`:
  ```bash
  pip install -r requirements.txt
  ```

## Steps to Run the Project
1. Clone the Repository:

```bash
git clone https://github.com/your-repo-url/password-cracker
cd password-cracker
```
2. View the Files:

+ password.txt: This contains the two password hashes you're trying to crack.
+ dictionary.txt: This is the list of possible password guesses.
+ unix_crypt_cracker.py: Legacy password cracker using weak Unix crypt hashing.
+ cryptWord.py: Generates SHA512 hashes for testing.
+ modern_password_cracker.py: Modern SHA512 password cracker.

3. Run the Legacy Unix Crypt Cracker: This script will attempt to crack the password using the legacy Unix crypt method:

```bash
python3 unix_crypt_cracker.py
```

4. Generate SHA512 Hash: Use this script to generate a SHA512 hash from a password:

```bash
python3 cryptWord.py
```
5. Run the Modern SHA512 Password Cracker: This script will hash each password guess in the dictionary.txt using the SHA512 algorithm and known salt:

```bash
python3 modern_password_cracker.py
```

Example Output
You should see something like this when running the modern password cracker:

```bash
[+] Cracking Password for: victim
[+] Found Password using crypt: egg

[+] Cracking Password for: root
[-] Password not found with crypt.crypt, trying sha512_crypt...

[+] Found Password using SHA-512: strawberry
```

#### Notes
+ Make sure the salt in password.txt matches the one used in modern_password_cracker.py.
+ You can add more password guesses to dictionary.txt to increase the chances of cracking the password.

## Workflow
1. Legacy Unix Crypt Cracker
In the legacy approach, the salt is derived from the first two characters of each word in dictionary.txt. This is fed into unix_crypt_cracker.py, which attempts to crack the passwords using poor salting practices.

```bash
python3 unix_crypt_cracker.py
```

2. SHA512 Password Cracker
In the modern approach, the cryptWord.py script is used to create SHA512 hashes for known passwords. Knowing the salt used, we can store the hashes in password.txt. Then, the modern_password_cracker.py is used to crack the password by hashing each word in the dictionary with the SHA512 algorithm.

```bash
python3 cryptWord.py
python3 modern_password_cracker.py
```

3. Comparison of Salting Practices
+ Legacy Unix Crypt: The salt is weak, as it uses only two characters from the password. This makes the system vulnerable to rainbow table attacks or dictionary attacks.
+ SHA512: The robust SHA512 algorithm produces a stronger hash with a more secure salt, significantly reducing the risk of password cracking via brute force or dictionary attacks.

Conclusion
This project showcases the risks of poor salting in password hashing and the improved security provided by robust hashing algorithms like SHA512. By comparing the two approaches, we demonstrate the importance of using secure hashing algorithms and properly implementing salts in password storage systems.
