#!/usr/bin/env python3

import sys

firstWheel = input("What should the first wheel be? (each wheel can only be used once) [I/II/III/IV/V] ")

input = input("Please type your text you want to decode or encode in CAPITAL letters and use 'X' as space. ")

if dencode == "encode":
  print("Please type your text in CAPITAL letters and use 'x' as space. ")
  input = input()
  print('encoding: ' + input)
elif dencode == "decode":
  print("Please type your text in CAPITAL letters. ")
  output = input()
  print('encoding: ' + decoding)
else:
  sys.stdout.write("\033[1;31m")
  print("Unknown command")
  sys.stdout.write("\033[0;0m")
  sys.exit(127)
