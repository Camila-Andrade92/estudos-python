#Faça um programa que leia um número inteiro e mostre os primeiros elementos de 
#uma sequência fibonnacci

n=int(input("Quantos termos você quer mostrar? "))
n1=0
n2=1
n3=(n1+n2)
print("--"*30)
contador=3#pq já tem os valores de n1, n2, n3
print("A sequência febonacci do número escolhido é:")
while contador <= n:
    contador += 1
    print("{} -> {} -> ".format(n1,n2), end="")
    print("{}".format(n3), end="")
    n1=n2#faz com que os n eles andem e somam os próximos valores
    n2=n3

print("Fim!")
