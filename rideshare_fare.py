error = False

# Abfrage des Fahrtenupgrade
ride_type = input("Möchten sie ein Fahrtenupgrade (plus oder comfort)? ")

# Abfrage der verfpgbaren Credits
credits =  (input("Wie viele Credits haben Sie? "))

try:
    credits = float(credits)
except:
    print("Bitte geben Sie eine gültige Zahl ein")
    error = True





ride_price = 0
final_price = 0

if "plus" == ride_type.lower():
    ride_price = 20.5
elif "comfort" == ride_type.lower():
    ride_prince = 37.9
else:
    ride_price = 18.7



print(f"Der Fahrpreis beträgt. {ride_price} Euro")

if error == False:

    if credits > 0:
        final_price = ride_price - credits
    else:
        final_price = ride_price
else:
    print("Fehler bei der Eingabe der Credits.")

print(f"Der finale Fahrpreis nach Verrechnung der Credits beträgt: {final_price}")