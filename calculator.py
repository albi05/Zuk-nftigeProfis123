error = False
Zahl1 = input("Geben Sie die erste Zahl ein: ")

try:
 Zahl1 = float(Zahl1)

except:
 print("Du Idiot. Zahl geht nicht")
 error = True

Zahl2 = input("Geben Sie die zweite Zahl ein: ")

try:
 Zahl2 = float(Zahl2)

except:
 print("Du Idiot. Zahl geht nicht")
 error = True

operator = input("Was wollen Sie machen (+ | - | * | / )? ")

if operator == "+" and error == False:
    Ergebnis = Zahl1 + Zahl2
elif operator == "-" and error == False:
    Ergebnis = Zahl1 - Zahl2
elif operator == "*" and error == False:
    Ergebnis = Zahl1 * Zahl2
elif operator == "/" and error == False:
     Ergebnis = Zahl1 / Zahl2
else:
  print("Eingabefehler")
if error == False:
    print(f"Das Ergebnis ist {Ergebnis}")
else:
   print("Bro was war dein Ziel? Versuch es normal mit richtigen Eingaben")


