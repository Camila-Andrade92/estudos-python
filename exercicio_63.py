#Faça um programa que leia vários números inteiros e só pare quando digitar 999
#Mostre quantos números foram digitados e qual a soma deles
n1=int(input("Digite um número inteiro: "))
c=0
n=0
soma=0
#poderia ser c=n=soma=0
while n != 999:
    print("Pode digitar outro número: ")
    n=int(input())
    c+=1
    soma+=n#==soma=soma+n
    print("A soma dos números digitados é {}".format)
print("Até finalizar o programa você fez {} tentativas.".format(c))
#Para somar: 
print("Fim!")
