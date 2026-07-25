import pyautogui as auto
import time
from dataclasses import dataclass
from sys import exit as getout


@dataclass
class sotelock:
    service: str
    passwd: str

password_db = [ #Write here your password and where to use it
    sotelock("Service1", "Password1"),
    sotelock("Service2", "Password2")
]

mail_db = [ #Write Hear your mail and for what you use it
    sotelock("EmailService1", "noreply@mail1.com"),
    sotelock("EmailService2", "noreply@mail2.com")
]

def writter(key: str):
    print("    You have 3 seconds to put your cursor where you want to write...")
    time.sleep(3)
    if "@" in key:
        name, domain = key.split("@", 1)
        auto.write(name)
        print("Write the @ Fast")
        time.sleep(2)
        auto.write(domain)
    else:
        auto.write(key)

patience = 5

def main(key=False):
    def lock(attempts = 3):
        global patience
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

        #Secret Password (Modify this strings as you want)
        print("    This program is not allowed to be used by anyone who is not 'User', so, I'll ask you a question that only Sotelo may know, if your answer is correct, then you shall use this program, however if you fail, then, you shan't use this app whatsoever")
        print("    Tell me, 'Who is the one that encorage 'User' to start programming'?")
        try:
            letra = str(input("    Response: "))
        except ValueError:
            if patience == 5:
                print("I can see you did not undertand the concept of a name, a name is a group of characters, principally letter, that enable us to refer to someone or someting, so write a name, please")
                input()
                patience = patience - 1
                lock(attempts=attempts)
            if patience == 4:
                print("Do you really think you're funny, because you're not, instead, you're merely pathetic, I cannot help but rejoice in the contempt I have for you")
                input()
                patience = patience - 1
                lock(attempts=attempts)
            if patience == 3:
                print("Huh, I just figured out, so, you're just mocking a program, that´s the pitiable thing you could do, Did you realise I do not have feelings?")
                input()
                patience = patience - 1
                lock(attempts=attempts)
            if patience == 2:
                print("Are you fucking stupid, I'm asking for a name, not a number, nor the fucking Fibonacci sequence")
                input()
                print("...")
                input()
                print("Ok, pardon me for my earlies modals, as an apology, let me give you another chance, don't fuck it")
                lock(attempts=attempts)
            if patience == 1:
                print("...")
                input()
                lock(attempts=attempts)                
            if patience == 0:
                print("OK, fuck off")
                input()
                getout()

        if letra == "e": #Example
            del letra
            main(True)
        else:
            if attempts > 0:
                if attempts == 3:
                    if patience == 5:
                        print("    Yield my code, to claim your errors")
                    else:
                        print("    I still belive you could be [user], maybe you're in haste")
                    input()
                elif attempts == 2:
                    print("    Ok, you're definely not [user], so, stop trying out to fell like a sorta hacker, 'coz you're actually not good at this whatsoever")
                    input()
                elif attempts == 1:
                    print("    Didn't gave up already, may I remind you this is your last chance to 'SOMEHOW FELL LIKE A CRACKER' for once on your entire life")
                    input()
                attempts = attempts - 1
                lock(attempts=attempts)
            else:
                print("    Somehow, I clearly knew you weren't able to fullfil your dreams of being some kinda cracker")
                quit()

    if key == False:
        lock()
    else:
        pass

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

    num = int(1)

    for num in range(5):
        print("")

    print("    Choose an option (Only type the NUMBER):")
    print("")
    print("    1.Mails/Emails")
    print("    2.Passwords")
    print("    3.Exit")
    print("")
    try:
        option = int(input("    Opcion: "))
        if option >= 4:
            print("    You stupid or something you can only use 3 numbers and you still failed, press enter and let us begin again")
            input()
            main(True)
    except ValueError:
        print("    You can only use numbers dumbass, press enter and let us begin again")
        input()
        main(True)

    if option == 1:
        print("\033[2J\033[3J\033[H")
        print("")
        print(banner)
        for (num) in range(5):
            print(end="")
        num = 0
        for num in range(len(mail_db)):
            print(f"    {num + 1}.{mail_db[num].service}")
        print(end="")
        try:
            option = int(input("    Option: "))
            if option > len(mail_db):
                return 1
            writter(mail_db[option - 1].passwd)
        except ValueError:
            print("    Fatal Error, Detected Lack Of Neurons, I'll grant you another chance tho you may not used as it is intended to")
            input()
            main(True)
        main(True)

    elif option == 2:
        print("\033[2J\033[3J\033[H")
        print(end="")
        print(banner)
        for (num) in range(5):
            print(end="")
        num = 0
        for num in range(len(password_db)):
            print(f"    {num + 1}.{password_db[num].service}")
        print("")
        try:
            option = int(input("    Option: "))
            if option > len(password_db):
                return 1
            writter(password_db[option - 1].passwd)
        except ValueError:
            print("    Fatal Error, Detected Lack Of Neurons, I'll grant you another chance tho you may not used as it is intended to")
            input()
            main(True)
        main(True)

    elif option == 3:
        print ("    Sayonara")
        getout()
main()
