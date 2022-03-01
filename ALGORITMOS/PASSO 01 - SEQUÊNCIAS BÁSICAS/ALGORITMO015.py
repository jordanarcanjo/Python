##  Crie um programa que leia o número de dias trabalhados em um mês
##  e mostre o salário de um funcionário
##  sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada

diastrabalhados=int(input('Digite a quantidade de dias trabalhados no mês:'))

dia = 8*25
salario = (diastrabalhados*dia)

print('O valor total do dia é de R$ {}'. format(dia))
print('O valor total de {} dias trabalhados é de R$ {}'.format(diastrabalhados,salario))
