### Constants and Variables###

ride_price = 0
final_price = 0



#Abfrage upgrade
print("start")
ride_type = input("Möchten Sie ein Fahrtenupgrade (plus oder comfort)?")

#Abfrage Credits
credits =input("Wie viele Credits haben Sie?")

try:
    credits = float(credits)
except:
    print ("Bitte geben Sie eine gültige Zahl ein.")
    error = True

#Berechnung Rideprice

if ride_type.lower() == "comfort":
    ride_price = 20.5

elif ride_type.lower() == "plus":
    ride_price = 37.9

else:
    ride_price = 18.7

#Verrechnung mit Credits
if credits > 0:
    final_price = ride_price - credits
    print(final_price)

else:
    print(final_price)
