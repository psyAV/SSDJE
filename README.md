# S.S.D.J.E

S.S.D.J.E. (Secure Standard Double Json Encryption) is a secure way to store your passwords offline using a double encryption. The passwords will be saved in a storage.ssdje file readable as json file after the first layer is decrypted. After created a new file encrypted with your own password, this file can be decrypted using every keyword but only the person who know the password can decide if the file is decrypted in the correct way. This feature will prevent any kind of brute force attack because the file can be decrypted in infinite ways.
## Requirements:
* Python 3
* base64
* json
* hashlib
* cryptography
* getpass
## Feature list and usage:
* Add (A) => Add a new password
* Get (G) => Get your password 
* Edit (E) => Edit password, username, email etc..
* ALL => Display all your password stored
* Quit (q) => Leave the program
