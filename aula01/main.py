from datetime import datetime

impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27,
           29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53,
           55, 57, 59]

este_minuto = datetime.today().minute

if este_minuto in impares:
   print("Este minuto parece um pouco... ímpar.")
else:
   print("Não é um minuto ímpar.")
