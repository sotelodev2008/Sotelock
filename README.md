# Sotelock - Escribe contraseñas automáticamente / Auto-type your passwords

**🇪🇸 [Ver en Español](#guía-en-español)** | **🇬🇧 [See in English](#guide-in-english)**

---

## Índice Rápido / Quick Index

### 🇪🇸 Español
- [¿Qué es esto?](#qué-es-esto-español)
- [Para usuarios de Windows](#guía-para-windows-español)
- [Para usuarios de Linux](#guía-para-linux-español)
- [Configurar tus contraseñas](#configurar-tus-contraseñas-español)
- [Cómo usarlo](#cómo-usarlo-español)
- [Seguridad básica](#seguridad-básica-español)

### 🇬🇧 English
- [What is this?](#what-is-this-english)
- [For Windows users](#guide-for-windows-english)
- [For Linux users](#guide-for-linux-english)
- [Set up your passwords](#set-up-your-passwords-english)
- [How to use it](#how-to-use-it-english)
- [Basic security](#basic-security-english)

---

## Guía en Español

### ¿Qué es esto? (Español)

Es como un bloc de notas secreto que escribe por ti. Guardas tus contraseñas dentro, y cuando las necesitas, el programa las escribe solo en la pantalla. Así no tienes que memorizarlas ni escribirlas a mano donde alguien pueda verlas.

---

### Guía para Windows (Español)

#### Lo que necesitas antes de empezar

1. **Python** (el programa que hace funcionar esto)
   - Ve a: https://www.python.org/downloads/
   - Descarga la última versión
   - Al instalar, **marca la casilla que dice "Add Python to PATH"** (es muy importante)
   - Dale a "Install Now"

2. El archivo `sotelock.py` (el script que te descargaste)

#### Paso 1: Abrir la terminal (Windows)

La terminal es una ventana negra donde escribes comandos.

- Presiona la tecla `Windows` + `R`
- Escribe `cmd` y dale a Enter
- Se abrirá una ventana negra

#### Paso 2: Instalar lo que necesita el programa

En la ventana negra escribe:
```bash
pip install pyautogui
Si te dice que no encuentra pip, prueba:

bash
python -m pip install pyautogui
Espera a que termine (verás que deja de parpadear el cursor).

Guía para Linux (Español)
Lo que necesitas antes de empezar
Python (normalmente ya viene instalado en Linux)

Para comprobarlo, abre la terminal y escribe: python3 --version
Si te muestra un número (ej: 3.8.10), ya lo tienes
Si no, busca en tu gestor de paquetes "python3" e instálalo
El archivo sotelock.py

Paso 1: Abrir la terminal (Linux)
Busca "Terminal" en tu menú de aplicaciones, o
Presiona Ctrl + Alt + T (en la mayoría de distribuciones)
Paso 2: Instalar lo que necesita el programa
En la terminal escribe:

bash
pip3 install pyautogui
O si eso no funciona, prueba:

bash
sudo apt install python3-pip
pip3 install pyautogui
En algunas distribuciones (como Fedora) puede ser:

bash
sudo dnf install python3-pip
pip3 install pyautogui
Configurar tus contraseñas (Español)
Abre el archivo sotelock.py:

Windows: Clic derecho → "Abrir con" → Bloc de notas (o Notepad++)
Linux: Clic derecho → "Abrir con" → Editor de texto, o en terminal: nano sotelock.py
Busca estas partes y cambialas por tus datos:

Para contraseñas:

python
password_db = [
    sotelock("Netflix", "aquí pones tu contraseña"),
    sotelock("Gmail", "aquí pones otra"),
]
Para correos:

python
mail_db = [
    sotelock("Mi Correo", "tuemail@gmail.com"),
]
La pregunta secreta:
Busca esta línea y cambia la "e" por tu respuesta secreta:

python
if letra == "e":
También cambia la pregunta que está unas líneas arriba.

Guarda el archivo (Ctrl + S).

Cómo usarlo (Español)
En Windows:
Busca el archivo sotelock.py en tu carpeta
Haz doble clic en él (o clic derecho → "Abrir con Python")
Si se abre y se cierra rápido, abre la terminal, escribe cd (con espacio), arrastra la carpeta donde está el archivo a la terminal, y dale a Enter. Luego escribe: python sotelock.py
En Linux:
Abre la terminal
Ve a la carpeta donde está el archivo:
bash
cd /ruta/a/la/carpeta
(Puedes arrastrar la carpeta a la terminal después de escribir cd )
Dale permisos de ejecución (solo la primera vez):
bash
chmod +x sotelock.py
Ejecútalo:
bash
python3 sotelock.py
Una vez abierto:
Contesta la pregunta secreta
Verás un menú:
Pulsa 1 para un correo
Pulsa 2 para una contraseña
Pulsa 3 para salir
Elige cuál quieres (poniendo su número)
¡Rápido! Tienes 3 segundos para poner el ratón donde quieras escribir (ej: la casilla de contraseña de una web)
El programa escribe solo
Sobre el @: Cuando elijas un correo, escribe la parte antes del @, se para y tú debes escribir la @ manualmente (es por seguridad). Luego sigue solo.

Seguridad básica (Español)
⚠️ IMPORTANTE:

No subas este archivo a Internet (GitHub, Drive, etc.) con tus contraseñas reales
Las contraseñas se guardan en texto plano (cualquiera que abra el archivo las ve)
Mantén el archivo solo en tu computadora
En Linux, puedes hacer el archivo privado: chmod 600 sotelock.py (solo tú podrás leerlo)
Guide in English
What is this? (English)
It's like a secret notepad that types for you. You store your passwords inside, and when you need them, the program types them automatically on your screen. This way you don't have to memorize them or type them manually where someone might see.

Guide for Windows (English)
What you need before starting
Python (the program that makes this work)

Go to: https://www.python.org/downloads/
Download the latest version
When installing, check the box that says "Add Python to PATH" (very important)
Click "Install Now"
The file sotelock.py (the script you downloaded)

Step 1: Open the terminal (Windows)
The terminal is a black window where you type commands.

Press Windows key + R
Type cmd and press Enter
A black window will open
Step 2: Install what the program needs
In the black window type:

bash
pip install pyautogui
If it says it can't find pip, try:

bash
python -m pip install pyautogui
Wait until it finishes (you'll see the cursor stops blinking).

Guide for Linux (English)
What you need before starting
Python (usually already installed on Linux)

To check, open terminal and type: python3 --version
If it shows a number (e.g., 3.8.10), you have it
If not, search for "python3" in your package manager and install it
The file sotelock.py

Step 1: Open the terminal (Linux)
Search for "Terminal" in your applications menu, or
Press Ctrl + Alt + T (works on most distributions)
Step 2: Install what the program needs
In the terminal type:

bash
pip3 install pyautogui
Or if that doesn't work, try:

bash
sudo apt install python3-pip
pip3 install pyautogui
On some distributions (like Fedora) it might be:

bash
sudo dnf install python3-pip
pip3 install pyautogui
Set up your passwords (English)
Open the file sotelock.py:

Windows: Right click → "Open with" → Notepad (or Notepad++)
Linux: Right click → "Open with" → Text Editor, or in terminal: nano sotelock.py
Find these sections and change them to your data:

For passwords:

python
password_db = [
    sotelock("Netflix", "your password here"),
    sotelock("Gmail", "another password here"),
]
For emails:

python
mail_db = [
    sotelock("My Email", "youremail@gmail.com"),
]
The secret question:
Find this line and change "e" to your secret answer:

python
if letra == "e":
Also change the question a few lines above.

Save the file (Ctrl + S).

How to use it (English)
On Windows:
Find the file sotelock.py in your folder
Double-click it (or right-click → "Open with Python")
If it opens and closes quickly, open terminal, type cd (with space), drag the folder where the file is to the terminal, and press Enter. Then type: python sotelock.py
On Linux:
Open the terminal
Go to the folder where the file is:
bash
cd /path/to/folder
(You can drag the folder to the terminal after typing cd )
Give it execution permission (only first time):
bash
chmod +x sotelock.py
Run it:
bash
python3 sotelock.py
Once it's open:
Answer the secret question
You'll see a menu:
Press 1 for an email
Press 2 for a password
Press 3 to exit
Choose which one you want (by typing its number)
Quick! You have 3 seconds to move your mouse where you want it to type (e.g., the password box of a website)
The program types automatically
About the @ symbol: When you choose an email, it types the part before the @, stops and you must type the @ manually (security reason). Then it continues automatically.

Basic Security (English)
⚠️ IMPORTANT:

Don't upload this file to the Internet (GitHub, Drive, etc.) with your real passwords inside
Passwords are stored in plain text (anyone opening the file can see them)
Keep the file only on your computer
On Linux, you can make the file private: chmod 600 sotelock.py (only you can read it)
<div align="center">
¿Problemas? / Having issues?

Windows: Asegúrate de marcar "Add Python to PATH" al instalar / Make sure you checked "Add Python to PATH" when installing

Linux: Si pip3 no existe, instala python3-pip desde tu gestor de paquetes / If pip3 doesn't exist, install python3-pip from your package manager

</div> ```
