# S.S.D.J.E

S.S.D.J.E. (Secure Standard Double Json Encryption) is a safe way to store your passwords 100% offline using a double encryption. Your keys will be saved in a storage.ssdje file readable as json file after the first layer is decrypted. Once a new file is created and encrypted with your masterpassord, It can be decrypted in infinite ways but only the person who know the masterpassword will decrypted correctly. This feature will prevent any kind of brute force attack because the sowftware won't tell you if the typed password is wrong or not.

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
