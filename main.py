#!/usr/bin/env python3

import sys
import string
import os

# use colors class for better input and output, while still supporting NT based OSs
if os.name == "posix":
    class colors:
        HEADER = '\033[95m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        WARNING = '\033[93m'
        RED = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
else:
    class colors:
        HEADER = ''
        BLUE = ''
        GREEN = ''
        WARNING = ''
        RED = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''

# Alphabet list for converting input letters to numbers
ABC = list(string.ascii_uppercase)

# define the Walzen
I = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
II = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
III = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
IV = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']
V = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']
VI = ['J', 'P', 'G', 'V', 'O', 'U', 'M', 'F', 'Y', 'Q', 'B', 'E', 'N', 'H', 'Z', 'R', 'D', 'K', 'A', 'S', 'X', 'L', 'I', 'C', 'T', 'W']
VII = ['N', 'Z', 'J', 'H', 'G', 'R', 'C', 'X', 'M', 'Y', 'S', 'W', 'B', 'O', 'U', 'F', 'A', 'I', 'V', 'L', 'P', 'E', 'K', 'Q', 'D', 'T']
VIII = ['F', 'K', 'Q', 'H', 'T', 'L', 'X', 'O', 'C', 'B', 'J', 'S', 'P', 'D', 'Z', 'R', 'A', 'M', 'E', 'W', 'N', 'I', 'U', 'Y', 'G', 'V']
# beta and gamma were used in the Enigma M4
beta = ['L', 'E', 'Y', 'J', 'V', 'C', 'N', 'I', 'X', 'W', 'P', 'B', 'Q', 'M', 'D', 'R', 'T', 'A', 'K', 'Z', 'G', 'F', 'U', 'H', 'O', 'S']
gamma = ['F', 'S', 'O', 'K', 'A', 'N', 'U', 'E', 'R', 'H', 'M', 'B', 'T', 'I', 'Y', 'C', 'W', 'L', 'Q', 'P', 'Z', 'X', 'V', 'G', 'J', 'D']
A = ['E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C', 'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P', 'I', 'K', 'H', 'G', 'D']
B = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']
C = ['F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X', 'W', 'G', 'C', 'T', 'K', 'U', 'Q', 'S', 'B', 'N', 'M', 'H', 'L']
B_thin = ['E', 'N', 'K', 'Q', 'A', 'U', 'Y', 'W', 'J', 'I', 'C', 'O', 'P', 'B', 'L', 'M', 'D', 'X', 'Z', 'V', 'F', 'T', 'H', 'R', 'G', 'S']
C_thin = ['R', 'D', 'O', 'B', 'J', 'N', 'T', 'K', 'V', 'E', 'H', 'M', 'L', 'F', 'C', 'W', 'Z', 'A', 'X', 'G', 'Y', 'I', 'P', 'S', 'U', 'Q']

# get input from user
firstRotor = eval(input("Choose the " + colors.BOLD + "first " + colors.ENDC + "rotor (each rotor can only be used once) [I/II/III/IV/V/VI/VII/VIII] "))
# use static rotor for correct turning
firstRotorStatic = firstRotor
secondRotor = eval(input("Choose the " + colors.BOLD + "second " + colors.ENDC + "rotor (each rotor can only be used once) [I/II/III/IV/V/VI/VII/VIII] "))
secondRotorStatic = secondRotor
thirdRotor = eval(input("Choose the " + colors.BOLD + "third " + colors.ENDC + "rotor (each rotor can only be used once) [I/II/III/IV/V/VI/VII/VIII] "))
# fourthRotor for Enigma M4
# check if every Rotor is only used once
if firstRotor == secondRotor or firstRotor == thirdRotor or secondRotor == thirdRotor:
    print(colors.RED + "Each rotor can only be used once" + colors.ENDC)
    sys.exit(1)
# get the initial positions of the rotors
firstRotorPosition = int(input("Choose the position of the " + colors.BOLD + "first " + colors.ENDC + "rotor [1-26] ")) - 1
if firstRotorPosition < 0 or firstRotorPosition > 25:
    print(colors.WARNING + "Choose a value between 1 and 26" + colors.ENDC)
    firstRotorPosition = int(input("Choose the position of the " + colors.BOLD + "first " + colors.ENDC + "rotor [1-26] ")) - 1
    if firstRotorPosition < 0 or firstRotorPosition > 25:
        print(colors.RED + "Choose a value between 1 and 26" + colors.ENDC)
        sys.exit(1)
secondRotorPosition = int(input("Choose the position of the " + colors.BOLD + "second " + colors.ENDC + "rotor [1-26] ")) - 1
if secondRotorPosition < 0 or secondRotorPosition > 25:
    print(colors.WARNING + "Choose a value between 1 and 26" + colors.ENDC)
    secondRotorPosition = int(input("Choose the position of the " + colors.BOLD + "second " + colors.ENDC + "rotor [1-26] ")) - 1
    if secondRotorPosition < 0 or secondRotorPosition > 25:
        print(colors.RED + "Choose a value between 1 and 26" + colors.ENDC)
        sys.exit(1)
thirdRotorPosition = int(input("Choose the position of the " + colors.BOLD + "third " + colors.ENDC + "rotor [1-26] ")) - 1
if thirdRotorPosition < 0 or thirdRotorPosition > 25:
    print(colors.WARNING + "Choose a value between 1 and 26" + colors.ENDC)
    thirdRotorPosition = int(input("Choose the position of the " + colors.BOLD + "third " + colors.ENDC + "rotor [1-26] ")) - 1
    if thirdRotorPosition < 0 or thirdRotorPosition > 25:
        print(colors.RED + "Choose a value between 1 and 26" + colors.ENDC)
        sys.exit(1)
# let the user choose the reflector
reflector = eval(input("Choose reflector [A/B/C/B_thin/C_thin] "))

# input text from user
inputtext = input("Please type your text you want to decode or encode. Use 'X' as space or a stop. ")

# convert text to only upper case letters
inputtext = inputtext.upper()
# check for numbers in input
if len(set(string.digits).intersection(inputtext)) > 0:
    print(colors.RED + colors.BOLD + "Refer to the README. Don't use digits")
    if ' ' in inputtext:
        print("and no space!")
    print(colors.ENDC)
    sys.exit(1)
# convert input to list
textArray = list(inputtext)


# define reverse function for the way "back"
def reverse(array):
    reverseRotor = []
    for s in range(0, 26):
        reverseRotor.append(ABC[array.index(ABC[s])])
    return reverseRotor


# define shift function for shifting the rotors
def shift(array, int):
    return array[int:] + array[:int]


# shift to initial positions
firstRotor = shift(firstRotor, firstRotorPosition)
secondRotor = shift(secondRotor, secondRotorPosition)
thirdRotor = shift(thirdRotor, thirdRotorPosition)

# run code once for every letter in the input
for i in range(0, len(textArray)):

    # initial shift
    firstRotor = shift(firstRotor, 1)
    # check if any rotor is at the turnover notch position
    if firstRotorStatic == I:
        if firstRotor[0] == 'U':
            secondRotor = shift(secondRotor, 1)
    elif firstRotorStatic == II:
        if firstRotor[0] == 'I':
            secondRotor = shift(secondRotor, 1)
    elif firstRotorStatic == III:
        if firstRotor[0] == 'U':
            secondRotor = shift(secondRotor, 1)
    elif firstRotorStatic == IV:
        if firstRotor[0] == 'U':
            secondRotor = shift(secondRotor, 1)
    elif firstRotorStatic == V:
        if firstRotor[0] == 'V':
            secondRotor = shift(secondRotor, 1)
# some rotors have two turnover positions
    elif firstRotorStatic == VI:
        if firstRotor[0] == 'J' or firstRotor[0] == 'H':
            secondRotor = shift(secondRotor, 1)
    elif firstRotorStatic == VII:
        if firstRotor[0] == 'N' or firstRotor[0] == 'O':
            secondRotor = shift(secondRotor, 1)
    elif firstRotorStatic == VIII:
        if firstRotor[0] == 'F' or firstRotor[0] == 'D':
            secondRotor = shift(secondRotor, 1)
    elif firstRotorStatic == beta:
        if firstRotor[0] == 'P':
            secondRotor = shift(secondRotor, 1)
    elif firstRotorStatic == gamma:
        if firstRotor[0] == 'P':
            secondRotor = shift(secondRotor, 1)
    elif secondRotorStatic == I:
        if secondRotor[0] == 'U':
            thirdRotor = shift(thirdRotor, 1)
    elif secondRotorStatic == II:
        if secondRotor[0] == 'I':
            thirdRotor = shift(thirdRotor, 1)
    elif secondRotorStatic == III:
        if secondRotor[0] == 'U':
            thirdRotor = shift(thirdRotor, 1)
    elif secondRotorStatic == IV:
        if secondRotor[0] == 'U':
            thirdRotor = shift(thirdRotor, 1)
    elif secondRotorStatic == V:
        if secondRotor[0] == 'V':
            thirdRotor = shift(thirdRotor, 1)
    elif secondRotorStatic == VI:
        if secondRotor[0] == 'J' or secondRotor[0] == 'H':
            thirdRotor = shift(thirdRotor, 1)
    elif secondRotorStatic == VII:
        if secondRotor[0] == 'N' or secondRotor[0] == 'O':
            thirdRotor = shift(thirdRotor, 1)
    elif secondRotorStatic == VIII:
        if secondRotor[0] == 'F' or secondRotor[0] == 'D':
            thirdRotor = shift(thirdRotor, 1)
    elif secondRotorStatic == beta:
        if secondRotor[0] == 'P':
            thirdRotor = shift(thirdRotor, 1)
# reverse the rotors
    firstRotorReversed = reverse(firstRotor)
    secondRotorReversed = reverse(secondRotor)
    thirdRotorReversed = reverse(thirdRotor)

# most important piece of the script
# it basically takes the position of the letter in the list which then gets passed through the rotors, reflector and reverse rotors
    print(colors.GREEN + colors.BOLD + firstRotorReversed[ABC.index(secondRotorReversed[ABC.index(thirdRotorReversed[ABC.index(reflector[ABC.index(thirdRotor[ABC.index(secondRotor[ABC.index(firstRotor[ABC.index(textArray[i])])])])])])])] + colors.ENDC, end="")
# was needed for better looks
print('')
