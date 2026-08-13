# Sotelock v2.0 - Password & Email Manager with Auto-Typer

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/) [![SQLite](https://img.shields.io/badge/SQLite-3-green.svg)]() [![Platform](https://img.shields.io/badge/Windows%20%7C%20Linux-lightgrey.svg)]() ![License](https://img.shields.io/badge/License-MIT-green.svg)

*A sarcastic, over-engineered password manager that roasts you while keeping your credentials safe*

[🇬🇧 English](#-english-guide) | [🇪🇸 Español](#-guía-en-español)

</div>

---

## 📋 Table of Contents / Índice

**English Content:**

- [📖 Overview](#-overview)
- [✨ Features](#-features)
- [📁 Files](#-files)
- [🛠️ Installation](#-installation)
- [🚀 Usage](#-usage)
- [⚠️ security](#-security)
- [🤝 Contributing ](#-contributing)
- [📜 License](#-license)

  

**Contenido en Español:**
- [📖 Descripción general](#-descripción-general)
- [✨ Características](#-caracteristicas)
- [📁 Archivos](#-archivos)
- [🛠️ Instalación](#-instalación)
- [🚀 Uso](#-uso)
- [⚠️ Seguridad](#-seguridad)
- [🤝 Contribuciones](#-contributing--contribuciones)
- [📜 Licencia](#-licencia)

---

</div>

## 📖 Overview

**Sotelock** is no longer just a simple auto-typer. Now it's a full-featured password manager with SQLite database, master password authentication, and an attitude problem. It stores your credentials securely (well, locally), lets you add/remove entries, and automatically types them for you when needed.

**New in v2.0:** Persistent SQLite database, master password authentication, full credential management (add/view/delete), and an even more sarcastic personality.

## ✨ Features

- 🔐 **Master Password** - Configurable on first run, required on every launch
- 🗄️ **SQLite Database** - Persistent storage (no more editing Python files!)
- ➕ **Full CRUD** - Create, Read, and Delete entries (Update coming... maybe)
- ⌨️ **Auto-Typer** - Uses PyAutoGUI to type credentials for you
- 📧 **Smart Email Handling** - Pauses at @ symbol for manual entry (security feature)
- 💬 **Sarcastic CLI** - The program will judge your mistakes. Heavily.
- 🛡️ **User Binding** - Tied to your OS username (attempts to prevent unauthorized use)

## 📁 Files
```bash
sotelock/
├── sotelock.py      # Main application (the sarcastic one)
├── database.py      # Database handler (SQLite operations)
└── database.sot     # Your encrypted* data (*not really, it's SQLite)
```
⚠️ **IMPORTANT:** You need **both .py files** in the same folder.

## 🛠️ Installation
Clone this repository
Python 3.6+
```bash
pip3 install pyautogui #Little reminder, in windows is pip
```
Run:
```bash
python3 sotelock.py #Little reminder, in windows is python
# Set up your master password when prompted
# You get 3 attempts to confirm it correctly
# This will be your access key forever
```
## How to Use

#### Authentication
- On startup, the program verifies it's you (based on system username). If the master password isn't configured, it will guide you through creating one.

#### Main Menu
```bash
1. Mails/Emails    - Manage email addresses
2. Passwords       - Manage passwords  
3. Exit            - Exit (with GitHub link)
```
#### Sub-menus

```bash
Both sections (Emails and Passwords) have:

1. Get - View list and auto-type
2. Add - Add new entry (with confirmation)
3. Delete - Delete existing entry
```

#### Auto-Typing
When you select "Get":

You'll see a numbered list of your entries
Choose a number
You have 3 seconds to position the cursor where you want to type
For emails: manually type the @ when prompted
The program types the rest automatically

#### Patience System

*The program has a decreasing patience system:*

> Access attempts: 3 failures and you're out
> Error patience: 5 levels of increasing sarcasm
> Zero Easter egg: Try typing "0" in any menu and see what happens
> "Your performance is as disappointing as my compile times." - Sotelock, 2024

## ⚠️ Security
> [!WARNING]
> Warnings:
> Plain Text: Passwords are stored in SQLite without encryption (for now). Don't upload the database.sot file to the internet.
> Local Access: Anyone with access to your computer who knows your master password can see everything.
> Not Fort Knox: This is a personal/educational project. Don't use for ultra-sensitive data without improving security.
> Linux Permissions: Recommended:
```bash
chmod 600 database.sot
chmod +x sotelock.py
```
#### Database Structure
sqlite Tables created automatically:
```sql
passwords (id, service, passwd)
mail (id, service, mail)
access (id, access_passwd)  -- Your master password
```

#### Customization
```bash
Changing the sarcastic messages:
Look for strings in the code and substitude them with custom messages
```

```python
# Example in the lock() method:
print(choice([
    "Access denied. Your hacker career ends here.",
    "That's enough. Go outside and touch some grass.",
    "..."
]))
```

### 🤝 Contributing

Sotelo - [@sotelodev2008](https://github.com/sotelodev2008)

***If you would like to support the project, please submit a Pull Request on GitHub with your improvements.***

📜 License
Personal project. Use it, modify it, but don't blame me if you forget your master password.

**Key changes from the previous version:**
- Reflects the 2-file architecture (main + database)
- Explains the master password authentication system
- Mentions the "patience" system and sarcastic messages as features
- Includes the SQLite database structure
- Maintains the bilingual format but focuses more on the new capabilities
- Warns about the unencrypted nature of the database (important!)

---

## 📖 Descripción general

**Sotelock** is no longer just a simple auto-typer. Now it's a full-featured password manager with SQLite database, master password authentication, and an attitude problem. It stores your credentials securely (well, locally), lets you add/remove entries, and automatically types them for you when needed.

**Novedades v2.0:** Base de datos SQLite persistente, autenticación con contraseña maestra, gestión completa (añadir/ver/borrar), y una personalidad aún más sarcástica.

## 📋 Características

- 🔐 **Contraseña Maestra** - Configurable en el primer inicio y obligatoria cada vez que arranca la aplicación.
- 🗄️ **Base de datos SQLite** -  Almacenamiento persistente (¡se acabó eso de andar editando archivos de Python a mano!).
- ➕ **CRUD completo** - Crear, leer y borrar registros (la actualización vendrá... algún día, tal vez).
- ⌨️ **Auto-escritura** - Utiliza PyAutoGUI para escribir tus credenciales por ti.
- 📧 **Gestión inteligente de correos** - Se detiene de forma automática en el símbolo @ para que completes el resto a mano (medida de seguridad).
- 💬 **CLI Sarcástica** - El programa evaluará cada uno de tus errores. Y no tendrá piedad.
- 🛡️ **Vinculación de usuario** - Asociado a tu nombre de usuario del sistema operativo (un intento honesto de evitar usos no autorizados).

## 📁 Archivos
```bash
sotelock/
├── sotelock.py # Aplicación principal (La sarcástica)
├── database.py # Gestor de base de datos (Operaciones SQLite)
└── database.sot # Tu base de datos
```
> ⚠️ **IMPORTANTE:** Necesitas **ambos archivos** `.py` en la misma carpeta.


---

## 🛠️ Instalación
- Clona este repositorio
- Python 3.6+

```bash
pip3 install pyautogui # Pequeño recordatorio, en windows es pip a secas
```
## 🚀 Uso:
```bash
python sotelock.py
Configura tu contraseña maestra cuando se te pida
Tendrás 3 intentos para confirmarla correctamente
Esta será tu llave de acceso para siempre
```
#### Autenticación
- Al iniciar, el programa verifica que seas tú (basado en el nombre de usuario del sistema). Si la contraseña maestra no está configurada, te guiará para crearla.

#### Menú Principal
```bash
1. Mails/Emails    - Gestiona correos electrónicos
2. Passwords       - Gestiona contraseñas  
3. Exit            - Salir (con enlace a GitHub)
```

#### Sub-menús
- Ambas secciones (Emails y Passwords) tienen:
```bash
1. Get - Ver lista y escribir automáticamente
2. Add - Añadir nueva entrada (con confirmación)
3. Delete - Eliminar entrada existente
```

#### Auto-Typing

Cuando seleccionas "Get":

Verás una lista numerada de tus entradas
Elige un número
Tienes 3 segundos para posicionar el cursor donde quieres escribir
Para emails: escribe manualmente el @ cuando se te indique
El programa escribe el resto automáticamente

#### Sistema de "Paciencia"

***El programa tiene un sistema de paciencia decreciente:***

> Intentos de acceso: 3 fallos y te echa
> Paciencia con errores: 5 niveles de sarcasmo creciente
> Easter egg del 0: Intenta escribir "0" en cualquier menú y descubre qué pasa
> "Your performance is as disappointing as my compile times." - Sotelock, 2024

## ⚠️ Seguridad
> [!WARNING]
> Texto Plano / Plain Text: Las contraseñas se almacenan en SQLite sin encriptar (aún). No subas el archivo database.sot a internet.
> Acceso Local: Cualquiera con acceso a tu computadora y que sepa tu contraseña maestra puede ver todo.
> No es Fort Knox: Este es un proyecto personal/educativo. No uses para datos ultra-sensibles sin mejorar la seguridad.
> Permisos Linux: Recomendado:
```bash
chmod 600 database.sot
chmod +x sotelock.py
```

#### Estructura de la BD / DB Structure
```sql
-- Tablas creadas automáticamente:
passwords (id, service, passwd)
mail (id, service, mail)
access (id, access_passwd)  -- Tu contraseña maestra
```
#### Personalización / Customization
```bash
Cambiar los mensajes sarcásticos:
Busca cadenas de texto en el codigo y substituyelas con un texto personalizado
```
```python
# Ejemplo en el método lock():
print(choice([
    "Access denied. Your hacker career ends here.",
    "That's enough. Go outside and touch some grass.",
    "..."
]))
```

### 🤝 Contribuciones

Sotelo - [@sotelodev2008](https://github.com/sotelodev2008)

***If you would like to support the project, please submit a Pull Request on GitHub with your improvements.***

---

📜 Licencia
Proyecto personal. Úsalo, módificalo, pero no me culpes si olvidas tu contraseña maestra.

**Cambios clave respecto al anterior:**
- Refleja la arquitectura de 2 archivos (main + database)
- Explica el sistema de autenticación con contraseña maestra
- Menciona el sistema de "paciencia" y mensajes sarcásticos como feature
- Incluye la estructura de la base de datos SQLite
- Mantiene el formato bilingüe pero más enfocado en las nuevas capacidades
- Advierte sobre la naturaleza no-encriptada de la BD (importante!)