# pynigma

This python program should emulate an Enigma M3, which was used by the Navy, Airforce and Army. The M3 three uses 3 wheels while the M4 uses 4 wheels. The two machines are only compatible with each other with certain settings.

Support for other rotors, UKWs (Umkehrwalzen) and ETWs (Eintrittswalzen) can easily be added.

Here's how it works:

     1. Convert input letter to number - validate!
     2. Rotate wheels
     3. Pass through plugboard (currently NOT supported)
     4. Pass through right-hand wheel
     5. Pass through middle wheel
     6. Pass through left-hand wheel
     7. Pass through reflector
     8. Pass through left-hand wheel
     9. Pass through middle wheel
    10. Pass through right-hand wheel
    11. Pass through plugboard (currently NOT supported)
    12. Convert to output letter

##Numbers

Numbers:
![number](http://enigma.louisedade.co.uk/numberkeys.png)

To include numbers in your message, you first need to indicate that you are about to use a number by entering the letter "Y" before each number. So, to encode the number 5 in your message you would type in "YT", the number 6 would be "YZ", and 42 would be "YRW".

##Resources
- http://enigma.louisedade.co.uk/howitworks.html
- https://de.wikipedia.org/wiki/Enigma-Walzen (Rotor information)
