from passlib.hash import sha512_crypt

# Define the plaintext password
password = "strawberry"

# Define a valid custom salt for sha512_crypt (16 characters, valid format)
custom_salt = "abc123XYZ789.pq"

# Hash the password using the custom salt
hashed_password = sha512_crypt.hash(password, salt=custom_salt)

# Print the resulting hash
print(hashed_password)
