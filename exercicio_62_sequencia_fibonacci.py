#Faça um programa que leia um número inteiro e mostre os primeiros elementos de 
#uma sequência fibonnacci

numero=int(input("Quantos termos você quer mostrar? "))
numero1=0
numero2=1
numero3=(numero1+numero2)
print("--"*30)
contador=3#pq já tem os valores de n1, n2, n3
print("A sequência febonacci do número escolhido é:")
while contador <= numero:
    contador += 1
    print("{} -> {} -> ".format(numero1,numero2), end="")
    print("{}".format(numero3), end="")
    nnumero1=numero2#faz com que os n eles andem e somam os próximos valores
    nnumero2=numero3

print("Fim!")

