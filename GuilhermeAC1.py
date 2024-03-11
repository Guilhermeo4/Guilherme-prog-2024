#Guilherme Reis de Carvalho
#1

a = float (input(" entre com o valor de a: "))
b = float (input(" entre com o valor de b: "))
c = float (input(" entre com o valor de c: "))

delta= (b**2 - 4*a*c)
x1=( -b + delta**(1/2)) / (2*a)
x2=( -b - delta**(1/2)) / (2*a)

print('O valor do primeiro x é:', x1, ' o valor do segundo x é:', x2)

#2

ano = int (imput('Digite um ano de sua escolha:'))
bissexto =( ano % 4 == 0 and ano % 100! + 0) or (ano % 400 == 0 )
print (bissexto and f"{ano} é um ano bissexto."or f"{ano} não é um ano bissexto." ) 