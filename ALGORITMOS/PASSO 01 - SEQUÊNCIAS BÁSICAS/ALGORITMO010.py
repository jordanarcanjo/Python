largura=float(input('Digite a largura da parede: (cm)'))
altura=float(input('Digite a altura da parede: (cm)'))

area=(largura*altura)
areaTotal= (area/100)

print('A area total da parede é de {}' .format(areaTotal))

if (areaTotal>= 2):
    print('Irá precisar de apenas 1L de tinta!')
else:
    print('Irá precisar de mais de 1L de tinta!')
