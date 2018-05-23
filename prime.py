#Primerzahlen ja/nein
zahl = input("Geben Sie eine Zahl ein")
z =int(zahl)
primer = False
for i in range(2,z):
  if(z%i==0):
    primer = True
    break
if (primer):
  print("Es ist keine Primerzahl")
else:
  print("Es ist eine Primerzahl")
    
