import os
import hashlib
import pyperclip
from PIL import Image
import base64
from termcolor import colored

os.system('color')

print('''for the nerds, this uses SHA-224
''')

print(colored('''This program basically does the EXACT SAME thing Apple's new CSAM detection project will.
I created it to show you just how stupid the implementation is, and further your knowledge
so you can sniff out bullshit like this in the future.

(For most prompts, y = Yes and n = No)

''', 'green'))

def imghasher():
    try:
        with open(input('Input your image address here: '), 'rb') as image:
            b64string = base64.b64encode(image.read()).decode('ASCII')
            Hash = hashlib.sha224(str(b64string).encode('utf-8')).hexdigest()
            print(colored('Your image hash value is:'), colored(Hash, 'red'))
            pasteorno = input('Would you like to copy that to the clipboard?: ')
            if pasteorno.lower() == 'y':
                pyperclip.copy(Hash)
            again = input('Would you like to hash again? ')
            if again.upper() == 'Y':
                imghasher()
            else:
                 program()
    except FileNotFoundError:
        print('INVALID FILEPATH: Try dragging and dropping it directly into the window')
        conOrno = input('Would you like to exit?: ')
        if conOrno.lower() == 'y':
            program()
        imghasher()



def isSame():
    for n in range(1):
        firstHash = input('Input your first hash value here: ')
        secondHash = input('Input your second hash value here: ')
        if firstHash == secondHash:
            print(colored('PERFECT MATCH, UNDERLYING CONTENTS ARE BIT-FOR-BIT THE SAME', 'cyan'))
        else:
            print(colored('ERROR: HASH VALUES DO NOT MATCH, UNDERLYING CONTENTS ARE DIFFERENT.', 'red'))

    again = input('Would you like to compare 2 values again?: ')
    if again.lower() == 'y':
        isSame()
    else:
        program()

def program():

    hashOrcompare = int(input('''What would you like to do?
    Enter 1 to hash an image
    Enter 2 to compare hashes
    Enter anything else to exit
    (input here) > '''))

    if hashOrcompare == 1:

        yeOrne = input('Would you like a basic explanation on what this does and what hashes are?: ')
        if yeOrne.lower() == 'y':

            print(colored('''
This is where you'll create a hash value of an image

Basically, a hash value is an irreversible, unique identifier for practically
any digital input into a hashing algorithm. This can be anything from plaintext, to
(in this case) an image file, to an ENTIRE hard drive. This is extremely useful in forensics,
for example, let's say you pick up a hard drive at a crime scene. You need to ensure and demonstrate that
it has maintained integrity (basically, hasn't been tampered with) from collection, all the way through
chain of custody, to when you produce it at court. A hash value is perfect for this, because if the hard drive
stays the exact same (bit-for-bit), the hash value will also stay the exact same. So, going back to the 
forensics example, an investigator would generate a hash value upon first collection at the crime scene,
pass it to the correct hands (chain-of-custody), and then upon the court-date, another investigator would
generate a hash of the same hard drive, and they would match. This both ensures and proves integrity
making the hard drive admissible as evidence in court.
    ''', 'green'))

        imghasher()

    elif hashOrcompare == 2:
        yeOrne = input("Would you like a basic explanation on what this does and how it's used?: ")
        if yeOrne.lower() == 'y':
            print(colored('''
This will basically compare the two hash values to see if they're the same

Going back to the forensics explanation in the image hashser, on the court date they'd use an application like this
to demonstrate the first hash value (created at first collection) and second hash value (created on court day)
are the exact same. If the underlying hard drive is the EXACT SAME (bit-for-bit), the hash values will be the same,
and this program will say so. This is practically the exact same thing Apple check your image hash against the 
hashes of confirmed and verified images of child abuse. God, imagine being the person who has to verify images
of child abuse.
    ''', 'green'))

        isSame()
    else:
        return

program()
