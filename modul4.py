import random
import math


while True:
  svar = input("Skriv vad du vill(skriv q för att avsluta programmet): ")
  if svar == "q":
    break
  print(svar)



ten = input("Skriv något: ")
for i in range(10):
    print(ten)



for i in range(1,11):
   print(i)



y = int(input("Skriv ett tal: "))
for i in range(1,y+1):
   print(i)


for table in range(1, 13):
   for factor in range(1, 11):
      produkt = table * factor
      print(f"{table} * {factor} = {produkt}")


x = int(input("Skriv bas (x): ")) 
y = int(input("Skriv exponent (y): ")) 
potens = 1 
for i in range(y): 
  potens *= x 
  print(f"{x}^{y} = {potens}")