#Guilherme Carvalho

#1
import math

def eq_seg_grau(a, b, c):
    
    discriminante = b**2 - 4*a*c
    
   
    if discriminante < 0:
        return "Não há raízes reais"
    elif discriminante == 0:
       
        raiz = -b / (2*a)
        return raiz
    else:
       
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2

def bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Exemplos de uso
print(eq_seg_grau(1, -3, 2))  # Saída: (2.0, 1.0)
print(eq_seg_grau(1, -2, 1))   # Saída: 1.0
print(eq_seg_grau(2, 4, 2))    # Saída: -1.0

print(bissexto(2020))  # Saída: True
print(bissexto(1900))  # Saída: False
print(bissexto(2000))  # Saída: True



#2

def calcular_salario(salario_por_hora, horas_trabalhadas):
    salario_total = salario_por_hora * horas_trabalhadas
    return salario_total

salario_por_hora = float(input("Digite o salário por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_final = calcular_salario(salario_por_hora, horas_trabalhadas)
print("O salário a ser recebido é:", salario_final)
