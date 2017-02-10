#!/usr/bin/env python3

import sys
dencode = input("Do you want to encode or decode ? [encode/decode] ")

if dencode == "encode":
  print("Please type your text in CAPITAL letters and use 'X' as space. ")
  input = input()
  print('encoding: ' + input)
elif dencode == "decode":
  print("Please type your text in CAPITAL letters. ")
  output = input()
  print('encoding: ' + decoding)
else:
  print("Unknown command")
  sys.exit(127)
