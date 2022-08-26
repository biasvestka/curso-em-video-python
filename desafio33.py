a = int(input('Digite um número inteiro: '))  #entrada dos 3 número sem o "for" pq n tinha aprendido ainda
b = int(input('Digite outro número:'))
c = int(input('Digite outro número: '))
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
#define qual número é o maior e qual é menor
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print('O maior número é {}{}{} e o menor é {}{}{}.'. format('\033[1;34m', maior, '\033[m', '\033[1;31m', menor, '\033[m'))
