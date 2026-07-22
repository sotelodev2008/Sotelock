# Sotelock - Auto-escritor de Contraseñas / Password Auto-typer

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Windows%20%7C%20Linux-lightgrey.svg)]()

</div>

---

## ¿Qué es esto? / What is this?

**🇪🇸 Español:** Programa simple que escribe automáticamente tus contraseñas o emails para que no tengas que memorizarlas, ni escribirlas en público.

**🇬🇧 English:** Simple script to automatically type your passwords and emails so you don't have to memorize them, or type them in public.

---

## 📑 Índice / Index

**Contenido en Español:**
- [Requisitos](#requisitos)
- [Instalación](#instalacion)
  - [Windows](#windows-instalacion)
  - [Linux](#linux-instalacion)
- [Configuración](#configuracion)
- [Cómo usar](#como-usar)
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

1. **Python** (el programa y lenguaje de programación que hace funcionar este script).
2. **El archivo `sotelock.py`** (descargado en tu ordenador).

## Instalacion

### Windows (Instalacion)

1. **Descarga Python:**
   - Ve a: https://www.python.org/downloads/
   - Descarga la última versión.
   - **Importante:** Al instalar, marca la casilla que dice **"Add Python to PATH"**.
   - Dale a "Install Now".

2. **Instala las dependencias:**
   - Presiona la tecla `Windows` + `R`.
   - Escribe `cmd` y dale a Enter (se abre una ventana negra).
   - Escribe este comando y espera:
     ```bash
     pip install pyautogui
     ```
   - Si te da error, prueba:
     ```bash
     python -m pip install pyautogui
     ```

### Linux (Instalacion)

1. **Verifica si tienes Python:**
   - Abre la terminal (busca "Terminal" en tu menú o presiona Ctrl + Alt + T).
   - Escribe:
     ```bash
     python3 --version
     ```
   - Si te muestra un número (ej: 3.8.10), ya lo tienes. Si no, instálalo desde tu gestor de paquetes (apt, pacman, etc).

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

## Configuracion

Abre el archivo `sotelock.py` con cualquier editor de texto (Preferiblemente un editor de código compatible con Python como VS-Code):
- **Windows:** Clic derecho → "Abrir con" → Bloc de notas.
- **Linux:** Clic derecho → "Abrir con" → Editor de texto, o en terminal: `nano sotelock.py`.

### Paso 1: Pon tus contraseñas
Busca esta sección y cambia los ejemplos por tus datos reales:

```python
password_db = [
    sotelock("Netflix", "aquí pones tu contraseña"),
    sotelock("Gmail", "aquí pones otra contraseña"),
    sotelock("Banco", "tu_clave_secreta"),
]
```

### Paso 2: Pon tus correos
Busca esta sección y haz lo mismo:

```python
mail_db = [
    sotelock("Personal", "tuemail@gmail.com"),
    sotelock("Trabajo", "trabajo@empresa.com"),
]
```

### Paso 3: Cambia la pregunta secreta
Busca esta línea:

```python
if letra == "e":
```

Cambia la `"e"` por tu respuesta secreta. Por ejemplo, si pones `"madrid"`, tendrás que escribir madrid para entrar.

También cambia la pregunta que está unas líneas arriba:

```python
print("    Entonces, responde a esta pregunta, ¿'Cómo se llama tu perro'?")
```

Guarda el archivo (`Ctrl + S`).

---

## Como usar

### Windows (Uso)

1. Abre la carpeta donde guardaste el archivo `sotelock.py`.
2. Haz clic en la barra de direcciones de la carpeta superior, escribe `cmd` y presiona Enter.
3. Ejecuta el script escribiendo el siguiente comando:
   ```bash
   python sotelock.py
   ```

### Linux (Uso)

1. Abre tu terminal favorita.
2. Navega hasta el directorio de la descarga usando `cd` (ejemplo: `cd Downloads`).
3. Ejecuta el archivo utilizando Python 3:
   ```bash
   python3 sotelock.py
   ```
4. *(Opcional)* Si quieres, cámbiale los permisos para que solo tú puedas acceder y ejecutar el archivo:
   ```bash
   chmod +700 ./sotelock.py
   ```

---

### 🕹️ Instrucciones de ejecución

1. **Responde la pregunta secreta** (la que configuraste previamente en el archivo).
2. **Verás el siguiente menú en pantalla**:
   * **Pulsa 1**: Para escribir un correo.
   * **Pulsa 2**: Para escribir una contraseña.
   * **Pulsa 3**: Para salir del programa.
3. **Elige cuál quieres escribir** introduciendo su número correspondiente y presionando `Enter`.
4. **¡Sé rápido!** Tienes exactamente **3 segundos** para hacer clic con el ratón en la casilla o lugar donde quieras que el programa escriba (por ejemplo, el campo de texto de una página web).
5. El programa escribirá automáticamente tus credenciales.

#### 📧 Sobre el símbolo @ en los correos
Cuando eliges la opción de un correo, el programa escribirá la parte anterior al símbolo `@`, se detendrá y te pedirá que escribas tú la `@` manualmente. **Esto es un comportamiento normal de seguridad**. Una vez que escribas la `@`, el script continuará automáticamente con el resto del dominio (ej: `gmail.com`).

---

## Seguridad

> [!CAUTION]
> ### ⚠️ IMPORTANTE - Lee esto atentamente:
>
> * **No subas este archivo a Internet** (GitHub, Google Drive, etc.) si contiene tus contraseñas reales escritas dentro.
> * **Texto plano**: Las contraseñas se guardan en texto legible. Cualquiera con acceso físico o remoto a tu ordenador que abra el archivo podrá leerlas.
> * **Uso local**: Mantén este archivo guardado única y estrictamente en tu computadora de uso personal.
> * **Protección en Linux**: Puedes proteger el archivo restringiendo los accesos de otros usuarios del sistema con el siguiente comando:
>   ```bash
>   chmod 600 sotelock.py
>   ```

<!-- ================================================== -->
<!-- ALL ENGLISH CONTENT STARTS FROM HERE -->
<!-- ================================================== -->

# 📙 Complete English Guide

## Requirements

You need two things before getting started:

1. **Python** (the program and programming language required to run this script).
2. **The `sotelock.py` file** (downloaded to your computer).

## Installation

### Windows (Installation)

1. **Download Python:**
   - Go to: https://www.python.org/downloads/
   - Download the latest version available.
   - **Important:** During installation, make sure to check the box that says **"Add Python to PATH"**.
   - Click on "Install Now".

2. **Install dependencies:**
   - Press the `Windows` key + `R`.
   - Type `cmd` and hit Enter (a black terminal window will open).
   - Type the following command and wait:
     ```bash
     pip install pyautogui
     ```
   - If you encounter an error, try:
     ```bash
     python -m pip install pyautogui
     ```

### Linux (Installation)

1. **Verify if Python is installed:**
   - Open your terminal (search for "Terminal" in your menu or press Ctrl + Alt + T).
   - Type:
     ```bash
     python3 --version
     ```
   - If it displays a version number (e.g., 3.8.10), it is already installed. If not, install it using your package manager (apt, dnf, pacman, etc.).

2. **Install dependencies:**
   - In the terminal, type:
     ```bash
     pip3 install pyautogui
     ```
   - If pip3 is missing, install it first:

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

## Configuration

Open the `sotelock.py` file with any text editor (preferably a Python-compatible code editor like VS-Code):
- **Windows:** Right-click → "Open with" → Notepad.
- **Linux:** Right-click → "Open with" → Text Editor, or via terminal: `nano sotelock.py`.

### Step 1: Add your passwords
Locate this section and replace the placeholder examples with your real credentials:

```python
password_db = [
    sotelock("Netflix", "your_password_here"),
    sotelock("Gmail", "another_password_here"),
    sotelock("Bank", "your_secret_key"),
]
```

### Step 2: Add your emails
Locate this section and do the same:

```python
mail_db = [
    sotelock("Personal", "your-email@gmail.com"),
    sotelock("Work", "work@company.com"),
 ]
```

### Step 3: Change the secret security question
Locate this line:

```python
if letra == "e":
```

Change `"e"` to your own secret answer. For instance, if you set it to `"madrid"`, you will need to type madrid to grant script access.

Also, modify the question prompt a few lines above:

```python
print("    Then, respond to this question, 'What is your dog's name'?")
```

Save the file (`Ctrl + S`).

---

## How to Use

### Windows (Usage)

1. Open the folder where you saved the `sotelock.py` file.
2. Click on the file explorer's address bar at the top, type `cmd`, and press Enter.
3. Run the script by typing the following command:
   ```bash
   python sotelock.py
   ```

### Linux (Usage)

1. Open your preferred terminal.
2. Navigate to your download directory using `cd` (e.g., `cd Downloads`).
3. Run the script using Python 3:
   ```bash
   python3 sotelock.py
   ```
4. *(Optional)* If you want, restrict the file permissions so only you can access and execute it:
   ```bash
   chmod 700 ./sotelock.py
   ```

---

### 🕹️ Execution Instructions

1. **Answer the secret question** (the one you previously set up inside the file).
2. **You will see the following menu on your screen**:
   * **Press 1**: To type an email address.
   * **Press 2**: To type a password.
   * **Press 3**: To exit the program.
3. **Choose what you want to type** by entering its corresponding number and pressing `Enter`.
4. **Be fast!** You have exactly **3 seconds** to click with your mouse cursor inside the input field where you want the program to type (for example, a password field on a website).
5. The script will automatically type your credentials.

#### 📧 Regarding the @ symbol in emails
When you choose an email option, the program will type everything before the `@` symbol, pause, and ask you to type the `@` manually. **This is normal security behavior**. Once you type the `@`, the script will automatically resume typing the rest of the domain (e.g., `gmail.com`).

---

## Security

> [!CAUTION]
> ### ⚠️ IMPORTANT - Please read carefully:
>
> * **Do not upload this file to the Internet** (GitHub, Google Drive, etc.) if it contains your real passwords inside.
> * **Plain text**: Passwords are stored in a readable format. Anyone with physical or remote access to your computer who opens this file can read them.
> * **Local usage**: Keep this file stored strictly and exclusively on your personal computer.
> * **Linux protection**: You can protect the file by restricting other system users' access with the following command:
>   ```bash
>   chmod 600 sotelock.py
>   ```
