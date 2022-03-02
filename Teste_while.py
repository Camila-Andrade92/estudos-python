from random import randint
velocidade=randint(75,100)
print("Iremos medir sua velocidade.")
print(velocidade)
multa=(velocidade-80)*7
print("Se sua velicidade for superior a 80km/h você será multado R$ 7,00 por km excedente.")
if velocidade >80:
    print("Você será multado, você pagará:{}.".format(multa))
else:
    ("Parabéns!")
