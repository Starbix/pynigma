#!/usr/bin/env python3

import sys

dencode = input("Do you want to encode or decode ? [encode/decode] ")

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
