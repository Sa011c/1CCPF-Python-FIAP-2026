#Atividade 1
from numba.cpython.randomimpl import np_gauss_impl1

nome01 = input("Qual o seu nome?")
print(f"Bem-vindo(a), {nome01}!")

#Desafio 2
nome02 = input("Qual o seu nome?")
dia = int(input("Qual o dia do seu nascimento?"))
mes = int(input("Qual o mês do seu nascimento?"))
ano = int(input("Qual o ano do seu nascimento?"))
print(f"Olá, {nome02}! você nasceu no dia {dia}/{mes}/{ano}")


#Desafio 3
num1 = float(input("Escolha um número de 1 á 20:"))
num2 = float(input("Escolha mais um número de 1 á 20:"))
soma = (num1 + num2)

print(f"A soma dos dosi números escolhidos é {soma} ")
