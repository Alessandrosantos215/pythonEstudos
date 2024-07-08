#n1 = int(input('digite um numero:'))
#n2 = int(input('outro numero:'))

#s= n1 + n2
#m= n1 - n2
#d= n1 / n2
#i= n1 // n2
#v= n1 * n2

#print('a soma é {}, a subtração é {}, a divisão é igual a {}'.format(s, m, d), end = '')
#print ('divisão inteira {} e a multiplicação {}'.format(i,v))


#n1 = int(input('digite um numero: '))
#n2 = int(input('digite outro numeto:'))

#s = n1 + n2
#m = n1 + n2 - 1
#f = n1 + n2 + 1
#print( 'a soma é igual a {} seu antecessor é {} seu sucessor é {}'.format(s,m,f) )

#n1 = int(input('digite o alritimo:'))
#d= n1*2
#t= n1*3
#r= n1**2

#print('o dobro é {} o triplo é {} e a raiz quadrada é igual a {}'.format(d,t,r))




#7
#n1 = int(input('digite a primeira nota:'))
#n2 = int(input('digite a segunda nota:'))
#m = (n1 + n2)//2

#print ('a primeira nota é,{} a seguna foi,{} a media é igual a,{}'.format(n1,n2,m))




#8
#n1 = int(input('Digite o valor em metros:'))

#s = n1*100
#m = n1*1000
#print('o valor em metros é {}, e é igual a {} centimetros, e {} em milimitros'.format(n1,s,m))


#9
#n1 = int(input('digite um numero inteiro:'))

#print('a tabuada de {} é éssa {}'.format(n1,t))

#t=1* n1,2* n1,3*n1,4*n1,5*n1,6*n1,7*n1,8*n1,9*n1,10*n1


#10
#n1 = int(input('quanto voce tem na carteira:'))

#d = n1/3.27

#print('voce tem em reais {},e pode comprar {} dolares'.format(n1,d))

#11
#n1 = int(input('digite a largura da parede:'))
#n2 = int(input('digite a altura da parede:'))

#a = n1*n2
#m = a/2

#print('a area é igual a {}metros quadrados,para pintar é necessario {} litros de tinta '.format(a,m))

#12
#n1 = int(input( 'qual é o preço do produto?'))

#d = 5%-n1

#print('o valor do produto com o desconto é igual a {}'.format(d))


#13
#n1 = int(input('qual o salario?'))

#s = 15%-n1

#print('o salario com o almento de 15% é{}'.format(s))

#AULA006




#n = int(input('Digite um número:'))

#print('O dobro de {} vale {}.'.format(n, (n*2)))
#print(' triplo de {}. \n A raiz quadrada de {} é igual {}'.format(n,(n*3), n, pow(n, (1/2))))



#Aula007
#n1 = float(input('Primeira nota do aluno:'))
#n2 = float(input('Segunda nota do aluno:'))
#média = (n1 + n2) / 2
#print('A media entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))



#aula008

#medida = float(input('Uma distância em metroa: '))
#cm = medida * 100
#mm = medida * 1000
#print('A mediada de {}m corresponde a {}cm e {}mm'.format(medida, cm , mm))


#aula009
#num  = int(input('Digite um numero para ver sua tabuada: '))
#print('-'*12)
#print('{} * {:2} = {}'.format(num, 1 , num*1))
#print('{} * {:2} = {}'.format(num, 2, num*2))
#print('{} * {:2} = {}'.format(num, 3 ,num*3))
#print('{} * {:2} = {}'.format(num, 4 ,num*4))
#print('{} * {:2} = {}'.format( num, 5 , num*5))
#print('{} * {:2} = {}'.format(num, 6,num*6))
#print('{} * {:2} = {}'.format(num, 7 ,num*7))
#print('{} * {:2} = {}'.format(num, 8 ,num*8))
#print('{} * {:2} = {}'.format(num , 9 , num*9))
#print('{} * {:2} = {}'.format(num , 10 , num*10))
#print('-'*12)



#aula0010

#real = float(input('Quanto dinheiro você tem na carteira? R$'))
#dolar = real / 3.27
#print('Com R${:.2f}voçê pode comprar Us{:.2f}'.format(real, dolar))


#aula0011


#larg = float(input('lLargura da parede?'))
#alt = float(input('Autura da parede:'))
#área = larg * alt
#print('Sua parede tem a dimenção de {}*{} e sua área é de {}mª.'.format(larg, alt, área))
#tinta = área / 2
#print('Para pintar essa parede,voçê precisará de {}l de tinta.'.format(tinta))

#aula0012

#preço = float(input('Qual o preço do produto? R$'))
#novo = preço - (preço * 5  / 100)
#print ('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))


#salario = float(input('Qual é o saláro do funcionario:'))
#novo = salario + (salario * 15 / 100)
#print('Um funconario que ganhava R${}, com 15% de aumento,passa a receber R${}'.format(salario, novo))


#aula0014
#c = float(input('Informe a temperatura emºC: '))
#f = 9 * c / 5 + 32
#print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))

#aula0015
#dias = int(input('quantosd dias alugados?'))
#km = float(input('Quantos Km rodado?'))
#pago = (dias * 60) +  (km * 0.15)
#print('O total a pagar é de R${:.2f}'.format(pago))


#aula0016
#n1 = int(input(('Digite um numero inteiro:')))
#n2 = float + n1

#print('O numro inteiro{} e o seu fracionamento {}'.format(n1, n2 ))

from math import trunc
#num = float(input('Digite um valor:'))
#print("O valor digitado foi {} e a sua porção inteira é {}".format(num, trunc(num)))

#num = float(input('Digite um valor: '))
#print('O valor digitado foi {}e a sua porção inteira é {}'.format(num, int(num)))


#aula0017

#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2)  ** (1/2)
#print ('A hipotenusa vai medir {:.2f}'.format(hi))



#import math
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente:' ))
#hi = math.hypot(co, ca)
#print('A hipotenusa vai medir {:.2}'.format(hi))


#aula0018

#import math
#ângulo = float(input('Digite o ângulo que voce deseja:'))
#seno = math.sin(math.radians(ângulo))
#print('O ângulo de {}tem o SENO de {:.2f}'.format(ângulo, seno))
#cosseno = math.cos(math.radians(ângulo))
#print('O ângulo de {} tem cosseno de {:.2f}'.format(ângulo, cosseno))
#tangente = math.tan(math.radians((ângulo)))
#print ('Oângulo de {}tem a TANGENTE de {:.2f}'.format(ângulo, tangente))


#import random
#from ramdom import choice

#n1 = str(input('Primeiro aluno:'))
#2 = str(input('Segundo aluno:'))
#n3 = str(input('Terçeiro aluno:'))
#n4 = str(input('Quarto aluno:'))
#lista= [n1, n2, n3, n4]
#escolhido = random.choice(lista)
#print("O aluno escolhido foi {}".format(escolhido))


import random
#n1 = str(input('Primeiro aluno'))
#n2 = str(input('Segundo anuno'))
#n3 = str(input('Terceiro aluno'))
#n#4 = str(input('Quarto aluno'))
#lista = [n1, n2, n3, n4]
#random.shuffle(lista)
#print('A ordem de apresentação será')
#print(lista)


#exercicio21
#import pygame
#pygame.init()
#pygame.mixer.music.load('ex21.mp3')
#pygame.mixer.music.playa()
#pygame.event.wait()

#frase = 'Curso de video python'
#print(frase[:13])


