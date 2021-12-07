from config.cipher import *
from getpass import getpass


def command(console_input=None, options=False):
    if options:
        console_output = input("\n$ (A)dd, (G)et, (E)dit, (D)el, (ALL), (Q)uit: ")
        return console_output
    console_output = input(f"$ {console_input}")
    return console_output


def Add():
    name = input("$ Name: ")
    user = input("$ Username / email: ")
    passwd = getpass("$ Password: ")
    url = input("$ URL: ")
    notes = input("$ Notes: ")
    return name, user, passwd, url, notes


def main():
    password = getpass("Please provide the master password: ")
    print("""
    
    ______    ______   _______      _____  ________
   /      \  /      \ /       \    /     |/        |
  /$$$$$$  |/$$$$$$  |$$$$$$$  |   $$$$$ |$$$$$$$$/
  $$ \__$$/ $$ \__$$/ $$ |  $$ |      $$ |$$ |__
  $$      \ $$      \ $$ |  $$ | __   $$ |$$    |
   $$$$$$  | $$$$$$  |$$ |  $$ |/  |  $$ |$$$$$/
  /  \__$$ |/  \__$$ |$$ |__$$ |$$ \__$$ |$$ |_____
  $$    $$/ $$    $$/ $$    $$/ $$    $$/ $$       |
   $$$$$$/   $$$$$$/  $$$$$$$/   $$$$$$/  $$$$$$$$/

        """)
    krypt0 = Cipher("./config/storage00.ssdje", password)
    print("S.S.D.J.E console v1.0, choose a command:\n")
    while True:
        choose = command(options=True)
        choose = choose.upper()
        if choose == "A" or choose == "ADD":
            name, user, passwd, url, notes = Add()
            krypt0.encrypt(name, user, passwd, url, notes, add=True)
        elif choose == "G" or choose == "GET":
            keyword = input("$ Name: ")
            passwd = krypt0.decrypt(keyword)
            if passwd:
                print(f"\nSuccessfully decrypted: {keyword}\n\n"
                      f"  |*| Username / Email = user\n"
                      f"  |*| Password = {passwd}\n"
                      f"  |*| Url = url\n"
                      f"  |*| Notes = notes\n")

            choose2 = input("$ Enter any key to go back, or (Q)uit: ")
            if choose2.upper() == "Q":
                exit()
            else:
                continue
        elif choose == "E" or choose == "EDIT":
            keyword = input("$ Name: ")
            try:
                krypt0.decrypt(keyword)
            except:
                print("CODE:667 PIPPO FATAL ERROR, Mismatch!\n")
                exit()
            name, user, passwd, url, notes = Add()
            krypt0.encrypt(name, user, passwd, url, notes, edit=True, old=keyword)
            print("\n Item  Name         Username         Password   Url\n"
                  " ----  -----------  ---------------  ---------  -------------\n")
            print(f"  {str(0).zfill(2)[:2]}"
                  f"    {str(name).ljust(12)[:12]}"
                  f" {str(user).ljust(14)[:14]}"
                  f"   *******    "
                  f"{url}\n")
            choose2 = input("$ Enter any key to go back, or (Q)uit: ")
            if choose2.upper() == "Q":
                exit()
            else:
                continue
        elif choose == "D" or choose == "DEL":
            keyword = input("$ Name: ")
            output = krypt0.del_json(keyword)
            if output:
                print(f"\nSuccessfully deleted: {keyword}\n")
            choose2 = input("$ Enter any key to go back, or (Q)uit: ")
            if choose2.upper() == "Q":
                exit()
            else:
                continue
        elif choose == "ALL":
            name, username, url = krypt0.show_all_json()
            print("\n Item  Name\n"
                  " ----  -----------\n")
            for count, value in enumerate(name):
                #if len(str(count)) < 2:  TODO: why I just put this line???
                print(f"  {str(count).zfill(2)[:3]}"
                      f"    {str(value).ljust(12)[:12]}")
            print("\n")
            choose2 = input("$ Enter any key to go back, or (Q)uit: ")
            if choose2.upper() == "Q":
                exit()
            else:
                continue
        elif choose == "Q" or choose == "QUIT":
            exit()
        else:
            print("CODE:444 Invalid input\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
