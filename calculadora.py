# -*- coding: utf-8 -*-
"""Calculadora.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uiBP28k5cF0Tvt2hA2PnfitxLbHK60Gz
"""

from re import A
print("Olá, sejá bem vindo.")
num1 = int(input("Digite o primeiro número: ")) # Recebe o valor do primeiro número e convertendo em int
num2 = int(input("Digite o segundo número: ")) # Recebe o valor do segundo número e convertendo em int
operacao = (input("Escolha a operação desejada:\n A para adição\n S para subtração\n M para multiplicação\n D para divisão\n")) # Usuário escolhe qual tipo de operação deseja efetuar: A para adição / S para subtração / M para multiplicação / D para divisão
if operacao == 'A': #
  adi = num1 + num2
  print("Resultado: ",adi)
elif operacao == 'S':
  sub = num1 - num2
  print("Resultado: ",sub)
elif operacao == 'M':
  mul = num1 * num2
  print("Resultado: ", mul)
elif operacao == 'D':
  div = num1 / num2
  print("Resultado:",div)