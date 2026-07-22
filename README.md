# Sotelock - Password Auto-typer

Simple script to automatically type your passwords and emails so you don't have to memorize them, or type then in public.

## Quick Install

```bash
# Install dependencies (they're in requisites.py)
pip install -r requisites.py

What you can customize
1. Your passwords and emails
Find these sections in the code:

python
password_db = [
    sotelock("Netflix", "your_pass_here"),
    sotelock("Gmail", "another_password")
]

mail_db = [
    sotelock("Personal", "your@email.com"),
    sotelock("Work", "work@company.com")
]
Put your own services and credentials there. Add as many as you want.

2. The secret question
In the lock() function, change this:

python
if letra == "e":  # Change "e" to your secret answer
And above that, change the question:

python
print("    Tell me, 'Question'?")  # Change 'Question' to whatever you want
3. The sarcastic messages
The patience = 5 variable controls how many tries you get before the program kicks you out. You can change the messages that show up on each failed attempt if you want it to be less (or more) rude.

4. The timing
In writter() change:

python
time.sleep(3)  # Seconds to position your cursor
5. The ASCII art
The banner and lock are just text. Replace them with whatever you want using ASCII art generators.

⚠️ Important: The program CANNOT type @
When you select an email, the program types the part before the @, stops and tells you to manually type the @ yourself, waits 2 seconds, then types the rest (gmail.com, etc.).

This is on purpose, not a bug. It's a security thing so the @ doesn't get logged somewhere or whatever.

How to use it
Run the script: python sotelock.py
Answer the secret question
Choose if you want an email (1) or password (2)
Pick which one
You have 3 seconds to put your cursor where the text goes
Done, it types it for you
For emails: remember that you have to type the @ when it asks.

Basic security
Keep this file local, don't upload it to GitHub with your real passwords. Credentials are stored in plain text, so keep the file safe on your computer.

Extra customization
Want more menu options? Add more elif option == 4: etc.
Want it to type slower/faster? Adjust the time.sleep() values
Want to change the insults? Edit the error messages
That's it. Use responsibly.

