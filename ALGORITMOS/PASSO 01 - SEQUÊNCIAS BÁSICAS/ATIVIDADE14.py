## A locadora de carros precisa da sua ajuda para cobrar seus serviços
## Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
## Calcule o preço total a pagar
## sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.


km=float(input('Digite a quantidade de KM percorridos do veículo:'))
dias = float(input('Digite a quantidade de dias alugados do veículo: '))

totaldias = (dias*90)
totalkm   = (km*0.20)

print('O valor total  de dias é de: R$ {}'.format(totaldias))
print('O valor total  de km é de: R$ {}'.format(totalkm))

totalpagar = (totaldias+totalkm)

print('O valor total a ser pago no total é de: R$ {}'.format(totalpagar))
