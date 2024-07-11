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


#exercicio0022

#nome =  str(input('Digite seu nome:')).strip()
#print('Analisando seu nome...')
#print('Seu nome rm Maiuscula é {}'.format(nome.upper()))
#print('Seu nome em minuscula é {}'.format(nome.lower()))
#print('Seu nome tem aotodo {} letras'.format(len(nome) - nome.count(' ')))
##print('Seu primeiro nome tem {} ltras'.format(nome.find(' ')))
#separa = nome.split()
#print('Seu primeiro nome é {}e ele tem {} letras'.format(separa[0], len(separa[0])))

#exercicio0023

#num = int(input('Informe numero:'))
#n = str(num)
#print('Analisando o numero: {}'.format(num))
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))




#exercicio0024

#cid = str(input('Em qual cidade você nasçeu?')).strip()
#print(cid[:5].upper() == 'SANTO')



#exercio0025

#@nome = str(input('Qual é seu nome completo?')).strip()
#print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))


#exercicio24

#frase = str(input('Digite uma frase?')).upper().strip()
#print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
#print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
#print('A ultima Letra A apareceu na posição: {}'.format(frase.rfind('A')+1))


#exercicio27

#n = str(input('Digite seu nome completo:')).strip()
#nome= n.split()
#print('Muito prazer em te conhecer!')
#print('Seu primeiro nome é {}'.format(nome[0]))
#print('Seu último nome é {}'.format(nome[len(nome)-1]))



#exercicio 28

#distância = float(input('Qual a distância da sua viagem?'))
#if distância <= 200:
 #   preço = distância * 0.50
#else:
#    preço = distância * 0.45
#preço =  distância * 0.50 if distância <= 200 else distância * 0.45
#print('E o preço da sua passagem sera de R${:.2f}'.format(preço))



#desafio29

from datetime import date
#ano = int(input('Que ano quer analisar?Coloque 0 para analisar o ano atual:'))
#if ano == 0:
   # ano = date.today().year
#if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0:
   # print('O ano{}é  BIXESTO'.format(ano))
#else:
    #print('O ano {} NÂO é BISSEXTO'.format (ano))



#exercicio 33
#a = int(input('Primeiro valor : '))
#b = int(input('segundo valor : '))
#c = int(input('terceiro valor : '))
#Verificar quem é o menor
#menor = a
#if b < a and b < c:
#    menor = b
#if c < a and c < b:
#    menor = c
#verificar quem é o maior
#maior = a
#if b > a and b> c:
#    maior = b
#if c > a and c > b:
#    maior = c
#print('O mair valor digitado foi : {}'.format(maior))
#print('O menor valor digitado foi : {}'.format(menor))

#exercicio34

#salário = float(input('Qual é o salário do funcionario? R$'))
#if salário <= 1250:
#    novo = salário + (salário * 15/100 )
#else:
#    novo = salário + (salário * 10/100 )
#print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))



#exercicio35
#print('-='*20)
#print('Analisador de Triandulos')
#print('-='*20)
#r1 = float(input('Primeiro seguimento ; '))
#r2 = float(input('Segundo seguimento ; '))
#r3 = float(input('Terceiro seguimento ; '))
#if r1 < r2 + r3 and r2 < r1 + r3 and r3 <r1 + r2:
#    print('Os seguimentos acima PODEM  formar triangulo!')
#else:
#    print('Os Seguimentos acima NÂO podem formar triandulo')




#Aula0012

#nome  =  str(input('Qual é seu nome?'))
#if nome == 'Gustavo':
#    print('Que nome bonito')
#elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
#   print('Seu nome é bem popular no Brasil')
#elif nome in 'Ana Claudia Jessica Juliana':
#    print('Belo nome feminino')
#else:
#    print('Seu nome é bem normaal')
#print ('Tenha um bom dia, {}!'.format(nome))


#exercicico36
#casa = float(input('valor da casa?'))
#Salário = float(input('Salário do comprador'))
#anos = int(input('Quantos anos de financiamento?'))
#prestação = casa / (anos * 12 )
#minímo = Salário * 30 / 100
#print('Para pagar uma casa de R${:.2}em {} anos'.format(casa, anos), end='')
#print('a prestação será de R${:.2f}'.format(prestação))
#if prestação <= minímo:
#    print('Emprestimo pode ser CONCEDIDO!')
#else:
#    print('Emprestimo negado')


#exercicio 37

#num = int(input('Digite um numero inteiro: '))
#print('''Escolhe uma das bases para a conversão:)
#[ 1 ] Converter para BINARIO
#[ 2 ] Converter para OCTAL
#[ 3 ] Convertar para HEXADECIMAL ''')
#opção = int(input('Sua opção:'))
#if opção == 1:
#    print('{} Convertido para BINÀRIO é igual a {}'.format(num, bin(num)[2:]))
#elif opção == 2:
#    print('{}convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
#elif opção == 3:
#    print('{} convertido para HEXADECIMAL é igual a {}'.format(num , hex(num)[2:]))
#else:
#    print('Opção invalida tente novamente')


#exercicio 38
#n1 = int(input('primeiro numero: '))
#n2 = int(input('segundo numero: '))
#if n1 > n2:
#    print('o Primeiro numero é maior')
#elif n2 > n1:
#    print('o SEGUNDO numero é maior')
#elif n1 == n2:
#    print('os numeros são iguais')

#exercicio 39

#from datetime import date
#atual = date.today().year
#nasc = int(input('Ano de nascimento: '))
#idade = atual - nasc
#print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
#if idade == 18:
#    print('Você tem que se alisar imediatamente!')
#elif idade < 18 :
#    saldo = 18 - idade
#    print('Ainda faltam {} anos para o alistamento'.format(saldo))
#    ano = atual = saldo
#    print('Seu alistamento sera em {}'.format(ano))
#elif idade > 18:
#    saldo = idade - 18
#    print('Você já deveria ter se alistado há {} anso'.format(saldo))
#    ano = atual - saldo
#    print('Seu alistamento foi em {}'.format(ano))



#exercicio 40

#nota1 = float(input('Primeira nota: '))
#nota2 = float(input('Segunda nota :'))
#m#édia = ( nota1 + nota2) / 2
#print('Tirando {:.1f} e {:.1f},a média do aluno é {:.1f}'.format(nota1, nota2, média))
#if  7 > média >= 5:
#    print('O aluno está em RECUPERAÇÃO')
#elif média < 5:
#    print("O aluno está REPROVADO")
#elif média >= 7 :
#    print('O aluno esta aprovado')


#exercicio 41

#from datetime import date
#atual = date.today().year
#nascimento = int(input('Ano de Nascimento:'))
#idade = atual - nascimento
#print('O atleta tem {} anos'.format(idade))
#if idade <= 9:
#    print('Classificação: MIRIM')
#elif idade <= 14:
#    print('Classificação: INFANTIL')
#elif idade <= 19:
#    print('Classificação: JUNIOR')
#elif idade <= 25:
#    print('Classificação: SÊNIOR')
#else:
#    print('Classificação: MASTER')

#r1 = float(input("primeiro segmento: "))
#r2 = float(input('segundo segmento: '))
#r3 = float(input('terceiro segmento: '))
#if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
#    if r1 == r2 == r3:
#        print('EQUILATERO')
#    elif r1 != r2 != r3 != r1:
#        print('ESCALENO')
#   else:
#        print('ISOSCELES')
#else:
#    print('Os segmentos acima NÃO PODEM FORMAR triângulo')





#exercicio 43

peso= float(input('qual é seu peso? (Kg) '))
altura = float(input('qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está ABAIXO do peso normal')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO')
elif 30 <= imc < 40:
    print('Voce está em OBESIDADE!')
elif imc >= 40:

    print('Voce está em OBESIDADE MÓRBIDA, cuidado!')