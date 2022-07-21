#Valores apenas para estudos, não condiz com a realidade.
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu imc está em {:.3f} você está abaixo do peso.'.format(imc))
elif imc == 18.5 and imc < 25:
    print('Seu imc está em {:.3f} você está com o peso ideal.'.format(imc))
elif imc == 25 and imc < 30:
    print('Seu imc está em {:.3f} você está com sobrepeso.'.format(imc))
elif imc == 30 and imc < 40:
    print('Seu imc está em {:.3f} você está com obesidade.'.format(imc))
else:
    print('Seu imc está em {:.3f} você está com obesidade morbida.'.format(imc))
