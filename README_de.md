# pynigma

Dieses Pythonscript sollte eine Enigma M3 emulieren. Die M3 benutzt 3 Rotoren, während die M4 4 Rotoren benutzt. Sie sind nur unter bestimmten Einstellungen kompatibel.
Support for other rotors, UKWs (Umkehrwalzen) and ETWs (Eintrittswalzen) can easily be added.

Wie es funktioniert:

     1. Input Buchstabe zu einer Zahlkonvertieren
     2. Rotoren rotieren
     3. Steckbrett durchlaufen (momentan nicht unterstützt)
     4. Rechten Rotor durchlaufen
     5. Mittleren Rotor durchlaufen
     6. Linken Rotor durchlaufen
     7. Reflektor durchlaufen
     8. Linken Rotor durchlaufen
     9. Mittleren Rotor durchlaufen
    10. Rechten Rotor durchlaufen
    11. Steckbrett durchlaufen (momentan nicht unterstützt)
    12. Zahl zu Buchstaben konvertieren

##Zahlen

Zahlen:
![Zahlen](http://enigma.louisedade.co.uk/numberkeys.png)

Um Zahlen in Nachrichten zu benutzen, muss man den Buchstaben "Y" vor der Zahl schreiben. Und als Zahl muss man Buchstaben benutzen wie man im obigen Bild sieht.

##Resourcen
- http://enigma.louisedade.co.uk/howitworks.html
- https://de.wikipedia.org/wiki/Enigma-Walzen (Rotor Information)
