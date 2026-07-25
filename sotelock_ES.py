import pyautogui as auto
import time
from dataclasses import dataclass
from sys import exit as getout


@dataclass
class sotelock:
    service: str
    passwd: str

password_db = [ #Escribe aqui tus contraseñas y donde las usas
    sotelock("Servicio", "clave1"),
    sotelock("Service2", "clave")
]

mail_db = [ #Escribe aqui el correo de de que servicio es/donde lo usas/un identificativo
    sotelock("ServicioDeCorreo1", "noreply@mail1.com"),
    sotelock("ServicioDeCorreo2", "noreply@mail2.com")
]

def writter(key: str):
    print("    Tienes 3 segundos para poner el cursos donde sea que quieras escribir...")
    time.sleep(3)
    if "@" in key:
        name, domain = key.split("@", 1)
        auto.write(name)
        print("Escribe la @ rapido")
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
        print("    Este programa no esta permitido que sea usado por nadie mas que no sea 'User', por lo tanto, te hare una pregunta para verificar tu identidad, si la respuesta es correcta demostrara la veracidad de tus palabras y tendras permitido el acceso al programa, por otro lado, si fallas, entonces no se te negara el acceso por completo")
        print("    Entonces, responde a esta pregunta, ¿'Como Se llama la vecina loca'?")
        try:
            letra = str(input("    Respuesta: "))
        except ValueError:
            if patience == 5:
                print("Por lo que veo no comprendes el concepto de nombre, un nombre es un grupo de caracteres, principalmente letras, eso nos permite referirnos a personas u objetos, dicho esto, escribe un nombre, por favor")
                input()
                patience = patience - 1
                lock(attempts=attempts)
            if patience == 4:
                print("Realmente crees que eres gracioso, la respuesta es sencilla, no lo eres, al contrario, eres completamente patetico, no puedo hacer nada mas por ti a excepcion de regocijarme en el desprecio que siento hacia ti")
                input()
                patience = patience - 1
                lock(attempts=attempts)
            if patience == 3:
                print("Eh, Acabo de deducirlo, entonces, te estas burlando de un programa, es lo mas lamentable que podrias hacer. ¿Te das cuenta que no tengo sentimiento?")
                input()
                patience = patience - 1
                lock(attempts=attempts)
            if patience == 2:
                print("Eres tonto del culo o que te pasa, te estoy pidiendo un nombre, no un numero, ni la puta sucesión fibonachi")
                input()
                print("...")
                input()
                print("Vale, perdona mis modales mostrados con anterioridad, como disculpa, te dare otra oportunidad, no lo arruines")
                lock(attempts=attempts)
            if patience == 1:
                print("...")
                input()
                lock(attempts=attempts)
            if patience == 0:
                print("Jodete")
                input()
                getout()

        if letra == "e": #Ejemplo
            del letra
            main(True)
        else:
            attempts = attempts - 1
            if attempts > 0:
                if attempts == 3:
                    print("Aún creo que puedes ser [Usuario], puede que estes en un apuro, prueba otra vez")
                    input()
                if attempts == 2:
                    print("Vale, Definitivamente no eres [Usuario], entonces, deja de intentar sentirte como una especie de hacker, pues de hecho no eres bueno en esto en absoluto")
                    input()
                if attempts == 1:
                    print("Aún no te has rendido, deberia recordarte que esta es tu ultima oportunidad para 'SENTIRTE COMO UN CRACKER' for once on your entire life")
                    input()
                lock(attempts=attempts)
            else:
                print("    Por algún motivo, sabia claramente que no serias capaz de completar tu sueño de ser una especie de cracker")
                getout()

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

    print("    Elige una opcion (Solo un NUMERO):")
    print("")
    print("    1.Correos/Emails")
    print("    2.Contraseñas")
    print("    3.Cerrar")
    print("")
    try:
        option = int(input("    Opcion: "))
        if option >= 4:
            print("    Eres tonto o que te pasa, solo tienes opcion a elegir entre 3 opciones, y aun asi fallas, pulsa enter y comenzemos de nuevo")
            input()
            main(True)
    except ValueError:
        print("    Solo puedes usar numeros imbecil, pulsa enter y comenzemos de nuevo")
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
            option = int(input("    Opcion: "))
            if option > len(mail_db):
                return 1
            writter(mail_db[option - 1].passwd)
        except ValueError:
            print("    Error fatal, Se han detectado falta de neuronas en el usuario, te dare otra oportunidad aunque seguramente no la aproveches como es debido")
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
            option = int(input("    Opcion: "))
            if option > len(password_db):
                return 1
            writter(password_db[option - 1].passwd)
        except ValueError:
            print("    Error fatal, Se han detectado falta de neuronas en el usuario, te dare otra oportunidad aunque seguramente no la aproveches como es debido")
            input()
            main(True)
        main(True)

    elif num == 3:
        print ("    Sayonara")
        getout()
main()
