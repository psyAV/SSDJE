from cryptography.fernet import Fernet
import base64
import hashlib
import json


def hash_sha256(value):
    hashed_value = hashlib.sha256(bytes(value, encoding="utf8")).digest()
    return hashed_value


class Cipher:
    def __init__(self, cipher_file, passwd):
        self.file = cipher_file
        self.passwd = bytes(passwd, encoding="utf8")
        self.key1 = base64.b64encode(hashlib.sha256(self.passwd).digest())
        self.key2 = base64.b64encode(hashlib.sha256(bytes(passwd[::-1], encoding="utf-8")).digest())
        self.encryption = Fernet(self.key1)
        self.ssjde_encryption = Fernet(self.key1)

    def add_json(self, name, user, ciphertext, url, notes):
        data = {str(name): {"user": str(user), "passwd": str(ciphertext), "url": str(url), "notes": str(notes)}}
        json_cipher_text = self.SSDJE_encryption()
        try:
            content = json.loads(json_cipher_text)
        except:
            print("CODE:667 PIPPO FATAL ERROR, Mismatch!\n")
            exit()
            return False
        content.update(data)
        with open(self.file, "w") as json_file:
            json.dump(content, json_file)
        self.SSDJE_encryption(json_file=True)
        return True

    def edit_json(self, old, name, user, ciphertext, url, notes):
        try:
            self.del_json(old)
            data = {str(name): {"user": str(user), "passwd": str(ciphertext), "url": str(url), "notes": str(notes)}}
            json_cipher_text = self.SSDJE_encryption()
            content = json.loads(json_cipher_text)
        except:
            print("CODE:667 PIPPO FATAL ERROR, Mismatch!\n")
            exit()
            return False
        content.update(data)
        with open(self.file, "w") as json_file:
            json.dump(content, json_file)
        self.SSDJE_encryption(json_file=True)
        return True

    def del_json(self, name):
        json_cipher_text = self.SSDJE_encryption()
        try:
            content = json.loads(json_cipher_text)
        except:
            print("CODE:667 PIPPO FATAL ERROR, Mismatch!\n")
            exit()
            return False
        try:
            content.pop(name)
        except:
            print("CODE:444 Invalid input\n")
            return False
        with open(self.file, "w") as json_file:
            json.dump(content, json_file)
        self.SSDJE_encryption(json_file=True)
        return True

    def show_all_json(self):
        json_cipher_text = self.SSDJE_encryption()
        try:
            content = json.loads(json_cipher_text)
        except:
            print("CODE:667 PIPPO FATAL ERROR, Mismatch!\n")
            exit()
            return False
        name = []
        username = []
        url = []
        for count, value in enumerate(content):
            name.append(value)
            username.append(content[name[count]]["user"])
            url.append(content[name[count]]["url"])
        return name, username, url

    def SSDJE_encryption(self, json_file=False):
        """S.S.D.J.E. (Standard Secure Double Json Encryption)"""
        if json_file:
            with open(self.file, "r") as ssjde:
                ciphertext = ssjde.read()
            cipher_json_text = self.ssjde_encryption.encrypt(ciphertext.encode())
            with open(self.file, "w") as ssjde:
                ssjde.write(cipher_json_text.decode())
            return cipher_json_text
        else:
            with open(self.file, "r") as ssjde:
                cipher_json_text = ssjde.read()
            try:
                ciphertext = self.ssjde_encryption.decrypt(cipher_json_text.encode())
                return ciphertext
            except:
                return None

    def encrypt(self, name, user, passwd, url, notes, add=False, edit=False, old=None):
        ciphertext = self.encryption.encrypt(passwd.encode())
        if ciphertext is not None:
            if add:
                self.add_json(name, user, ciphertext, url, notes)
            if edit:
                self.edit_json(old, name, user, ciphertext, url, notes)

    def decrypt(self, name):
        json_cipher_text = self.SSDJE_encryption()
        if json_cipher_text:
            content = json.loads(json_cipher_text)
            try:
                plaintext = self.encryption.decrypt(content[name]["passwd"][2:-1].encode())
                return plaintext.decode()
            except KeyError as e:
                print(f"CODE:871 KeyError: {e} doesn't exist, insert a valid keyword!\n")
                return False
        else:
            return print("Decryption failed! Leaving the program...")


example = Cipher("storage.ssdje", "pippo2451")
# ---------------- Examples ----------------
# example = Cipher("example.ssdje", "master_passwd_example") <== To crate the Cipher object.
# It requires the file path and the master password.
# The master password will not be saved in any document.
# Don't forget your master password or all your data will be lost
#
# ---------------- Function decrypt ----------------
# example.encrypt("name", "user", "password", "https://example.org/", "some notes") <== To store passwords
#
# ---------------- Function encrypt ----------------
# example.decrypt("name") <== To decrypt your passwords
