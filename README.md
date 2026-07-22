Markdown
# Sotelock - Auto-escritor de Contraseñas / Password Auto-typer

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Windows%20%7C%20Linux-lightgrey.svg)]()

</div>

---

## ¿Qué es esto? / What is this?

**🇪🇸 Español:** Es como un bloc de notas secreto que escribe por ti. Guardas tus contraseñas y correos dentro, y cuando los necesitas, el programa los escribe solo en la pantalla. Así no tienes que memorizarlos ni escribirlos a mano donde alguien pueda verlos.

**🇬🇧 English:** It's like a secret notepad that types for you. You store your passwords and emails inside, and when you need them, the program types them automatically on screen. This way you don't have to memorize them or type them manually where someone might see.

---

## 📑 Índice / Table of Contents

**Contenido en Español:**
- [Requisitos](#requisitos)
- [Instalación](#instalación)
  - [Windows](#windows-instalación)
  - [Linux](#linux-instalación)
- [Configuración](#configuración)
- [Cómo usar](#cómo-usar)
  - [Windows](#windows-uso)
  - [Linux](#linux-uso)
- [Seguridad](#seguridad)

**English Content:**
- [Requirements](#requirements)
- [Installation](#installation)
  - [Windows](#windows-installation)
  - [Linux](#linux-installation)
- [Configuration](#configuration)
- [How to Use](#how-to-use)
  - [Windows](#windows-usage)
  - [Linux](#linux-usage)
- [Security](#security)

---

<!-- ================================================== -->
<!-- TODO EL CONTENIDO EN ESPAÑOL A PARTIR DE AQUÍ -->
<!-- ================================================== -->

# 📘 Guía Completa en Español

## Requisitos

Necesitas dos cosas antes de empezar:

1. **Python** (el programa que hace funcionar este script)
2. **El archivo `sotelock.py`** (descargado en tu computadora)

## Instalación

### Windows (Instalación)

1. **Descarga Python:**
   - Ve a: https://www.python.org/downloads/
   - Descarga la última versión
   - **Importante:** Al instalar, marca la casilla que dice **"Add Python to PATH"**
   - Dale a "Install Now"

2. **Instala las dependencias:**
   - Presiona la tecla `Windows` + `R`
   - Escribe `cmd` y dale a Enter (se abre una ventana negra)
   - Escribe este comando y espera:
     ```bash
     pip install pyautogui
     ```
   - Si te da error, prueba:
     ```bash
     python -m pip install pyautogui
     ```

### Linux (Instalación)

1. **Verifica si tienes Python:**
   - Abre la terminal (busca "Terminal" en tu menú o presiona Ctrl + Alt + T)
   - Escribe:
     ```bash
     python3 --version
     ```
   - Si te muestra un número (ej: 3.8.10), ya lo tienes. Si no, instálalo desde tu gestor de paquetes.

2. **Instala las dependencias:**
   - En la terminal escribe:
     ```bash
     pip3 install pyautogui
     ```
   - Si pip3 no existe, instálalo primero:

     **Ubuntu/Debian:**
     ```bash
     sudo apt install python3-pip
     pip3 install pyautogui
     ```

     **Fedora/CentOS:**
     ```bash
     sudo dnf install python3-pip
     pip3 install pyautogui
     ```

     **Arch:**
     ```bash
     sudo pacman -S python-pip
     pip3 install pyautogui
     ```

## Configuración

Abre el archivo `sotelock.py` con cualquier editor de texto:
- **Windows:** Clic derecho → "Abrir con" → Bloc de notas
- **Linux:** Clic derecho → "Abrir con" → Editor de texto, o en terminal: `nano sotelock.py`

### Paso 1: Pon tus contraseñas
Busca esta sección y cambia los ejemplos por tus datos reales:

```python
password_db = [
    sotelock("Netflix", "aquí pones tu contraseña"),
    sotelock("Gmail", "aquí pones otra contraseña"),
    sotelock("Banco", "tu_clave_secreta"),
]
Paso 2: Pon tus correos
Busca esta sección y haz lo mismo:

Python
mail_db = [
    sotelock("Personal", "tuemail@gmail.com"),
    sotelock("Trabajo", "trabajo@empresa.com"),
]
Paso 3: Cambia la pregunta secreta
Busca esta línea:

Python
if letra == "e":
Cambia la "e" por tu respuesta secreta. Por ejemplo, si pones "madrid", tendrás que escribir madrid para entrar.

También cambia la pregunta que está unas líneas arriba:

Python
print("    Entonces, responde a esta pregunta, ¿'Cómo se llama tu perro'?")
Guarda el archivo (Ctrl + S).

Cómo usar
Windows (Uso)
Abre la carpeta donde guardaste sotelock.py

Haz doble clic en el archivo

Si se abre y se cierra rápido, haz esto:

Abre la terminal (Windows + R, escribe cmd)

Escribe cd (con un espacio al final)

Arrastra la carpeta donde está el archivo a la ventana negra

Dale a Enter

Escribe: python sotelock.py

Linux (Uso)
Abre la terminal

Ve a la carpeta donde está el archivo:

Bash
cd /ruta/a/la/carpeta
(Puedes escribir cd y arrastrar la carpeta a la terminal)

Dale permisos de ejecución (solo la primera vez):

Bash
chmod +x sotelock.py
Ejecuta el programa:

Bash
python3 sotelock.py
Una vez abierto el programa:
Responde la pregunta secreta (la que configuraste antes)

Verás un menú:

Pulsa 1 para escribir un correo

Pulsa 2 para escribir una contraseña

Pulsa 3 para salir

Elige cuál quieres escribir (poniendo su número y dando a Enter)

¡Rápido! Tienes 3 segundos para poner el ratón donde quieras que escriba (por ejemplo, en la casilla de contraseña de una página web)

El programa escribe automáticamente

Sobre el símbolo @ en los correos
Cuando eliges un correo, el programa escribe la parte antes del @, se detiene y te pide que escribas tú la @ manualmente. Esto es normal y es por seguridad. Tú escribes la @ y él sigue con el resto (gmail.com, etc.).

Seguridad
⚠️ IMPORTANTE - Lee esto:

No subas este archivo a Internet (GitHub, Google Drive, etc.) con tus contraseñas reales dentro

Las contraseñas se guardan en texto plano: cualquiera que abra el archivo puede leerlas

Mantén el archivo solo en tu computadora personal

En Linux: Puedes proteger el archivo para que solo tú puedas leerlo:

Bash
chmod 600 sotelock.py
📗 Complete Guide in English
Requirements
You need two things before starting:

Python (the program that makes this script work)

The file sotelock.py (downloaded on your computer)

Installation
Windows (Installation)
Download Python:

Go to: https://www.python.org/downloads/

Download the latest version

Important: When installing, check the box that says "Add Python to PATH"

Click "Install Now"

Install dependencies:

Press Windows key + R

Type cmd and press Enter (a black window opens)

Type this command and wait:

Bash
pip install pyautogui
If you get an error, try:

Bash
python -m pip install pyautogui
Linux (Installation)
Check if you have Python:

Open terminal (search "Terminal" in your menu or press Ctrl + Alt + T)

Type:

Bash
python3 --version
If it shows a number (e.g., 3.8.10), you have it. If not, install it from your package manager.

Install dependencies:

In the terminal type:

Bash
pip3 install pyautogui
If pip3 doesn't exist, install it first:

Ubuntu/Debian:

Bash
sudo apt install python3-pip
pip3 install pyautogui
Fedora/CentOS:

Bash
sudo dnf install python3-pip
pip3 install pyautogui
Arch:

Bash
sudo pacman -S python-pip
pip3 install pyautogui
Configuration
Open the file sotelock.py with any text editor:

Windows: Right click → "Open with" → Notepad

Linux: Right click → "Open with" → Text Editor, or in terminal: nano sotelock.py

Step 1: Add your passwords
Find this section and change the examples to your real data:

Python
password_db = [
    sotelock("Netflix", "your password here"),
    sotelock("Gmail", "your other password here"),
    sotelock("Bank", "your_secret_key"),
]
Step 2: Add your emails
Find this section and do the same:

Python
mail_db = [
    sotelock("Personal", "youremail@gmail.com"),
    sotelock("Work", "work@company.com"),
]
Step 3: Change the secret question
Find this line:

Python
if letra == "e":
Change "e" to your secret answer. For example, if you put "london", you'll need to type london to enter.

Also change the question a few lines above:

Python
print("    Tell me, 'What is your dog's name'?")
Save the file (Ctrl + S).

How to Use
Windows (Usage)
Open the folder where you saved sotelock.py

Double-click the file

If it opens and closes quickly, do this:

Open terminal (Windows + R, type cmd)

Type cd (with a space at the end)

Drag the folder where the file is to the black window

Press Enter

Type: python sotelock.py

Linux (Usage)
Open the terminal

Go to the folder where the file is:

Bash
cd /path/to/folder
(You can type cd and drag the folder to the terminal)

Give it execution permission (only first time):

Bash
chmod +x sotelock.py
Run the program:

Bash
python3 sotelock.py
Once the program is open:
Answer the secret question (the one you configured before)

You'll see a menu:

Press 1 to type an email

Press 2 to type a password

Press 3 to exit

Choose which one you want to type (type its number and press Enter)

Quick! You have 3 seconds to move your mouse where you want it to type (for example, in the password box of a website)

The program types automatically

About the @ symbol in emails
When you choose an email, the program types the part before the @, stops and asks you to type the @ manually. This is normal and is for security. You type @ and it continues with the rest (gmail.com, etc.).

Security
⚠️ IMPORTANT - Read this:

Don't upload this file to the Internet (GitHub, Google Drive, etc.) with your real passwords inside

Passwords are stored in plain text: anyone opening the file can read them

Keep the file only on your personal computer

On Linux: You can protect the file so only you can read it:

Bash
chmod 600 sotelock.py
