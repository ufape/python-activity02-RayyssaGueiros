# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 2 - Problem 3
# Description:
"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
Digite 6 valores inteiros quaisquer.
Exemplo:
Digite o valor 1/6: 2
Digite o valor 2/6: 3
Digite o valor 3/6: 4
Digite o valor 4/6: 5
Digite o valor 5/6: 6
Digite o valor 6/6: 7

Processes:
Faça um programa que leia 6 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Output(s):
Exemplo:
Você digitou 3 valores pares.
"""


def main():

  def quarto(a, b, c, d, f, g):
    lista = [a, b, c, d, f, g]
    j = 0
    for i in range(len(lista)):
      if lista[i] % 2 == 0:
        j = j + 1
      i = i + 1
    return print("Você digitou " + str(j) + " valores pares.")

  a = int(input("Digite o valor 1/6: "))
  b = int(input("Digite o valor 2/6: "))
  c = int(input("Digite o valor 3/6: "))
  d = int(input("Digite o valor 4/6: "))
  f = int(input("Digite o valor 5/6: "))
  g = int(input("Digite o valor 6/6: "))

  quarto(a, b, c, d, f, g)


if __name__ == '__main__':
  main()
