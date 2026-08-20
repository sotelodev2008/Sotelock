import database
import pyautogui as auto
from time import sleep as stop
from sys import exit as getout
from sys import argv
from getpass import getuser
from getpass import getpass
from random import choice

database.comprobation()

def access():
    if database.access() == None:
        for i in range(3):
            access_passwd = input("Create a access password: ")
            access_conf = input("Confirm your access password: ")
            if access_passwd != access_conf:
                print("You have miswritten the confirmation password")
            else:
                database.access_registration(access_passwd)
                break
    else:
        pass

class sotelock:
    def __init__(self, passwd = None):
        try:
            if passwd is None:
                passwd = argv[1] == database.access()
        except IndexError:
            self.passwd = False
        self.passwd = passwd
        self.patience = 5
        self.attempts = 3

    def sotelo(self, text, url):
        link_s = "\033]8;;" # Start a sequence in the OS, the 8 means that the sequence is a LINK
        delimiter = "\033\\" # Tell to the terminal that the following text will be visible
        link_e = "\033]8;;\033\\" # Tells the terminal that the sequence have already ended
        blue = "\033[34m" # Tells the terminal to output text in blue
        reset = "\033[0m" # Reset the terminal output color
        color = f"{blue}{text}{reset}"

        return f"{link_s}{url}{delimiter}{color}{link_e}"

    def writter(self, key: str):
        print("    You have 3 seconds to put your cursor where you want to write...")
        stop(3)
        if "@" in key:
            name, domain = key.split("@", 1)
            auto.write(name)
            print("Write the @ Fast")
            stop(2)
            auto.write(domain)
        else:
            auto.write(key)
        profile = self.sotelo("Sotelo", "https://github.com/sotelodev2008")
        print(f"    Thanks for using Sotelock! Developed by {profile}. If you liked it, please consider supporting my work.")
        getout()

    def lock(self):
        print("\033[2J\033[3J\033[H")
        print(end="")


        print("""                                                                                                                                                  

                            ██████████████████
                            ██████████████████
                            ██████████████████
                        ████████████      ████████████
                        ████████████      ████████████
                        ████████████      ████████████
                        ██████                  ██████
                        ██████                  ██████
                        ██████                  ██████
                        ██████
                        ██████
                        ██████
                  ▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                  ██████████████████████████████████████████
                  ██████████████████████████████████████████
                  ██████████████████████████████████████████
                  ██████████████████████████████████████████
                  ██████████████████████████████████████████
                  ██████████████████      ██████████████████
                  ██████████████████      ██████████████████
                  ██████████████████      ██████████████████
                  ██████████████████      ██████████████████
                  ██████████████████      ██████████████████
                  ██████████████████      ██████████████████
                        ██████████████████████████████
                        ██████████████████████████████
                        ██████████████████████████████
                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                                                                                                                       
        """)

        print(end="")

        print(f"    This program is not allowed to be used by anyone who is not {getuser()}, so, I'll ask you a question that only {getuser()} may know, if your answer is correct, then you shall use this program, however if you fail, then, you shan't use this app whatsoever")
        print(f"    Tell me, What is {getuser()} access password for Sotelock?")
        try:
            letra = str(input("    Response: "))
        except ValueError:
            if self.patience == 5:
                print("I can see you did not understand the concept of a password, a password is a group of characters, principally letter, that keep something secure, so write a password with letters, not only numbers, please")
                input()
                self.patience = self.patience - 1
                self.lock()
            if self.patience == 4:
                print("Do you really think you're funny, because you're not, instead, you're merely pathetic, I cannot help but rejoice in the contempt I have for you")
                input()
                self.patience = self.patience - 1
                self.lock()
            if self.patience == 3:
                print("Huh, I just figured out, so, you're just mocking a program, that´s the pitiable thing you could do, Did you realise I do not have feelings?")
                input()
                self.patience = self.patience - 1
                self.lock()
            if self.patience == 2:
                print("Are you fucking stupid, I'm asking for a password, not a number, nor the fucking Fibonacci sequence")
                input()
                print("...")
                input()
                print("Ok, pardon me for my earlier manners, as an apology, let me give you another chance, don't fuck it")
                self.patience = self.patience - 1
                self.lock()
            if self.patience == 1:
                print("...")
                input()
                self.patience = self.patience - 1
                self.lock()
            if self.patience == 0:
                print("OK, fuck off")
                input()
                getout()

        if letra == database.access():
            self.passwd = True
            pass
        else:
            if self.attempts > 0:
                if self.attempts == 3:
                    print(f"    Perhaps you're just having a rough day, {getuser()}?\nMaybe you're in haste")
                    input()
                elif self.attempts == 2:
                    print(f"    Your performance is as disappointing as my compile times.\nSo, stop trying out to feel like a sorta hacker, 'coz you're actually not good at this whatsoever")
                    input()
                elif self.attempts == 1:
                    print("    Persistence is admirable, but you're wasting both our time.\nMay I remind you this is your last chance to 'SOMEHOW FEEL LIKE A HACKER' for once on your entire life")
                    input()
                self.attempts = self.attempts - 1
                self.lock()
            else:
                print(choice(["    Somehow, I clearly knew you weren't able to fullfil your dreams of being some kinda hacker", "    Access denied. Your hacker career ends here.", "That's enough. Go outside and touch some grass."]))
                getout()
    def main(self):
        if not self.passwd:
            self.lock()
        
        print("\033[2J\033[3J\033[H")
        print(end="")

        banner= """    ::······::::·······::::::··:::::········::········:::·······::::······:::··::::··::
        ::'######:::'#######::'########:'########:'##::::::::'#######:::'######::'##:::'##:
        :'##... ##:'##.... ##:... ##..:: ##.....:: ##:::::::'##.... ##:'##... ##: ##::'##::
        : ##:::..:: ##:::: ##:::: ##:::: ##::::::: ##::::::: ##:::: ##: ##:::..:: ##:'##:::
        :. ######:: ##:::: ##:::: ##:::: ######::: ##::::::: ##:::: ##: ##::::::: #####::::
        ::..... ##: ##:::: ##:::: ##:::: ##...:::: ##::::::: ##:::: ##: ##::::::: ##. ##:::
        :'##::: ##: ##:::: ##:::: ##:::: ##::::::: ##::::::: ##:::: ##: ##::: ##: ##:. ##::
        :. ######::. #######::::: ##:::: ########: ########:. #######::. ######:: ##::. ##:
        ::......::::.......::::::..:::::........::........:::.......::::......:::..::::..::"""

        print(banner)

        for i in range(5):
            print("")

        print("    Choose an option (Only type the NUMBER):")
        print("")
        print("    1. Mails/Emails")
        print("    2. Passwords")
        print("    3. Exit")
        print("")

        try:
            option = int(input("    Option: "))
            if option >= 4:
                print("    You stupid or something you can only use 3 numbers and you still failed, press enter and let us begin again")
                input()
                self.main()
            elif option == 0:
                print(f"    Heh heh, you really thought I would discard the posibility a user type zero just to found bugs, sorry, you won´t, 'coz this have just been patched because of you, so called {getuser()}")
                input()
                self.main()
        except ValueError:
            print("    You can only use numbers dumbass, press enter and let us begin again")
            input()
            self.main()

        if option == 1:
        
            print("\033[2J\033[3J\033[H")
            print(end="")
            print(banner)

            for i in range(5):
                print("")

            print("    Choose an option (Only type the NUMBER):")
            print("")
            print("    1. Get Email")
            print("    2. Add Email")
            print("    3. Delete Email")
            print("")
            try:
                option = int(input("    Option: "))
                if option >= 4:
                    print("    You stupid or something you can only use 3 numbers and you still failed, press enter and let us begin again")
                    input()
                    self.main()
                elif option == 0:
                    print(f"    Heh heh, you really thought I would discard the posibility a user type zero just to found bugs, sorry, you won´t, 'coz this have just been patched because of you, so called {getuser()}")
                    input()
                    self.main()
            except ValueError:
                print("    You can only use numbers dumbass, press enter and let us begin again")
                input()
                self.main()
            print("\033[2J\033[3J\033[H")
            print("")
            print(banner)
            for i in range(5):
                print("")
            if option == 1:
                num = 1
                number, services = database.count_mails()
                for i in range (number):
                    print(f"    {num}. {services[num-1]}")
                    num += 1 # Sum 1 to num
                print("")
                try:
                    option = int(input("    Option: "))
                    service_name = services[option - 1]
                    if option > number:
                        print(f"    You stupid or something you can only use {number} numbers and you still failed, press enter and let us begin again")
                        input()
                        self.main()
                    elif option == 0:
                        print(f"    Heh heh, you really thought I would discard the posibility a user type zero just to found bugs, sorry, you won´t, 'coz this have just been patched because of you, so called {getuser()}")
                        input()
                        self.main()
                except ValueError:
                    print("    You can only use numbers dumbass, press enter and let us begin again")
                    input()
                    self.main()
                self.writter(database.get_mail(service_name))
            if option == 2:
                print("    All right, write here the service where you use your mail, you can also write a name or hint to know which mail is that")
                service = input("    Service: ")

                print("\n", end=f"    Now, write the mail you used in/that reminds you to {service}")
                mail = str(getpass("    Mail: "))

                print("\n", end="    Now, repeat the mail to confirm that you really write it correctly")
                print("    You got 3 attempts (Note: invisible typing enabled)")

                self.attempts = 3

                while self.attempts != 0:
                    mail_confirmation = str(getpass("    Confirmation: "))

                    if mail == mail_confirmation:
                        database.mail_db(service, mail)
                        print("    The mail have been correctly added to the database")
                        input()
                        self.main()
                    elif mail != mail_confirmation:
                        self.attempts -= 1 # substract 1 to the attemps
                        print(f"    The confirmation does not match with the mail you gave us")
                        continue
                else:
                    print("    At this rate it is better for you to start again, so, the program will shut down")
                    getout()
            if option == 3:
                num = 1
                number, services = database.count_mails()
                for i in range (number):
                    print(f"    {num}. {services[num-1]}")
                    num += 1 # Sum 1 to num
                print("\n", end="    Choose a service to delete from the database\n")
                try:
                    option = int(input("    Option: "))
                    if option > number:
                        print(f"    You stupid or something you can only use {number} numbers and you still failed, press enter and let us begin again")
                        input()
                        self.main()
                    elif option == 0:
                        print(f"    Ah, the classic 'let's break the program with zero' attempt. Pathetic.")
                        print("    That error was similar to a blunder, so as a punishment, you'll have to begin again")
                        input()
                        self.main()
                except ValueError:
                    print("    You can only use numbers dumbass, press enter and let us begin again")
                    input()
                    self.main()
                sure = input("    Are you completely sure? (y/n): ")
                if sure == "y":
                    database.del_mails(option)
                    print("    The service have been correctly deleted")
                    input()
                    self.main()
                else:
                    print("OK, Don't worry, repenting is normal")
                    input()
                    main()
        if option == 2:
            print("\033[2J\033[3J\033[H")
            print("")
            print(banner)

            for i in range(5):
                print("")

            print("    Choose an option (Only type the NUMBER):")
            print("")
            print("    1. Get Password")
            print("    2. Add Password")
            print("    3. Delete Password")
            print("")

            try:
                option = int(input("    Option: "))
                if option >= 4:
                    print("    You stupid or something you can only use 3 numbers and you still failed, press enter and let us begin again")
                    input()
                    self.main()
                elif option == 0:
                    print(f"    Heh heh, you really thought I would discard the posibility a user type zero just to found bugs, sorry, you won´t, 'coz this have just been patched because of you, so called {getuser()}")
                    input()
                    self.main()
            except ValueError:
                print("    You can only use numbers dumbass, press enter and let us begin again")
                input()
                self.main()
            print("\033[2J\033[3J\033[H")
            print("")
            print(banner)
            for i in range(5):
                print("")

            if option == 1:
                num = 1
                number, services = database.count_passwords()
                for i in range (number):
                    print(f"    {num}. {services[num-1]}")
                    num += 1 # Sum 1 to num
                print("")
                try:
                    option = int(input("    Option: "))
                    service_name = services[option - 1]
                    if option > number:
                        print(f"    You stupid or something you can only use {number} numbers and you still failed, press enter and let us begin again")
                        input()
                        self.main()
                    elif option == 0:
                        print(f"    Ah, the classic 'let's break the program with zero' attempt. Pathetic.")
                        input()
                        self.main()
                except ValueError:
                    print("    You can only use numbers dumbass, press enter and let us begin again")
                    input()
                    self.main()
                self.writter(database.get_password(service_name))
            if option == 2:
                print("    All right, write here the service where you use your password, you can also write a name or hint to know which password is that")
                service = input("    Service: ")

                print("\n", end=f"    Now, write the password you used in/that reminds you to {service}")
                passwd = str(getpass("    Password: "))

                print("\n", end="    Now, repeat the password to confirm that you really write it correctly")
                print("    You got 3 attempts (Note: invisible typing enabled)")

                self.attempts = 3

                while self.attempts != 0:
                    passwd_confirmation = str(getpass("    Confirmation: "))

                    if passwd == passwd_confirmation:
                        database.password_db(service, passwd)
                        print("    The password have been correctly added to the database")
                        input()
                        self.main()
                    elif passwd != passwd_confirmation:
                        self.attempts -= 1 # substract 1 to the attemps
                        print(f"    The confirmation does not match with the password you gave us")
                        input()
                        continue
                else:
                    print("    At this rate it is better for you to start again, so, the program will shut down")
                    getout()
            if option == 3:
                num = 1
                number, services = database.count_passwords()
                for i in range (number):
                    print(f"    {num}. {services[num-1]}")
                    num += 1 # Sum 1 to num
                print("\n", end="    Choose a service to delete from the database\n")
                try:
                    option = int(input("    Option: "))
                    if option > number:
                        print(f"    You stupid or something you can only use {number} numbers and you still failed, press enter and let us begin again")
                        input()
                        self.main()
                    elif option == 0:
                        print(f"    Ah, the classic 'let's break the program with zero' attempt. Pathetic.")
                        print("    That error was similar to a blunder, so as a punishment, you'll have to begin again")
                        input()
                        self.main()
                except ValueError:
                    print("    You can only use numbers dumbass, press enter and let us begin again")
                    input()
                    self.main()
                sure = input("    Are you completely sure? (y/n): ")
                if sure == "y":
                    database.del_passwords(option)
                    print("    The service have been correctly deleted")
                    input()
                    self.main()
                else:
                    print("OK, Don't worry, repenting is normal")
                    input()
                    main()
        if option == 3:
            profile = self.sotelo("Github profile", "https://github.com/sotelodev2008")
            print(f"    If you wanna, and you have time, check out my {profile}")
            print("    ttyl, i guess...")
            getout()

if len(argv) <= 1:
    sol = sotelock()
elif len(argv) == 2:
    sol = sotelock(argv[1])
else:
    print("If you want to write arguments, you can only write one.") # Opción por defecto si ejecutas solo "python archivo.py"
    getout()

try:
    access()
except Exception as e:
    print("error")
try:
    sol.main()
except KeyboardInterrupt:
    print("\n    Stopped Correctly")
except RecursionError:
    print("\n    Yo, Gimme a break, I have opened a total of 1000 functions, wait dunno, 1 minute")
