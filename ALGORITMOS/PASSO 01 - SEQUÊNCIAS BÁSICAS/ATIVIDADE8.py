metro=float(input('Digite uma distância em metros: '))

print('A distância de {}m corresponde a:'.format(metro))

km= metro/1000
hm= metro/100
dam=metro/10
dm= metro*10
cm= metro*100
mm= metro*1000

print( '{}Km'.format(km))
print( '{}Hm'.format(hm))
print( '{}Dam'.format(dam))
print( '{}Dm'.format(dm))
print( '{}Cm'.format(cm))
print( '{}Mm'.format(mm))

